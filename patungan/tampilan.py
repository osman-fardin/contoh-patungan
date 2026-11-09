"""Menampilkan data ke terminal dengan library Rich."""

from rich.console import Console
from rich.table import Table

konsol = Console()


def format_rupiah(jumlah):
    """Mengubah 25000 menjadi Rp25.000."""
    return f"Rp{jumlah:,}".replace(",", ".")


def tampilkan_pengeluaran(daftar_pengeluaran):
    """Menampilkan semua pengeluaran dalam bentuk tabel."""
    if not daftar_pengeluaran:
        konsol.print("[yellow]Belum ada pengeluaran.[/yellow]")
        return

    tabel = Table(title="Daftar Pengeluaran")
    tabel.add_column("Keterangan")
    tabel.add_column("Dibayar oleh")
    tabel.add_column("Jumlah", justify="right")
    tabel.add_column("Dibagi ke")

    for item in daftar_pengeluaran:
        tabel.add_row(
            item["keterangan"],
            item["pembayar"],
            format_rupiah(item["jumlah"]),
            ", ".join(item["peserta"]),
        )
    konsol.print(tabel)


def tampilkan_pelunasan(pelunasan):
    """Menampilkan siapa harus membayar kepada siapa."""
    if not pelunasan:
        konsol.print("[green]Semua sudah lunas.[/green]")
        return

    tabel = Table(title="Siapa Bayar ke Siapa")
    tabel.add_column("Dari")
    tabel.add_column("Ke")
    tabel.add_column("Jumlah", justify="right")

    for dari, ke, jumlah in pelunasan:
        tabel.add_row(dari, ke, format_rupiah(jumlah))
    konsol.print(tabel)
