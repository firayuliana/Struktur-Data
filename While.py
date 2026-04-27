while True:
    angka = float(input("Masukkan angka: "))
    
    if angka >= 0:
        # Jika angka positif atau nol, keluar dari perulangan
        break
    else:
        # Jika angka negatif, tampilkan pesan dan ulangi lagi
        print("Harus positif!")

print(f"Terima kasih! Kamu memasukkan angka: {angka}")