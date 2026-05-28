from exceptions.custom_exceptions import (
    KursusPenuhError, PesertaSudahTerdaftarError,
    KursusTidakDitemukanError, PesertaTidakDitemukanError
)
from models.pendaftaran import Pendaftaran

class LembagaKursus:
    def __init__(self, nama):
        self.nama = nama
        self.kursus_list = []
        self.pendaftaran_list = []

    def tambah_kursus(self, kursus):
        self.kursus_list.append(kursus)

    def daftar_peserta(self, peserta, kursus):
        if kursus not in self.kursus_list:
            raise KursusTidakDitemukanError()
        if peserta in kursus.peserta:
            raise PesertaSudahTerdaftarError()
        if kursus.sisa_slot() <= 0:
            raise KursusPenuhError()
        kursus.tambah_peserta(peserta)
        pendaftaran = Pendaftaran(peserta, kursus, None)
        self.pendaftaran_list.append(pendaftaran)
        return pendaftaran

    def cari_peserta(self, nama):
        for p in self.pendaftaran_list:
            if p.peserta.nama == nama:
                return p.peserta
        raise PesertaTidakDitemukanError()
