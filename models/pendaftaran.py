class Pendaftaran:
    def __init__(self, peserta, kursus, status_pembayaran):
        self.peserta = peserta
        self.kursus = kursus
        self.status_pembayaran = status_pembayaran

    def bayar(self, status_pembayaran_baru):
        self.status_pembayaran = status_pembayaran_baru

