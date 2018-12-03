# -*- coding: utf-8 -*-  

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem)
from Ui_MainWindow import *
from hxrpc import http_request

class HXMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HXMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.assets = self.prepareAssetSummary()
        self.assetSummaryTable.setRowCount(len(self.assets))
        self.assetSummaryTable.setColumnCount(2)
        self.assetSummaryTable.setHorizontalHeaderLabels(['资产', '数量'])
        assetTableLine = 0
        for k, v in self.assets.items():
            assetItem = QTableWidgetItem(k)
            self.assetSummaryTable.setItem(assetTableLine, 0, assetItem)
            if assetItem == 'HX':
                supplyItem = QTableWidgetItem(str(v))
            else:
                supplyItem = QTableWidgetItem(str(v))
            self.assetSummaryTable.setItem(assetTableLine, 1, supplyItem)
            assetTableLine += 1

    def prepareAssetSummary(self):
        assets = {'HX': 0, 'HC': 0, 'BTC': 0, 'ETH': 0, 'LTC': 0, 'PAX': 0}
        for asset in assets.keys():
            rsp = http_request('get_asset_imp', [asset])
            if rsp is not None:
                if asset == 'HX':
                    assets[asset] = int(rsp['dynamic_data']['current_supply']) / 100000
                else:
                    assets[asset] = int(rsp['dynamic_data']['current_supply']) / 100000000
        return assets

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = HXMainWindow()
    myWin.show()
    sys.exit(app.exec_())