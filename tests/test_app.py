"""Menguji halaman web tanpa perlu membuka browser."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from patungan.penyimpanan import muat_data, simpan_data

LOKASI_APP = Path(__file__).parent.parent / "app.py"


@pytest.fixture
def lokasi_data(tmp_path, monkeypatch):
    lokasi = tmp_path / "data.json"
    monkeypatch.setenv("PATUNGAN_DATA", str(lokasi))
    return lokasi


def jalankan_app():
    # Batas waktunya longgar supaya tes tetap lolos di laptop yang lebih lambat.
    app = AppTest.from_file(str(LOKASI_APP), default_timeout=30)
    app.run()
    assert not app.exception
    return app


def test_app_kosong_bisa_dibuka(lokasi_data):
    app = jalankan_app()
    assert app.metric[0].value == "Rp0"
    assert app.metric[1].value == "0"


def test_tambah_anggota_lewat_form_tersimpan(lokasi_data):
    app = jalankan_app()

    app.text_input[0].set_value("Ani")
    app.button[0].click().run()

    assert not app.exception
    assert not app.error
    assert muat_data(lokasi_data)["anggota"] == ["Ani"]
    assert app.metric[1].value == "1"


def test_pelunasan_ditampilkan(lokasi_data):
    simpan_data(
        lokasi_data,
        {
            "anggota": ["Ani", "Budi"],
            "pengeluaran": [
                {
                    "keterangan": "Makan",
                    "pembayar": "Ani",
                    "jumlah": 50000,
                    "peserta": ["Ani", "Budi"],
                }
            ],
        },
    )

    app = jalankan_app()

    assert app.metric[0].value == "Rp50.000"
    assert app.code[0].value == "Budi bayar ke Ani: Rp25.000"
