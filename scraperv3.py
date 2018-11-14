#!/usr/bin/python

import sys
import urllib.request
import json
import csv
from googlesearch import search
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import tldextract


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1066, 640)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(450, 580, 161, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(600)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnClose = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "/Users/mewt/eclipse-workspace/testProject/Close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClose.setIcon(icon)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_2.addWidget(self.btnClose)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1051, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tabgooglemap = QtWidgets.QWidget()
        self.tabgooglemap.setObjectName("tabgooglemap")
        self.textArea = QtWidgets.QTextEdit(self.tabgooglemap)
        self.textArea.setGeometry(QtCore.QRect(10, 110, 1021, 401))
        self.textArea.setObjectName("textArea")
        self.lineEdit = QtWidgets.QLineEdit(self.tabgooglemap)
        self.lineEdit.setGeometry(QtCore.QRect(130, 15, 895, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabgooglemap)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 469, 48))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnScrape = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "/Users/mewt/eclipse-workspace/testProject/process.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnScrape.setIcon(icon1)
        self.btnScrape.setObjectName("btnScrape")
        self.horizontalLayout.addWidget(self.btnScrape)
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(
            "/Users/mewt/eclipse-workspace/testProject/edit-clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnClear.setIcon(icon2)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.btnSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(
            "/Users/mewt/eclipse-workspace/testProject/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSave.setIcon(icon3)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setEnabled(False)
        self.horizontalLayout.addWidget(self.btnSave)
        self.label_3 = QtWidgets.QLabel(self.tabgooglemap)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 161, 25))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabgooglemap)
        self.label_4.setGeometry(QtCore.QRect(930, 70, 51, 25))
        self.label_4.setObjectName("label_4")
        self.lblTotal = QtWidgets.QLabel(self.tabgooglemap)
        self.lblTotal.setGeometry(QtCore.QRect(978, 70, 61, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(50)
        self.lblTotal.setFont(font)
        self.lblTotal.setObjectName("lblTotal")
        self.tabWidget.addTab(self.tabgooglemap, "")
        self.tabgooglesearch = QtWidgets.QWidget()
        self.tabgooglesearch.setObjectName("tabgooglesearch")
        self.textArea_2 = QtWidgets.QTextEdit(self.tabgooglesearch)
        self.textArea_2.setGeometry(QtCore.QRect(10, 120, 765, 391))
        self.textArea_2.setObjectName("textArea_2")
        self.textArea_3 = QtWidgets.QTextEdit(self.tabgooglesearch)
        self.textArea_3.setGeometry(QtCore.QRect(750, 120, 255, 391))
        self.textArea_3.setObjectName("textArea_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tabgooglesearch)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 16, 885, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tabgooglesearch)
        self.label_5.setGeometry(QtCore.QRect(900, 70, 71, 25))
        self.label_5.setObjectName("label_5")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabgooglesearch)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 50, 462, 48))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.verticalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnScrape_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnScrape_2.setIcon(icon1)
        self.btnScrape_2.setObjectName("btnScrape_2")
        self.horizontalLayout_3.addWidget(self.btnScrape_2)
        self.btnClear_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnClear_2.setIcon(icon2)
        self.btnClear_2.setObjectName("btnClear_2")
        self.horizontalLayout_3.addWidget(self.btnClear_2)
        self.btnSave_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btnSave_2.setIcon(icon3)
        self.btnSave_2.setObjectName("btnSave_2")
        self.btnSave_2.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.btnSave_2)
        self.label = QtWidgets.QLabel(self.tabgooglesearch)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tabgooglesearch)
        self.label_2.setGeometry(QtCore.QRect(500, 56, 231, 25))
        self.label_2.setObjectName("label_2")
        self.leditUrlInput = QtWidgets.QLineEdit(self.tabgooglesearch)
        self.leditUrlInput.setGeometry(QtCore.QRect(660, 53, 61, 25))
        self.leditUrlInput.setObjectName("leditUrlInput")
        self.lblTotal_2 = QtWidgets.QLabel(self.tabgooglesearch)
        self.lblTotal_2.setGeometry(QtCore.QRect(978, 70, 61, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(50)
        self.lblTotal_2.setFont(font)
        self.lblTotal_2.setObjectName("lblTotal_2")
        self.tabWidget.addTab(self.tabgooglesearch, "")
        self.textArea.setReadOnly(True)
        self.textArea_2.setReadOnly(True)
        self.label_6 = QtWidgets.QLabel(self.tabgooglesearch)
        self.label_6.setGeometry(QtCore.QRect(10, 95, 71, 25))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tabgooglesearch)
        self.label_7.setGeometry(QtCore.QRect(750, 95, 91, 25))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tabgooglesearch)
        self.label_8.setGeometry(QtCore.QRect(500, 93, 321, 25))
        self.label_8.setObjectName("label_8")
        self.txtBrand = QtWidgets.QLineEdit(self.tabgooglesearch)
        self.txtBrand.setGeometry(QtCore.QRect(543, 90, 180, 25))
        self.txtBrand.setObjectName("txtBrand")
        self.label_9 = QtWidgets.QLabel(self.tabgooglemap)
        self.label_9.setGeometry(QtCore.QRect(515, 70, 321, 25))
        self.label_9.setObjectName("label_9")
        self.txtBrand2 = QtWidgets.QLineEdit(self.tabgooglemap)
        self.txtBrand2.setGeometry(QtCore.QRect(560, 70, 180, 25))
        self.txtBrand2.setObjectName("txtBrand2")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        # bind  btnclose
        self.btnClose.clicked.connect(Form.close)
        # bind  btnScrape
        self.btnScrape.clicked.connect(self.GetDataGMap)
        # bind btnClear
        self.btnClear.clicked.connect(self.ClearFieldsGMap)
        # bind btnScrape_2
        self.btnScrape_2.clicked.connect(self.GetDataGoogle)
        # bind btnClear_2
        self.btnClear_2.clicked.connect(self.ClearFieldsGoogle)
        #  bind btnSave (GMap)
        self.btnSave.clicked.connect(self.saveMap)
        # bind btnSave_2(Google search)
        self.btnSave_2.clicked.connect(self.saveGoogleSearch)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Google Scraper"))
        self.btnClose.setText(_translate("Form", "Close"))
        self.btnScrape.setText(_translate("Form", "Load Data"))
        self.btnClear.setText(_translate("Form", "Clear"))
        self.btnSave.setText(_translate("Form", "Save"))
        self.label_3.setText(_translate("Form", "Retailer Search:"))
        self.label_4.setText(_translate("Form", "URLs:"))
        self.label_5.setText(_translate("Form", "URL count:"))
        self.lblTotal.setText(_translate("Form", "0"))
        self.lblTotal_2.setText(_translate("Form", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabgooglemap), _translate("Form", "Google Map"))
        self.btnScrape_2.setText(_translate("Form", "Load URLs"))
        self.btnClear_2.setText(_translate("Form", "Clear"))
        self.btnSave_2.setText(_translate("Form", "Save"))
        self.label.setText(_translate("Form", "Keyword Search:"))
        self.label_2.setText(_translate(
            "Form", "No. of results to retrieve?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabgooglesearch), _translate("Form", "Google Search"))
        self.label_6.setText(_translate("Form", "Raw result:"))
        self.label_7.setText(_translate("Form", "Domains only:"))
        self.label_8.setText(_translate("Form", "Brand:"))
        self.label_9.setText(_translate("Form", "Brand:"))

    def GetDataGMap(self):
        google_api = 'AIzaSyDzIeUqIwwXlnT_ZpXd-MDqHYsDexa_smc'
        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?&key=' + \
            google_api + '&query='

        self.btnSave.setEnabled(True)
        self.textArea.clear()
        if self.lineEdit.text() == "":
            QMessageBox.information(
                None, "Empty Field", "Please make sure the search box is filled.", QMessageBox.Ok)
            self.lineEdit.setFocus()
            self.btnSave.setEnabled(False)
        elif self.txtBrand2.text() == "":
            QMessageBox.information(
                None, "Empty Field", "Type in the brand.", QMessageBox.Ok)
            self.txtBrand2.setFocus()
            self.btnSave.setEnabled(False)
        else:
            count = 0
            self.gmapquery = self.lineEdit.text()
            search = self.gmapquery.replace(' ', '+')
            final_url = url + search + \
                '&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry'
            response = urllib.request.urlopen(final_url).read()
            json_obj = str(response, 'utf-8')
            self.gmapdata = json.loads(json_obj)

            for item in self.gmapdata['results']:
                count = count + 1
                retailer = item['name']
                address = item['formatted_address']
#                 self.textArea.append(dict)
                self.textArea.append(retailer + ' | ' + address)
                self.lblTotal.setText(str(count))

    def GetDataGoogle(self):
        self.btnSave_2.setEnabled(True)
        self.dict = []
        self.textArea_2.clear()
        getURLValue = self.lineEdit_2.text()
        getDomValue = self.leditUrlInput.text()
        if getURLValue == "":
            QMessageBox.information(
                None, "Empty Field", "Please make sure the search box is filled", QMessageBox.Ok)
            self.lineEdit_2.setFocus()
            self.btnSave_2.setEnabled(False)
        elif getDomValue == "":
            QMessageBox.information(
                None, "Empty Field", "Type in the number of results  to retrieve.", QMessageBox.Ok)
            self.leditUrlInput.setFocus()
        elif self.txtBrand.text() == "":
            self.txtBrand.setFocus()
            QMessageBox.information(
                None, "Empty Field", "Type in the brand.", QMessageBox.Ok)
        else:
            urls = int(self.leditUrlInput.text())
            query = self.lineEdit_2.text()
            count = 0
            search_query = search(
                query, tld="com", lang="en", num=urls, stop=1, pause=2)
            for item in search_query:
                count = count + 1
                extracted = tldextract.extract(item)
                fin_items = "{}.{}".format(
                    extracted.domain, extracted.suffix)
                self.textArea_2.append(item)
                self.textArea_3.append(fin_items)
                brand = self.txtBrand.text()
#                     d = {'url': fin_items}
                d = {'OLRetailer': fin_items, 'Brand': brand}
                self.dict.append(d)
                self.lblTotal_2.setText(str(count))

    def ClearFieldsGMap(self):
        self.textArea.clear()
        self.lineEdit.clear()
        self.lineEdit.setFocus()
        self.lblTotal.clear()
        self.btnSave.setEnabled(False)
        self.txtBrand2.clear()

    def ClearFieldsGoogle(self):
        self.textArea_2.clear()
        self.lineEdit_2.clear()
        self.lineEdit_2.setFocus()
        self.leditUrlInput.clear()
        self.lblTotal_2.clear()
        self.textArea_3.clear()
        self.btnSave_2.setEnabled(False)
        self.txtBrand.clear()

    def saveMap(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            None, "QFileDialog.getSaveFileName()", "", "All Files (*);;CSV Files (*.csv)", 'w', options=options)
        if fileName != "":
            w = open(fileName + '.csv', 'w')
            csv_writer = csv.writer(w)
            csv_writer.writerow(['Brand', 'B&M', 'Address', 'ContactNo'])
            for item in self.gmapdata['results']:
                retailer = item['name']
                address = item['formatted_address']
                brand = self.txtBrand2.text()
                contact = ''
                csv_row = (brand, retailer, address, contact)
                csv_writer.writerow(csv_row)
            QMessageBox.information(
                None, "Save File", "File has been saved.", QMessageBox.Ok)

    def saveGoogleSearch(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            None, "QFileDialog.getSaveFileName()", "", "All Files (*);;CSV Files (*.csv)", 'w', options=options)
        if fileName != "":
            w = open(fileName + '.csv', 'w')
            csv_writer = csv.writer(w)
            csv_writer.writerow(['Brand', 'OLRetailer'])
            for k in self.dict:
                online_retailer = k.get('OLRetailer')
                brand_retailer = k.get('Brand')
                csv_row = (brand_retailer, online_retailer)
#                 csv_writer.writerow(csv_row)
                csv_writer.writerow(csv_row)
            QMessageBox.information(
                None, "Save File", "File has been saved.", QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    UI = Ui_Form()
    UI.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
