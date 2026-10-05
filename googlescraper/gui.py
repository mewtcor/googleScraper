"""PyQt5 window with a Google Map tab and a Google Search tab."""

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QStyle

from googlescraper import export, places, web_search


def _warn(title, text):
    QMessageBox.information(None, title, text, QMessageBox.Ok)


def _button(text, style, icon):
    return QtWidgets.QPushButton(style.standardIcon(icon), text)


def _ask_save_path():
    path, _ = QFileDialog.getSaveFileName(
        None, "Save results", "", "CSV Files (*.csv);;All Files (*)",
        options=QFileDialog.DontUseNativeDialog)
    return path


class MapTab(QtWidgets.QWidget):
    """Look up brick-and-mortar retailers with Google Maps."""

    def __init__(self, search_places=places.search_places, get_api_key=places.get_api_key):
        super().__init__()
        self._search_places = search_places
        self._get_api_key = get_api_key
        self.results = []

        style = self.style()
        self.query = QtWidgets.QLineEdit()
        self.brand = QtWidgets.QLineEdit()
        self.btn_load = _button("Load Data", style, QStyle.SP_BrowserReload)
        self.btn_clear = _button("Clear", style, QStyle.SP_DialogResetButton)
        self.btn_save = _button("Save", style, QStyle.SP_DialogSaveButton)
        self.btn_save.setEnabled(False)
        self.total = QtWidgets.QLabel("0")
        self.output = QtWidgets.QTextEdit(readOnly=True)

        form = QtWidgets.QFormLayout()
        form.addRow("Retailer Search:", self.query)
        form.addRow("Brand:", self.brand)
        buttons = QtWidgets.QHBoxLayout()
        for w in (self.btn_load, self.btn_clear, self.btn_save):
            buttons.addWidget(w)
        buttons.addStretch()
        buttons.addWidget(QtWidgets.QLabel("URLs:"))
        buttons.addWidget(self.total)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(buttons)
        layout.addWidget(self.output)

        self.btn_load.clicked.connect(self.load)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_save.clicked.connect(self.save)

    def load(self):
        if not self.query.text().strip():
            _warn("Empty Field", "Please make sure the search box is filled.")
            self.query.setFocus()
            return
        if not self.brand.text().strip():
            _warn("Empty Field", "Type in the brand.")
            self.brand.setFocus()
            return
        try:
            self.results = self._search_places(self.query.text(), self._get_api_key())
        except places.PlacesError as e:
            _warn("Google Maps", str(e))
            return
        self.output.clear()
        for place in self.results:
            self.output.append(f"{place.name} | {place.address}")
        self.total.setText(str(len(self.results)))
        self.btn_save.setEnabled(bool(self.results))

    def clear(self):
        self.results = []
        self.output.clear()
        self.query.clear()
        self.brand.clear()
        self.total.setText("0")
        self.btn_save.setEnabled(False)
        self.query.setFocus()

    def save(self, path=None):
        path = path or _ask_save_path()
        if path:
            export.save_places(path, self.brand.text(), self.results)
            _warn("Save File", "File has been saved.")


class SearchTab(QtWidgets.QWidget):
    """Find online retailers for a keyword with Google Search."""

    def __init__(self, search_urls=web_search.search_urls):
        super().__init__()
        self._search_urls = search_urls
        self.domains = []

        style = self.style()
        self.query = QtWidgets.QLineEdit()
        self.count = QtWidgets.QSpinBox(minimum=1, maximum=100, value=10)
        self.brand = QtWidgets.QLineEdit()
        self.btn_load = _button("Load URLs", style, QStyle.SP_BrowserReload)
        self.btn_clear = _button("Clear", style, QStyle.SP_DialogResetButton)
        self.btn_save = _button("Save", style, QStyle.SP_DialogSaveButton)
        self.btn_save.setEnabled(False)
        self.total = QtWidgets.QLabel("0")
        self.raw = QtWidgets.QTextEdit(readOnly=True)
        self.domain_list = QtWidgets.QTextEdit(readOnly=True)

        form = QtWidgets.QFormLayout()
        form.addRow("Keyword Search:", self.query)
        form.addRow("No. of results to retrieve?", self.count)
        form.addRow("Brand:", self.brand)
        buttons = QtWidgets.QHBoxLayout()
        for w in (self.btn_load, self.btn_clear, self.btn_save):
            buttons.addWidget(w)
        buttons.addStretch()
        buttons.addWidget(QtWidgets.QLabel("URL count:"))
        buttons.addWidget(self.total)
        results = QtWidgets.QGridLayout()
        results.addWidget(QtWidgets.QLabel("Raw result:"), 0, 0)
        results.addWidget(QtWidgets.QLabel("Domains only:"), 0, 1)
        results.addWidget(self.raw, 1, 0)
        results.addWidget(self.domain_list, 1, 1)
        results.setColumnStretch(0, 3)
        results.setColumnStretch(1, 1)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addLayout(form)
        layout.addLayout(buttons)
        layout.addLayout(results)

        self.btn_load.clicked.connect(self.load)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_save.clicked.connect(self.save)

    def load(self):
        if not self.query.text().strip():
            _warn("Empty Field", "Please make sure the search box is filled")
            self.query.setFocus()
            return
        if not self.brand.text().strip():
            _warn("Empty Field", "Type in the brand.")
            self.brand.setFocus()
            return
        try:
            urls = self._search_urls(self.query.text(), self.count.value())
        except web_search.SearchError as e:
            _warn("Google Search", str(e))
            return
        self.domains = [web_search.extract_domain(u) for u in urls]
        self.raw.setPlainText("\n".join(urls))
        self.domain_list.setPlainText("\n".join(self.domains))
        self.total.setText(str(len(urls)))
        self.btn_save.setEnabled(bool(urls))

    def clear(self):
        self.domains = []
        self.raw.clear()
        self.domain_list.clear()
        self.query.clear()
        self.brand.clear()
        self.count.setValue(10)
        self.total.setText("0")
        self.btn_save.setEnabled(False)
        self.query.setFocus()

    def save(self, path=None):
        path = path or _ask_save_path()
        if path:
            export.save_domains(path, self.brand.text(), self.domains)
            _warn("Save File", "File has been saved.")


class MainWindow(QtWidgets.QWidget):
    def __init__(self, map_tab=None, search_tab=None):
        super().__init__()
        self.setWindowTitle("Google Scraper")
        self.resize(1066, 640)
        self.map_tab = map_tab or MapTab()
        self.search_tab = search_tab or SearchTab()
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self.map_tab, "Google Map")
        tabs.addTab(self.search_tab, "Google Search")
        btn_close = _button("Close", self.style(), QStyle.SP_DialogCloseButton)
        btn_close.clicked.connect(self.close)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(tabs)
        layout.addWidget(btn_close)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()
