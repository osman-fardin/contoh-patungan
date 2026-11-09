"""Menyimpan dan membaca data patungan dari file JSON."""

import json


def data_kosong():
    """Membuat struktur data awal."""
    return {"anggota": [], "pengeluaran": []}


def muat_data(lokasi):
    """Membaca data dari file. Mengembalikan data kosong jika file belum ada."""
    if not lokasi.exists():
        return data_kosong()

    try:
        with lokasi.open(encoding="utf-8") as berkas:
            return json.load(berkas)
    except json.JSONDecodeError as galat:
        raise ValueError(f"File data {lokasi} rusak.") from galat


def simpan_data(lokasi, data):
    """Menulis data ke file dan membuat foldernya jika belum ada."""
    lokasi.parent.mkdir(parents=True, exist_ok=True)
    with lokasi.open("w", encoding="utf-8") as berkas:
        json.dump(data, berkas, ensure_ascii=False, indent=2)
