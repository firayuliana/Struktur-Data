data_nahasiswa = [
    "citra",77,
    "kia",94,
    "ika",90,
    "fira",81,
    "intan",83,
    "vivi",72,  
]

print ("\n\t\tPILIH MENU")
print("="*40)
print("1. Tampilkan Data")
print("2. Tambah Data")
print("3. Ubah Data")
print("4. Hapus Data")
print("5. Cari Data")
print("6. Urutkan Data")
print("7. Hitung Rata-rata")
print("8. Keluar")
print("="*40)

while True:
    print("\n" + "="*40)
    pilihan = input("Pilih menu: ")
    print("="*40)
    if pilihan == "1":
        print("Data Mahasiswa:")
        for i in range(0, len(data_nahasiswa), 2):
            print(f"Nama: {data_nahasiswa[i]},\t\t Nilai: {data_nahasiswa[i+1]}")
    
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        data_nahasiswa.append(nama)
        data_nahasiswa.append(nilai)
        print("Data berhasil ditambahkan!")
    
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        for i in range(0, len(data_nahasiswa), 2):
            if data_nahasiswa[i] == nama:
                nilai = int(input("Masukkan nilai baru: "))
                data_nahasiswa[i+1] = nilai
                print("Data berhasil diubah!")
                break
        else:
            print("Mahasiswa tidak ditemukan.")
    
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        for i in range(0, len(data_nahasiswa), 2):
            if data_nahasiswa[i] == nama:
                del data_nahasiswa[i:i+2]
                print("Data berhasil dihapus!")
                break
        else:
            print("Mahasiswa tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama mahasiswa yang ingin dicari: ")
        for i in range(0, len(data_nahasiswa), 2):
            if data_nahasiswa[i] == nama:
                print(f"Nama: {data_nahasiswa[i]}, Nilai: {data_nahasiswa[i+1]}")
                break
        else:
            print("Mahasiswa tidak ditemukan.")

    elif pilihan == "6":
        # Urutkan berdasarkan nilai (dari tertinggi ke terendah)
        pairs = [(data_nahasiswa[i], data_nahasiswa[i+1]) for i in range(0, len(data_nahasiswa), 2)]
        pairs.sort(key=lambda x: x[1], reverse=True)
        data_nahasiswa.clear()
        for name, score in pairs:
            data_nahasiswa.extend([name, score])
        print("Data berhasil diurutkan!")

    elif pilihan == "7":
        total = sum(data_nahasiswa[i+1] for i in range(0, len(data_nahasiswa), 2))
        rata_rata = total / (len(data_nahasiswa) // 2)
        print(f"Rata-rata nilai mahasiswa: {rata_rata}")

    elif pilihan == "8":
        print("Keluar dari program.")
        break
    
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        