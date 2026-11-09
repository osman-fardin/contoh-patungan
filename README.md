# Patungan

Aplikasi terminal buat nyatet pengeluaran bareng dan ngitung siapa harus bayar ke siapa.

> Repo ini **contoh** buat Proyek Kelompok DDP1. Boleh banget niru susunan repo-nya, tapi masalah dan solusinya cari sendiri ya.

## Masalahnya

Pas makan atau liburan bareng, biasanya satu orang nalangin dulu. Lama-lama utangnya numpuk dan ribet kalau dihitung manual.

## Solusinya

Patungan nyatet tiap pengeluaran, ngebaginya ke orang yang ikut, terus bikin daftar siapa bayar ke siapa.

## Fiturnya

- Nambah anggota
- Nyatet pengeluaran, termasuk yang cuma dibagi ke sebagian anggota
- Nampilin daftar pengeluaran
- Ngitung siapa harus bayar ke siapa
- Nyimpen data otomatis ke file JSON

## Cara jalaninnya

Butuh Python 3.10 ke atas.

```bash
git clone <link-repo>
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
python main.py
```

## Jalanin tes

```bash
python -m pytest
```

## Isi foldernya

```text
contoh-patungan/
├── main.py              Menu dan input
├── patungan/
│   ├── hitung.py        Perhitungan
│   ├── penyimpanan.py   Baca dan tulis JSON
│   └── tampilan.py      Tabel di terminal
├── tests/               Tes otomatis
├── docs/arsitektur.md   Penjelasan arsitektur
├── requirements.txt     Daftar library
└── .gitignore           File yang nggak dikirim ke GitHub
```

Penjelasan lengkapnya ada di [docs/arsitektur.md](docs/arsitektur.md).

## Hal baru di luar materi kelas

- [Rich](https://rich.readthedocs.io/) buat bikin tabel di terminal
- [pytest](https://docs.pytest.org/) buat tes otomatis
- JSON buat nyimpen data

## Pembagian tugas

Kalau di proyek beneran, isi tabel ini pakai anggota kelompokmu.

| Anggota | Tugas |
| --- | --- |
| Anggota A | Menu utama (`main.py`) |
| Anggota B | Perhitungan (`hitung.py`) dan tesnya |
| Anggota C | Penyimpanan (`penyimpanan.py`) dan tesnya |
| Anggota D | Tampilan (`tampilan.py`), README, dan video |
