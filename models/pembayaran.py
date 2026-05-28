from abc import ABC, abstractmethod

class StatusPembayaran(ABC):
    @abstractmethod
    def keterangan(self):
        pass

    @abstractmethod
    def is_lunas(self):
        pass

class Lunas(StatusPembayaran):
    def __init__(self, tanggal_bayar):
        self.tanggal_bayar = tanggal_bayar

    def keterangan(self):
        return f"Lunas pada {self.tanggal_bayar}"

    def is_lunas(self):
        return True

class BelumLunas(StatusPembayaran):
    def keterangan(self):
        return "Belum Lunas"

    def is_lunas(self):
        return False

