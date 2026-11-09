"""Titik masuk aplikasi Patungan."""

from pathlib import Path

from patungan import hitung, penyimpanan, tampilan

LOKASI_DATA = Path("data/patungan.json")

MENU = """
=== PATUNGAN ===
1. Tambah anggota
2. Catat pengeluaran
3. Lihat pengeluaran
4. Lihat siapa bayar ke siapa
0. Keluar
"""


def tambah_anggota(data):
    nama = input("Nama anggota: ").strip()
    if not nama:
        print("Nama tidak boleh kosong.")
    elif nama in data["anggota"]:
        print(f"{nama} sudah terdaftar.")
    else:
        data["anggota"].append(nama)
        print(f"{nama} ditambahkan.")


def minta_jumlah():
    """Meminta jumlah uang sampai input berupa bilangan bulat positif."""
    while True:
        teks = input("Jumlah (rupiah): ").strip().replace(".", "")
        if teks.isdigit() and int(teks) > 0:
            return int(teks)
        print("Masukkan angka lebih dari 0, contoh: 25000")


def minta_peserta(anggota):
    """Meminta peserta. Input kosong berarti semua anggota ikut."""
    while True:
        teks = input("Dibagi ke (pisahkan koma, kosong = semua): ").strip()
        if not teks:
            return list(anggota)

        peserta = [nama.strip() for nama in teks.split(",") if nama.strip()]
        asing = [nama for nama in peserta if nama not in anggota]
        if peserta and not asing:
            return peserta
        print(f"Nama tidak dikenal: {', '.join(asing) or '(kosong)'}")


def catat_pengeluaran(data):
    anggota = data["anggota"]
    if not anggota:
        print("Tambahkan anggota dulu.")
        return

    keterangan = input("Keterangan: ").strip() or "Tanpa keterangan"
    pembayar = input("Dibayar oleh: ").strip()
    if pembayar not in anggota:
        print(f"{pembayar} belum terdaftar.")
        return

    data["pengeluaran"].append(
        {
            "keterangan": keterangan,
            "pembayar": pembayar,
            "jumlah": minta_jumlah(),
            "peserta": minta_peserta(anggota),
        }
    )
    print("Pengeluaran dicatat.")


def lihat_pelunasan(data):
    saldo = hitung.hitung_saldo(data["anggota"], data["pengeluaran"])
    tampilan.tampilkan_pelunasan(hitung.hitung_pelunasan(saldo))


def main():
    try:
        data = penyimpanan.muat_data(LOKASI_DATA)
    except ValueError as galat:
        print(galat)
        return

    while True:
        print(MENU)
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_anggota(data)
        elif pilihan == "2":
            catat_pengeluaran(data)
        elif pilihan == "3":
            tampilan.tampilkan_pengeluaran(data["pengeluaran"])
        elif pilihan == "4":
            lihat_pelunasan(data)
        elif pilihan == "0":
            print("Sampai jumpa!")
            return
        else:
            print("Menu tidak tersedia.")

        penyimpanan.simpan_data(LOKASI_DATA, data)


if __name__ == "__main__":
    main()
