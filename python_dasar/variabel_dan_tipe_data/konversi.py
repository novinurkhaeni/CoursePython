nama = input("Masukkan nama Anda: ")
print("Hello", nama)

panjang = input("Masukan panjang persegi panjang: ")
lebar = input("Masukan lebar persegi panjang: ")

# inputan harus dikonversi karena hasil dari input selalu string
luas = int(panjang) * int(lebar)

print("Luas persegi panjang adalah:", luas)