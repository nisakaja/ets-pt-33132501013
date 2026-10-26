# Definisi fungsi rentang
def rentang(data):
    if not data:
        return (0, 0)
    # Mengembalikan tuple (nilai terkecil, nilai terbesar)
    return (min(data), max(data))

# Definisi fungsi ringkasan
def ringkasan(data):
    if not data:
        return {"jumlah": 0, "min": 0, "maks": 0, "rata": 0.0}
    
    total = sum(data)
    jml_data = len(data)
    
    # Mengembalikan dictionary dengan kunci: jumlah, min, maks, dan rata
    return {
        "jumlah": jml_data,
        "min": min(data),
        "maks": max(data),
        "rata": total / jml_data
    }
