import pytest

from patungan.penyimpanan import data_kosong, muat_data, simpan_data


def test_file_belum_ada_menghasilkan_data_kosong(tmp_path):
    assert muat_data(tmp_path / "tidak-ada.json") == data_kosong()


def test_data_tersimpan_bisa_dibaca_lagi(tmp_path):
    lokasi = tmp_path / "folder-baru" / "data.json"
    data = {"anggota": ["Ani"], "pengeluaran": []}

    simpan_data(lokasi, data)

    assert muat_data(lokasi) == data


def test_file_rusak_ditolak(tmp_path):
    lokasi = tmp_path / "rusak.json"
    lokasi.write_text("bukan json", encoding="utf-8")

    with pytest.raises(ValueError):
        muat_data(lokasi)
