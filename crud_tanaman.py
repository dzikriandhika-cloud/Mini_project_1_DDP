 # Program CRUD sederhana untuk data tanaman

# List berisi tuple (nama, jenis, umur)
data_tanaman = [
    ("Padi", "Tumbuhan pangan", "120"),
    ("Jagung", "Tumbuhan pangan", "100"),
    ("Cabai", "Tumbuhan sayur", "90")
]

while True:
    print("\n=== MENU CRUD TANAMAN ===")
    print("1. Tambah Data Tanaman")
    print("2. Lihat Data Tanaman")
    print("3. Update Data Tanaman")
    print("4. Hapus Data Tanaman")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama tanaman: ")
        jenis = input("Masukkan jenis tanaman: ")
        umur = input("Masukkan umur tanaman (hari): ")
        data_tanaman.append((nama, jenis, umur))
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        if not data_tanaman:
            print("Belum ada data.")
        else:
            print("\nDaftar Tanaman:")
            for i, tanaman in enumerate(data_tanaman, start=1):
                print(f"{i}. Nama: {tanaman[0]}, Jenis: {tanaman[1]}, Umur: {tanaman[2]} hari")

    elif pilihan == "3":
        if not data_tanaman:
            print("Belum ada data untuk diupdate.")
        else:
            indeks = int(input("Masukkan nomor data yang ingin diupdate: ")) - 1
            if 0 <= indeks < len(data_tanaman):
                nama = input("Masukkan nama baru: ")
                jenis = input("Masukkan jenis baru: ")
                umur = input("Masukkan umur baru: ")
                data_tanaman[indeks] = (nama, jenis, umur)
                print("Data berhasil diupdate!")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "4":
        if not data_tanaman:
            print("Belum ada data untuk dihapus.")
        else:
            indeks = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
            if 0 <= indeks < len(data_tanaman):
                data_tanaman.pop(indeks)
                print("Data berhasil dihapus!")
            else:
                print("Nomor tidak valid.")

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
