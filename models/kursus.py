class Kursus:
    def __init__(self, nama, harga, kapasitas):
        self.nama = nama
        self._harga = harga
        self._kapasitas = kapasitas
        self.peserta = []

    @property
    def harga(self):
        return self._harga

    @property
    def kapasitas(self):
        return self._kapasitas

    def sisa_slot(self):
        return self._kapasitas - len(self.peserta)

    def tambah_peserta(self, peserta):
        if self.sisa_slot() <= 0:
            raise Exception("Kursus penuh")
        self.peserta.append(peserta)

class KursusDesain(Kursus):
    def __init__(self, nama, harga, kapasitas, software):
        super().__init__(nama, harga, kapasitas)
        self.software = software

class KursusPemrograman(Kursus):
    def __init__(self, nama, harga, kapasitas, bahasa_pemrograman):
        super().__init__(nama, harga, kapasitas)
        self.bahasa_pemrograman = bahasa_pemrograman

class KursusBahasa(Kursus):
    def __init__(self, nama, harga, kapasitas, bahasa_target, level):
        super().__init__(nama, harga, kapasitas)
        self.bahasa_target = bahasa_target
        self.level = level
