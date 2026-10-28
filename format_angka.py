"""Tugas 2: Fungsi Format Angka (format Indonesia)."""


def format_angka(angka):
    """Mengubah bilangan bulat positif menjadi format ribuan Indonesia.

    Contoh: 125000 -> "125.000"
    """
    # Pastikan angka berupa bilangan bulat positif
    if not isinstance(angka, int) or isinstance(angka, bool) or angka < 0:
        return "Input harus bilangan bulat positif"

    # Format dengan koma (125,000), lalu ganti koma menjadi titik
    return f"{angka:,}".replace(",", ".")
