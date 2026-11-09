from patungan.tampilan import (
    baris_pelunasan,
    baris_saldo,
    format_rupiah,
    teks_pelunasan,
)


def test_format_rupiah():
    assert format_rupiah(1250000) == "Rp1.250.000"


def test_baris_saldo_memberi_status():
    assert baris_saldo({"Ani": 5000, "Budi": -5000, "Citra": 0}) == [
        {"Anggota": "Ani", "Status": "Harus nerima", "Jumlah": "Rp5.000"},
        {"Anggota": "Budi", "Status": "Harus bayar", "Jumlah": "Rp5.000"},
        {"Anggota": "Citra", "Status": "Udah impas", "Jumlah": "Rp0"},
    ]


def test_baris_pelunasan():
    assert baris_pelunasan([("Budi", "Ani", 5000)]) == [
        {"Dari": "Budi", "Ke": "Ani", "Jumlah": "Rp5.000"}
    ]


def test_teks_pelunasan_satu_baris_per_transfer():
    pelunasan = [("Citra", "Ani", 15000), ("Budi", "Ani", 5000)]
    assert teks_pelunasan(pelunasan) == (
        "Citra bayar ke Ani: Rp15.000\nBudi bayar ke Ani: Rp5.000"
    )
