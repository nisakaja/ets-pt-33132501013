
from debit import hitung_rata_rata, cari_terendah, cek_status

# Uji 1: Menghitung rata-rata
print("Hasil hitung rata-rata:", hitung_rata_rata([10, 20, 30]))

# Uji 2: Mencari nilai terendah
print("Hasil cari terendah:", cari_terendah([12.5, 14.0, 11.0]))

# Uji 3-6: Memeriksa status debit berdasarkan input
nilai_debit = float(input("Masukkan nilai debit: "))
print("Hasil cek status:", cek_status(nilai_debit))
