import pytest
from models.kursus import Kursus
from models.peserta import Peserta
from models.pembayaran import Lunas, BelumLunas
from services.lembaga import LembagaKursus
from exceptions.custom_exceptions import KursusPenuhError

def test_harga_negatif():
    kursus = Kursus("Python", -1000, 10)
    assert kursus.harga < 0

def test_kapasitas_nol():
    kursus = Kursus("Java", 5000, 0)
    assert kursus.sisa_slot() == 0

def test_kursus_penuh():
    kursus = Kursus("C++", 2000, 1)
    peserta1 = Peserta("A", "a@mail.com", "123")
    kursus.tambah_peserta(peserta1)
    with pytest.raises(Exception):
        kursus.tambah_peserta(Peserta("B", "b@mail.com", "456"))

def test_sisa_slot():
    kursus = Kursus("Go", 3000, 2)
    peserta = Peserta("C", "c@mail.com", "789")
    kursus.tambah_peserta(peserta)
    assert kursus.sisa_slot() == 1

def test_lunas_is_lunas():
    status = Lunas("2026-05-29")
    assert status.is_lunas() is True
    belum = BelumLunas()
    assert belum.is_lunas() is False

