class Rekening:
    def __init__(self, saldo_awal, limit):
        self.saldo = saldo_awal
        self.limit = limit

    def debit(self, jumlah):
        if jumlah > self.saldo or jumlah > self.limit:
            print("Transaksi gagal. Jumlah penarikan melebihi saldo atau limit.")
        else:
            self.saldo -= jumlah
            print(f"Saldo berhasil dikurangi sebesar {jumlah}. Saldo sekarang: {self.saldo}")

    def kredit(self, jumlah):
        if self.saldo + jumlah > self.limit * 4:
            print("Transaksi gagal. Jumlah penyetoran melebihi batas maksimal anda.")
        else:
            self.saldo += jumlah
            print(f"Saldo berhasil ditambah sebesar {jumlah}. Saldo anda sekarang: {self.saldo}")

    def getSaldo(self):
        print(f"Saldo saat ini: {self.saldo}")


rekening = Rekening(1000, 2000)


rekening.debit(200)
rekening.kredit(300)
rekening.debit(2000)
rekening.kredit(3000)
rekening.getSaldo()