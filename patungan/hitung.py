"""Logika perhitungan patungan.

Modul ini tidak membaca input dan tidak mencetak apa pun,
sehingga mudah diuji. Semua jumlah uang memakai bilangan bulat rupiah.
"""


def bagi_rata(jumlah, peserta):
    """Membagi jumlah ke semua peserta tanpa ada rupiah yang hilang.

    Sisa pembagian diberikan satu rupiah per orang, mulai dari peserta pertama.
    """
    if not peserta:
        raise ValueError("Peserta tidak boleh kosong.")

    bagian, sisa = divmod(jumlah, len(peserta))
    hasil = {}
    for urutan, nama in enumerate(peserta):
        hasil[nama] = bagian + (1 if urutan < sisa else 0)
    return hasil


def hitung_saldo(anggota, daftar_pengeluaran):
    """Menghitung saldo setiap anggota.

    Saldo positif berarti anggota harus menerima uang.
    Saldo negatif berarti anggota harus membayar.
    """
    saldo = {nama: 0 for nama in anggota}

    for pengeluaran in daftar_pengeluaran:
        pembayar = pengeluaran["pembayar"]
        peserta = pengeluaran["peserta"]

        for nama in [pembayar, *peserta]:
            if nama not in saldo:
                raise ValueError(f"{nama} belum terdaftar sebagai anggota.")

        saldo[pembayar] += pengeluaran["jumlah"]
        for nama, bagian in bagi_rata(pengeluaran["jumlah"], peserta).items():
            saldo[nama] -= bagian

    return saldo


def hitung_pelunasan(saldo):
    """Mengubah saldo menjadi daftar pembayaran (dari, ke, jumlah)."""
    penerima = sorted(
        ([nama, nilai] for nama, nilai in saldo.items() if nilai > 0),
        key=lambda data: (-data[1], data[0]),
    )
    pembayar = sorted(
        ([nama, -nilai] for nama, nilai in saldo.items() if nilai < 0),
        key=lambda data: (-data[1], data[0]),
    )

    pelunasan = []
    i = 0
    j = 0
    while i < len(pembayar) and j < len(penerima):
        jumlah = min(pembayar[i][1], penerima[j][1])
        pelunasan.append((pembayar[i][0], penerima[j][0], jumlah))

        pembayar[i][1] -= jumlah
        penerima[j][1] -= jumlah
        if pembayar[i][1] == 0:
            i += 1
        if penerima[j][1] == 0:
            j += 1

    return pelunasan
