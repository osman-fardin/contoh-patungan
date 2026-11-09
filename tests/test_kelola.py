import pytest

from patungan.kelola import (
    hapus_anggota,
    hapus_pengeluaran,
    tambah_anggota,
    tambah_pengeluaran,
)


def buat_data():
    return {"anggota": ["Ani", "Budi"], "pengeluaran": []}


def test_tambah_anggota_merapikan_nama():
    data = buat_data()
    tambah_anggota(data, "  Citra ")
    assert data["anggota"] == ["Ani", "Budi", "Citra"]


@pytest.mark.parametrize("nama", ["", "   ", "ani"])
def test_tambah_anggota_menolak_nama_kosong_atau_kembar(nama):
    with pytest.raises(ValueError):
        tambah_anggota(buat_data(), nama)


def test_tambah_pengeluaran_tersimpan():
    data = buat_data()
    tambah_pengeluaran(data, "Makan", "Ani", 20000, ["Ani", "Budi"])
    assert data["pengeluaran"] == [
        {
            "keterangan": "Makan",
            "pembayar": "Ani",
            "jumlah": 20000,
            "peserta": ["Ani", "Budi"],
        }
    ]


@pytest.mark.parametrize(
    "pembayar, jumlah, peserta",
    [("Ani", 0, ["Ani"]), ("Ani", 1000, []), ("Zaki", 1000, ["Ani"])],
)
def test_tambah_pengeluaran_menolak_input_salah(pembayar, jumlah, peserta):
    with pytest.raises(ValueError):
        tambah_pengeluaran(buat_data(), "Makan", pembayar, jumlah, peserta)


def test_anggota_yang_dipakai_tidak_bisa_dihapus():
    data = buat_data()
    tambah_pengeluaran(data, "Makan", "Ani", 20000, ["Budi"])
    with pytest.raises(ValueError):
        hapus_anggota(data, "Budi")


def test_hapus_pengeluaran_membuka_hapus_anggota():
    data = buat_data()
    tambah_pengeluaran(data, "Makan", "Ani", 20000, ["Ani"])

    hapus_pengeluaran(data, 0)
    hapus_anggota(data, "Ani")

    assert data == {"anggota": ["Budi"], "pengeluaran": []}
