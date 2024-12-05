def tampilkan_menu():
    print("\n=== DAFTAR BARANG ===")
    for kode, item in barang.items():
        print(f"{kode}. {item['nama']} - Rp{item['harga']:,}")
