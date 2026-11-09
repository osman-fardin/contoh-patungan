import pytest

from patungan.hitung import bagi_rata, hitung_pelunasan, hitung_saldo


def buat_pengeluaran(pembayar, jumlah, peserta):
    return {
        "keterangan": "Makan",
        "pembayar": pembayar,
        "jumlah": jumlah,
        "peserta": peserta,
    }


def test_bagi_rata_tidak_menghilangkan_rupiah():
    hasil = bagi_rata(10000, ["Ani", "Budi", "Citra"])
    assert hasil == {"Ani": 3334, "Budi": 3333, "Citra": 3333}
    assert sum(hasil.values()) == 10000


def test_bagi_rata_tanpa_peserta_ditolak():
    with pytest.raises(ValueError):
        bagi_rata(10000, [])


def test_saldo_satu_pengeluaran():
    anggota = ["Ani", "Budi"]
    pengeluaran = [buat_pengeluaran("Ani", 50000, anggota)]
    assert hitung_saldo(anggota, pengeluaran) == {"Ani": 25000, "Budi": -25000}


def test_saldo_menolak_nama_asing():
    pengeluaran = [buat_pengeluaran("Zaki", 50000, ["Ani"])]
    with pytest.raises(ValueError):
        hitung_saldo(["Ani"], pengeluaran)


def test_pelunasan_beberapa_orang():
    saldo = {"Ani": 30000, "Budi": -10000, "Citra": -20000}
    assert hitung_pelunasan(saldo) == [
        ("Citra", "Ani", 20000),
        ("Budi", "Ani", 10000),
    ]


def test_pelunasan_kosong_jika_sudah_impas():
    assert hitung_pelunasan({"Ani": 0, "Budi": 0}) == []
