# Import modul
import datetime

# Fungsi untuk menambahkan pengeluaran
def tambah_pengeluaran(pengeluaran_list):
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    deskripsi = input("Masukkan deskripsi pengeluaran: ")
    nominal = float(input("Masukkan nominal pengeluaran: "))
    
    pengeluaran = {
        "tanggal": tanggal,
        "deskripsi": deskripsi,
        "nominal": nominal
    }
    pengeluaran_list.append(pengeluaran)
    print("Pengeluaran berhasil ditambahkan!")