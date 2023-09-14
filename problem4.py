# Inisialisasi jumlah bakteri awal
jumlah_bakteri = 100

# Durasi dalam jam dalam sehari
waktu_sehari = 24

# Waktu reproduksi satu bakteri (dalam jam)
waktu_reproduksi = 20 / 60  # Ubah waktu reproduksi menjadi jam (20 menit)

# Hitung berapa kali reproduksi terjadi dalam sehari
reproduksi_per_hari = waktu_sehari // waktu_reproduksi

# Hitung jumlah bakteri setelah satu hari
jumlah_bakteri_setelah_satu_hari = jumlah_bakteri * (2 ** reproduksi_per_hari)

# Cetak hasilnya
print("Jumlah bakteri setelah satu hari:", jumlah_bakteri_setelah_satu_hari)
