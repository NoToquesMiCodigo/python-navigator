# -*- coding: utf-8 -*-
# Tested in Python2.7

from PySide import QtCore, QtGui
from PySide import QtWebKit
from PySide import QtNetwork


class Navegador(QtGui.QWidget):

    def __init__(self):
        # constructor de la clase
        super(Navegador, self).__init__(parent=None)
        self.setWindowTitle("Python Navigator")
        self.showMaximized()
        self.gridLayout = QtGui.QGridLayout(self)
        self.btnAtras = QtGui.QPushButton(self, text='atras')
        self.gridLayout.addWidget(self.btnAtras, 0, 0, 1, 1)
        self.btnAdelante = QtGui.QPushButton(self, text='adelante')
        self.gridLayout.addWidget(self.btnAdelante, 0, 1, 1, 1)
        self.label = QtGui.QLabel(u"Dirección", self)
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.txtUrl = QtGui.QLineEdit(self)
        self.gridLayout.addWidget(self.txtUrl, 0, 3, 1, 1)
        self.wvNavegador = QtWebKit.QWebView(self)
        self.gridLayout.addWidget(self.wvNavegador, 1, 0, 1, 4)

        QtNetwork.QNetworkProxyFactory.setUseSystemConfiguration(True)
        QtWebKit.QWebSettings.globalSettings().setAttribute(
            QtWebKit.QWebSettings.PluginsEnabled, True)
        QtWebKit.QWebSettings.globalSettings().setAttribute(
            QtWebKit.QWebSettings.JavascriptCanOpenWindows, True)
        QtWebKit.QWebSettings.globalSettings().setAttribute(
            QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)

        QtCore.QObject.connect(
            self.txtUrl,
            QtCore.SIGNAL("returnPressed()"),
            self.cargarUrl)
        QtCore.QObject.connect(
            self.btnAtras,
            QtCore.SIGNAL("clicked()"),
            self.wvNavegador.back)
        QtCore.QObject.connect(
            self.btnAdelante,
            QtCore.SIGNAL("clicked()"),
            self.wvNavegador.forward)

        _url = "http://www.python.org"
        self.wvNavegador.load(QtCore.QUrl(_url))
        self.txtUrl.setText(_url)

    def cargarUrl(self):
        url = self.txtUrl.text()
        url = url if url.startswith(
            "http://") or url.startswith(
                "https://") else "http://{url}".format(
                    url=url)
        self.wvNavegador.load(QtCore.QUrl(url))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    nav = Navegador()
    nav.show()
    sys.exit(app.exec_())
