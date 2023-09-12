# Inisialisasi jumlah bakteri awal
jumlah_bakteri_hidup = 100

# Durasi dalam jam
waktu = 500

# Durasi hidup bakteri dalam jam (satu hari)
durasi_hidup = 24

# Hitung berapa kali bakteri hidup dalam 500 jam
reproduksi_periode = waktu // durasi_hidup

# Hitung jumlah bakteri yang masih hidup setelah 500 jam
jumlah_bakteri_hidup_setelah_500_jam = jumlah_bakteri_hidup ** reproduksi_periode

# Cetak hasilnya
print("Jumlah bakteri yang masih hidup setelah 500 jam:", jumlah_bakteri_hidup_setelah_500_jam)
