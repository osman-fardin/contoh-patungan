"""Halaman web aplikasi Patungan. Jalankan dengan: streamlit run app.py"""

import os
from pathlib import Path

import streamlit as st

from patungan import hitung, kelola, penyimpanan, tampilan

LOKASI_BAWAAN = Path(__file__).parent / "data" / "patungan.json"
LOKASI_DATA = Path(os.environ.get("PATUNGAN_DATA", LOKASI_BAWAAN))


def terapkan(data, aksi, *argumen):
    """Menjalankan perubahan data, menyimpannya, lalu memuat ulang halaman."""
    try:
        aksi(data, *argumen)
    except ValueError as galat:
        st.error(str(galat))
        return

    penyimpanan.simpan_data(LOKASI_DATA, data)
    st.rerun()


def tampilkan_ringkasan(data, pelunasan):
    total = sum(item["jumlah"] for item in data["pengeluaran"])

    kolom_total, kolom_anggota, kolom_transfer = st.columns(3)
    kolom_total.metric("Total pengeluaran", tampilan.format_rupiah(total))
    kolom_anggota.metric("Anggota", len(data["anggota"]))
    kolom_transfer.metric("Transfer yang perlu", len(pelunasan))


def tampilkan_tab_anggota(data):
    with st.form("form_anggota", clear_on_submit=True):
        nama = st.text_input("Nama anggota", placeholder="Contoh: Ani")
        if st.form_submit_button("Tambah anggota"):
            terapkan(data, kelola.tambah_anggota, nama)

    if not data["anggota"]:
        st.info("Belum ada anggota. Tambahin dulu di atas ya.")

    for nama in data["anggota"]:
        kolom_nama, kolom_hapus = st.columns([5, 1])
        kolom_nama.write(nama)
        if kolom_hapus.button("Hapus", key=f"hapus_anggota_{nama}"):
            terapkan(data, kelola.hapus_anggota, nama)


def tampilkan_form_pengeluaran(data):
    anggota = data["anggota"]

    with st.form("form_pengeluaran", clear_on_submit=True):
        keterangan = st.text_input("Buat apa?", placeholder="Contoh: Makan siang")
        pembayar = st.selectbox("Siapa yang nalangin?", anggota)
        jumlah = st.number_input(
            "Jumlah (rupiah)", min_value=1, value=10000, step=1000
        )
        peserta = st.multiselect("Dibagi ke siapa aja?", anggota, default=anggota)

        if st.form_submit_button("Catat pengeluaran"):
            terapkan(
                data,
                kelola.tambah_pengeluaran,
                keterangan,
                pembayar,
                int(jumlah),
                peserta,
            )


def tampilkan_tab_pengeluaran(data):
    if not data["anggota"]:
        st.info("Tambahin anggota dulu di tab Anggota ya.")
        return

    tampilkan_form_pengeluaran(data)

    for indeks, item in enumerate(data["pengeluaran"]):
        kolom_info, kolom_hapus = st.columns([5, 1])
        kolom_info.markdown(tampilan.teks_pengeluaran(item))
        if kolom_hapus.button("Hapus", key=f"hapus_pengeluaran_{indeks}"):
            terapkan(data, kelola.hapus_pengeluaran, indeks)


def tampilkan_tab_pelunasan(saldo, pelunasan):
    if not saldo:
        st.info("Belum ada data buat dihitung.")
        return

    st.subheader("Saldo tiap orang")
    st.dataframe(tampilan.baris_saldo(saldo), hide_index=True)

    st.subheader("Siapa bayar ke siapa")
    if not pelunasan:
        st.success("Semua udah impas!")
        return

    st.dataframe(tampilan.baris_pelunasan(pelunasan), hide_index=True)
    st.caption("Tinggal copy terus kirim ke grup:")
    st.code(tampilan.teks_pelunasan(pelunasan), language=None)


def main():
    st.set_page_config(page_title="Patungan", page_icon="💸")
    st.title("Patungan")
    st.caption("Catat pengeluaran bareng, biar tau siapa harus bayar ke siapa.")

    try:
        data = penyimpanan.muat_data(LOKASI_DATA)
    except ValueError as galat:
        st.error(str(galat))
        st.stop()

    saldo = hitung.hitung_saldo(data["anggota"], data["pengeluaran"])
    pelunasan = hitung.hitung_pelunasan(saldo)

    tampilkan_ringkasan(data, pelunasan)

    tab_anggota, tab_pengeluaran, tab_pelunasan = st.tabs(
        ["Anggota", "Pengeluaran", "Siapa Bayar"]
    )
    with tab_anggota:
        tampilkan_tab_anggota(data)
    with tab_pengeluaran:
        tampilkan_tab_pengeluaran(data)
    with tab_pelunasan:
        tampilkan_tab_pelunasan(saldo, pelunasan)


main()
