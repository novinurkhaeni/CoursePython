nama = input("Masukkan nama Anda: ")
print("Hello", nama)

umur_teks = input("Masukan umur Anda: ")
# hasil dari input selalu string
umur = int(umur_teks)

print("Umur Anda:", umur)
print("Tipe data sebelum di konversi", type(umur_teks))
print("Tipe data setelah di konversi", type(umur))