
# Data debit untuk pengujian
# Data debit untuk pengujian
data_debit = [10, 20, 30, 40, 50]


def hitung_rata_rata(data):
    """Menghitung rata-rata data debit."""
    if len(data) == 0:
        return 0

    total = sum(data)
    rata_rata = total / len(data)
    return rata_rata


def cari_terendah(data):
    """Mencari nilai debit paling rendah."""
    if len(data) == 0:
        return None

    terendah = min(data)
    return terendah


def cek_status(debit):
    """Memeriksa status berdasarkan nilai debit."""
    if debit < 10:
        return "Rendah"
    elif debit <= 20:
        return "Normal"
    else:
        return "Tinggi"


# Menampilkan hasil pengolahan data
print("Data debit:", data_debit)
print("Rata-rata debit:", hitung_rata_rata(data_debit))
print("Debit terendah:", cari_terendah(data_debit))
