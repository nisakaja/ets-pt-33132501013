
class Lampu:
    def __init__(self, nama):
        self.nama = nama
        self.aktif = False
        self.kecerahan = 0

    def nyalakan(self):
        self.aktif = True

    def matikan(self):
        self.aktif = False

    def atur(self, nilai):
        if 0 <= nilai <= 100:
            self.kecerahan = nilai
