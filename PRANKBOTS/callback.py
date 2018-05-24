# -*- coding: utf-8 -*-
class LineCallback(object):

    def __init__(self, callback):
        self.callback = callback

    def PinVerified(self, pin):
        self.callback("Masukkan kode pin berikut '" + pin + "' kedalam aplikasi LINE mu dalam 2 menit")

    def QrUrl(self, url, showQr=True):
        self.callback("Salin link berikut dan pastekan pada alikasi LINE mu kemudian klik dalam 2 menit \n" + url)
        if showQr:
            import pyqrcode
            url = pyqrcode.create(url)
            self.callback(url.terminal('green', 'white', 1))

    def default(self, str):
        self.callback(str)