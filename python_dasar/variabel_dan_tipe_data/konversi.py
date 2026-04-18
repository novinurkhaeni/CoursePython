#● int(), mengubah string atau data lain menjadi integer (bilangan bulat)
#● str(), mengubah integer atau data lain menjadi string (teks)
#● float(), mengubah string atau integer menjadi float (bilangan desimal)
#● bool(), mengubah data lain menjadi boolean (True/False)

nama = input("Masukkan nama Anda: ")
print("Hello", nama)

panjang = input("Masukan panjang persegi panjang: ")
lebar = input("Masukan lebar persegi panjang: ")

# inputan harus dikonversi karena hasil dari input selalu string
luas = int(panjang) * int(lebar)

print("Luas persegi panjang adalah:", luas)
