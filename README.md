# Patungan

Web app buat nyatet pengeluaran bareng dan ngitung siapa harus bayar ke siapa. Dibikin pakai Python dan Streamlit.

> Repo ini **contoh** buat Proyek Kelompok DDP1. Boleh banget niru susunan repo-nya, tapi masalah dan solusinya cari sendiri ya.

## Masalahnya

Pas makan atau liburan bareng, biasanya satu orang nalangin dulu. Lama-lama utangnya numpuk dan ribet kalau dihitung manual.

## Solusinya

Patungan nyatet tiap pengeluaran, ngebaginya ke orang yang ikut, terus bikin daftar siapa bayar ke siapa yang tinggal dikirim ke grup.

## Fiturnya

- Nambah dan ngehapus anggota
- Nyatet pengeluaran, termasuk yang cuma dibagi ke sebagian anggota
- Ringkasan total pengeluaran dan jumlah transfer
- Saldo tiap orang
- Daftar siapa bayar ke siapa yang bisa langsung di-copy
- Nyimpen data otomatis ke file JSON

## Tech stack

| Teknologi | Dipakai buat |
| --- | --- |
| Python | Bahasa utama |
| [Streamlit](https://streamlit.io/) | Halaman web |
| [pytest](https://docs.pytest.org/) | Tes otomatis |
| JSON | Nyimpen data |

## Cara jalaninnya

Butuh Python 3.10 ke atas.

```bash
git clone https://github.com/osman-fardin/contoh-patungan.git
cd contoh-patungan
python -m venv .venv
```

Aktifin lingkungan virtualnya:

```bash
# Windows (Git Bash)
source .venv/Scripts/activate

# macOS dan Linux
source .venv/bin/activate
```

Install library-nya, terus jalanin:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Nanti app-nya kebuka di browser, biasanya di `http://localhost:8501`.

## Jalanin tes

```bash
python -m pytest
```

## Isi foldernya

```text
contoh-patungan/
├── app.py               Halaman web
├── patungan/
│   ├── kelola.py        Aturan ubah data
│   ├── hitung.py        Perhitungan
│   ├── penyimpanan.py   Baca dan tulis JSON
│   └── tampilan.py      Format teks dan tabel
├── tests/               Tes otomatis
├── docs/arsitektur.md   Penjelasan arsitektur
├── requirements.txt     Daftar library
└── .gitignore           File yang nggak dikirim ke GitHub
```

Penjelasan lengkapnya ada di [docs/arsitektur.md](docs/arsitektur.md).

## Hal baru di luar materi kelas

- Bikin web app pakai Streamlit
- Tes otomatis pakai pytest
- Nyimpen data pakai JSON

## Pembagian tugas

Kalau di proyek beneran, isi tabel ini pakai anggota kelompokmu.

| Anggota | Tugas |
| --- | --- |
| Anggota A | Halaman web (`app.py`) dan tesnya |
| Anggota B | Aturan data dan perhitungan (`kelola.py`, `hitung.py`) dan tesnya |
| Anggota C | Penyimpanan dan tampilan (`penyimpanan.py`, `tampilan.py`), README, dan video |
