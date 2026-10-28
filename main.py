"""Program utama untuk mencoba ketiga fungsi."""

from persegi_panjang import tampilkan_hasil
from format_angka import format_angka
from cek_stok import cek_stok


def garis(judul):
    """Mencetak judul bagian agar output rapi."""
    print()
    print("=" * 40)
    print(judul)
    print("=" * 40)


# ---------- Tugas 1: Persegi Panjang ----------
garis("TUGAS 1: PERSEGI PANJANG")
tampilkan_hasil(10, 5)
print()
tampilkan_hasil(8, 3)

# ---------- Tugas 2: Format Angka ----------
garis("TUGAS 2: FORMAT ANGKA")
for angka in [125000, 1000000, 500, 7500]:
    print(f"{angka} menjadi {format_angka(angka)}")

# ---------- Tugas 3: Cek Stok ----------
garis("TUGAS 3: CEK STOK")
# Setiap data berisi (stok, jumlah yang diminta)
data_uji = [(10, 5), (3, 5), (5, 5), (0, 1)]
for stok, jumlah in data_uji:
    print(f"cek_stok({stok}, {jumlah}) = {cek_stok(stok, jumlah)}")
