
class Perangkat:
    def __init__(self, nama):
        self.nama = nama
        self.data = []

    def baca(self, nilai):
        self.data.append(nilai)

    def proses(self):
        raise NotImplementedError(
            "Metode proses() harus diterapkan oleh kelas turunan"
        )


class SensorSuhu(Perangkat):
    def proses(self):
        if not self.data:
            raise ValueError("Data suhu masih kosong")

        return max(self.data)


class SensorDebit(Perangkat):
    def __init__(self, nama, satuan):
        super().__init__(nama)
        self.satuan = satuan

    def proses(self):
        if not self.data:
            raise ValueError("Data debit masih kosong")

        return sum(self.data) / len(self.data)
