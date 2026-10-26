
from perangkat import SensorSuhu, SensorDebit

# Membuat objek sensor
suhu = SensorSuhu("Suhu")
debit = SensorDebit("Debit", "L/menit")

# Mengisi data sensor suhu
suhu.baca(30.1)
suhu.baca(30.6)
suhu.baca(30.3)

# Mengisi data sensor debit
debit.baca(12.0)
debit.baca(15.0)
debit.baca(15.0)

# Memasukkan kedua sensor ke dalam satu list
sensor_list = [suhu, debit]

# Memproses semua sensor dengan satu perulangan
for p in sensor_list:
    print(f"{p.nama} -> {p.proses()}")
