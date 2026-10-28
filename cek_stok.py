"""Tugas 3: Fungsi Cek Stok."""


def cek_stok(stok, jumlah):
    """Mengembalikan True jika stok mencukupi, False jika tidak.

    Jika jumlah yang diminta sama dengan stok, hasilnya tetap True.
    """
    return stok >= jumlah
