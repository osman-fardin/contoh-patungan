"""Mengubah data menjadi teks dan baris tabel yang siap ditampilkan."""


def format_rupiah(jumlah):
    """Mengubah 25000 menjadi Rp25.000."""
    return f"Rp{jumlah:,}".replace(",", ".")


def teks_pengeluaran(item):
    """Membuat satu baris ringkasan pengeluaran."""
    jumlah = format_rupiah(item["jumlah"])
    peserta = ", ".join(item["peserta"])
    return (
        f"**{item['keterangan']}** · {jumlah}  \n"
        f"Ditalangin {item['pembayar']}, dibagi ke {peserta}"
    )


def baris_saldo(saldo):
    """Membuat baris tabel saldo setiap anggota."""
    baris = []
    for nama, nilai in saldo.items():
        if nilai > 0:
            status = "Harus nerima"
        elif nilai < 0:
            status = "Harus bayar"
        else:
            status = "Udah impas"
        baris.append(
            {"Anggota": nama, "Status": status, "Jumlah": format_rupiah(abs(nilai))}
        )
    return baris


def baris_pelunasan(pelunasan):
    """Membuat baris tabel siapa bayar ke siapa."""
    return [
        {"Dari": dari, "Ke": ke, "Jumlah": format_rupiah(jumlah)}
        for dari, ke, jumlah in pelunasan
    ]


def teks_pelunasan(pelunasan):
    """Membuat ringkasan yang siap dikirim ke grup chat."""
    return "\n".join(
        f"{dari} bayar ke {ke}: {format_rupiah(jumlah)}"
        for dari, ke, jumlah in pelunasan
    )
