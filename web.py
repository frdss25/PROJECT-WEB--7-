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

# Fungsi untuk melihat semua pengeluaran
def lihat_pengeluaran(pengeluaran_list):
    if not pengeluaran_list:
        print("Belum ada pengeluaran yang dicatat.")
        return
    
    print("\nDaftar Pengeluaran:")
    for i, pengeluaran in enumerate(pengeluaran_list, start=1):
        print(f"{i}. {pengeluaran['tanggal']} - {pengeluaran['deskripsi']} - Rp{pengeluaran['nominal']:.2f}")

# Fungsi untuk menghitung total pengeluaran
def total_pengeluaran(pengeluaran_list):
    total = sum(item["nominal"] for item in pengeluaran_list)
    print(f"\nTotal pengeluaran Anda adalah: Rp{total:.2f}")

# Program utama
if __name__ == "__main__":
    pengeluaran_list = []
    while True:
        print("\n=== Menu Pencatatan Pengeluaran ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Total Pengeluaran")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_pengeluaran(pengeluaran_list)
        elif pilihan == "2":
            lihat_pengeluaran(pengeluaran_list)
        elif pilihan == "3":
            total_pengeluaran(pengeluaran_list)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
