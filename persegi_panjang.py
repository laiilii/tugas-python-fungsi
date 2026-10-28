"""Tugas 1: Fungsi Persegi Panjang."""


def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang: panjang x lebar."""
    return panjang * lebar


def hitung_keliling(panjang, lebar):
    """Menghitung keliling persegi panjang: 2 x (panjang + lebar)."""
    return 2 * (panjang + lebar)


def tampilkan_hasil(panjang, lebar):
    """Menampilkan hasil perhitungan luas dan keliling dengan jelas."""
    luas = hitung_luas(panjang, lebar)
    keliling = hitung_keliling(panjang, lebar)

    print(f"Panjang  : {panjang}")
    print(f"Lebar    : {lebar}")
    print(f"Luas     : {panjang} x {lebar} = {luas}")
    print(f"Keliling : 2 x ({panjang} + {lebar}) = {keliling}")
