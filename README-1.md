# Tugas Python: Fungsi Dasar

Project latihan Python untuk siswa SMK RPL yang berisi tiga fungsi sederhana: menghitung persegi panjang, memformat angka ala Indonesia, dan mengecek stok barang.

## Daftar File

| File | Keterangan |
|------|------------|
| `persegi_panjang.py` | Fungsi luas dan keliling persegi panjang |
| `format_angka.py` | Fungsi format angka dengan titik pemisah ribuan |
| `cek_stok.py` | Fungsi `cek_stok(stok, jumlah)` |
| `main.py` | Program untuk mencoba ketiga fungsi |
| `README.md` | Dokumentasi project |

## Cara Menjalankan

1. Pastikan Python 3 sudah terpasang (cek dengan `python --version`).
2. Buka terminal di folder project ini.
3. Jalankan:

```bash
python main.py
```

Tidak perlu menginstal library tambahan.

## Contoh Output

```
========================================
TUGAS 1: PERSEGI PANJANG
========================================
Panjang  : 10
Lebar    : 5
Luas     : 10 x 5 = 50
Keliling : 2 x (10 + 5) = 30

Panjang  : 8
Lebar    : 3
Luas     : 8 x 3 = 24
Keliling : 2 x (8 + 3) = 22

========================================
TUGAS 2: FORMAT ANGKA
========================================
125000 menjadi 125.000
1000000 menjadi 1.000.000
500 menjadi 500
7500 menjadi 7.500

========================================
TUGAS 3: CEK STOK
========================================
cek_stok(10, 5) = True
cek_stok(3, 5) = False
cek_stok(5, 5) = True
cek_stok(0, 1) = False
```
