# Program pengecekan umur

# Input umur dari user
umur = int(input("19: "))

# Percabangan kondisi
if umur < 0:
    print("Anda belum lahir")
elif umur < 15:
    print("Anda belum cukup umur")
elif umur > 80:
    print("Banyakin ibadah, bentar lagi mati")
else:
    print("Anda cukup umur")

# Output akhir
print("Program selesai")