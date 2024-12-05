def tampilkan_menu():
    print("\n=== DAFTAR BARANG ===")
    for kode, item in barang.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']:,}")

def hitung_total(pesanan):
    total = 0
    print("\n=== DETAIL PEMBELIAN ===")
    for kode, jumlah in pesanan.items():
        nama_barang = barang[kode]['nama']
        harga = barang[kode]['harga']
        subtotal = harga * jumlah
        total += subtotal
        print(f"{nama_barang} x {jumlah} = Rp{subtotal:,}")
    return total

# Data barang (simulasi database)
barang = {
    '1': {'nama': 'Nasi telur', 'harga': 10000},
    '2': {'nama': 'Nasi sarden', 'harga': 10000},
    '3': {'nama': 'Mie goreng', 'harga': 7000},
    '4': {'nama': 'Es teh', 'harga': 3000},
    '5': {'nama': 'Es jeruk', 'harga': 4000}
}

# Program utama
print("=== WARMINDO RIZKY ===")
nama_pembeli = input("Masukkan nama pembeli: ")

# Tampilkan daftar barang
tampilkan_menu()

# Input pesanan
pesanan = {}
while True:
    kode_barang = input("\nMasukkan kode barang (0 untuk selesai): ")
    if kode_barang == '0':
        break
    
    if kode_barang not in barang:
        print("Kode barang tidak valid!")
        continue
    
    try:
        jumlah = int(input(f"Masukkan jumlah {barang[kode_barang]['nama']}: "))
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue
    except ValueError:
        print("Jumlah harus berupa angka!")
        continue
    
    pesanan[kode_barang] = jumlah

# Hitung total
total_belanja = hitung_total(pesanan)

# Proses pembayaran
while True:
    try:
        pembayaran = int(input(f"\nTotal belanja: Rp{total_belanja:,}\nMasukkan jumlah uang: Rp"))
        if pembayaran < total_belanja:
            print("Uang tidak cukup!")
            continue
        break
    except ValueError:
        print("Input tidak valid!")

# Cetak struk
print("\n=== STRUK PEMBELIAN ===")
print(f"Nama Pembeli: {nama_pembeli}")
print(f"Total Belanja: Rp{total_belanja:,}")
print(f"Pembayaran: Rp{pembayaran:,}")
print(f"Kembalian: Rp{pembayaran - total_belanja:,}")
print("Terima kasih telah berbelanja!")