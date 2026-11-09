"""Aturan untuk mengubah data anggota dan pengeluaran.

Setiap fungsi mengubah data, atau memunculkan ValueError jika inputnya salah.
"""


def tambah_anggota(data, nama):
    nama = nama.strip()
    if not nama:
        raise ValueError("Nama nggak boleh kosong.")

    nama_terdaftar = [anggota.lower() for anggota in data["anggota"]]
    if nama.lower() in nama_terdaftar:
        raise ValueError(f"{nama} udah terdaftar.")

    data["anggota"].append(nama)


def hapus_anggota(data, nama):
    for item in data["pengeluaran"]:
        if nama == item["pembayar"] or nama in item["peserta"]:
            raise ValueError(f"{nama} masih ada di catatan pengeluaran.")

    data["anggota"].remove(nama)


def tambah_pengeluaran(data, keterangan, pembayar, jumlah, peserta):
    if jumlah <= 0:
        raise ValueError("Jumlah harus lebih dari 0.")
    if not peserta:
        raise ValueError("Pilih minimal satu orang.")

    for nama in [pembayar, *peserta]:
        if nama not in data["anggota"]:
            raise ValueError(f"{nama} belum terdaftar.")

    data["pengeluaran"].append(
        {
            "keterangan": keterangan.strip() or "Tanpa keterangan",
            "pembayar": pembayar,
            "jumlah": jumlah,
            "peserta": list(peserta),
        }
    )


def hapus_pengeluaran(data, indeks):
    del data["pengeluaran"][indeks]
