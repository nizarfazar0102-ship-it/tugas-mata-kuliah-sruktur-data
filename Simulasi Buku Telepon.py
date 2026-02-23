def tampilkan_menu():
    print("\n--- Simulasi Buku Telepon ---")
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. Keluar")

def tambah_kontak(buku_telepon):
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor telepon: ")
    buku_telepon[nama] = nomor
    print(f"Kontak {nama} berhasil ditambahkan.")

def lihat_kontak(buku_telepon):
    if not buku_telepon:
        print("Buku telepon kosong.")
    else:
        print("\n--- Daftar Kontak ---")
        for nama, nomor in buku_telepon.items():
            print(f"Nama: {nama}, Nomor: {nomor}")

def cari_kontak(buku_telepon):
    nama = input("Masukkan nama yang dicari: ")
    nomor = buku_telepon.get(nama)
    if nomor:
        print(f"Nomor {nama} adalah {nomor}.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def hapus_kontak(buku_telepon):
    nama = input("Masukkan nama yang akan dihapus: ")
    if nama in buku_telepon:
        del buku_telepon[nama]
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Kontak {nama} tidak ditemukan.")

def main():
    buku_telepon = {}  # Menggunakan dictionary untuk menyimpan kontak
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah_kontak(buku_telepon)
        elif pilihan == '2':
            lihat_kontak(buku_telepon)
        elif pilihan == '3':
            cari_kontak(buku_telepon)
        elif pilihan == '4':
            hapus_kontak(buku_telepon)
        elif pilihan == '5':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
