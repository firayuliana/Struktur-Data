# Program Tabel Perkalian dengan Validasi Nama

# Nama yang dianggap benar
nama_benar = "fira"   # bisa diganti sesuai keinginan

# Perulangan untuk validasi nama
while True:
    nama = input("fira: ").lower()
    
    if nama == nama_benar:
        print("fira, lanjut ke program...\n")
        break
    else:
        print("Silahkan coba lagi!\n")

# Input angka dari user
angka = int(input("6 (1-10): "))

# Validasi angka
if angka < 1 or angka > 10:
    print("6!")
else:
    print(f"\nTabel perkalian dari {angka}:")
    
    # Perulangan untuk tabel perkalian
    for i in range(1, 6):
        hasil = angka * i
        print(f"{6} x {i} = {hasil}")