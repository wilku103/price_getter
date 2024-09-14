import requests, sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_mainwindow import Ui_MainWindow


def prepare_table(input_table):
    new_table = {}
    for row in input_table:
        new_table[row["code"]] = row

    return new_table


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # set default currency and get exchange rates
        self.current_currency = "USD"
        self.exchange = prepare_table(requests.get("https://api.nbp.pl/api/exchangerates/tables/C/").json()[0]["rates"])

        # setup UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_currencies()

        # connect signals
        self.ui.input.valueChanged.connect(self.update_exchanged)
        self.ui.currencies.selectionModel().currentChanged.connect(self.on_currency_changed)

    def setup_currencies(self):
        model = QStandardItemModel()
        self.ui.currencies.setModel(model)

        # add currencies to the list
        for currency in self.exchange.values():
            item = QStandardItem(f"{currency['code']} ({currency['currency']})")
            model.appendRow(item)

    def update_exchanged(self):
        self.ui.out.setValue(float(self.ui.input.value()) * self.exchange[self.current_currency]["bid"])

    def on_currency_changed(self):
        # update current currency and corresponding ui elements
        self.current_currency = self.ui.currencies.currentIndex().data().split(" ")[0]
        self.ui.currency_code.setText(self.current_currency)
        self.update_exchanged()


def main():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
