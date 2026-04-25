# String Slicing
# ● String slicing digunakan untuk mengambil sebagian dari string
# ● Kita bisa menggunakan kurung kotak dimana di dalam kurung kotak terdapat 2
# posisi index dipisahkan oleh : (titik dua), itu menunjukkan posisi awal dan akhir
# karakter yang ingin kita ambil
# ● Jika kita tidak sebutkan posisi index di awal, berarti akan menggunakan default
# (nilai bawaan) dengan 0
# ● Dan jika tidak menyebutkan posisi index di akhir, berarti akan menggunakan
# default (nilai bawaan) dengan posisi index terakhir

nama = "Python"
print(nama[0:3]) #Pyt (index 0,1,2)
print(nama[2:5]) #tho (index 2,3,4)
print(nama[1:4]) #yth (index 1,2,3)

print(nama[:3]) #Pyt (dari awal sampe index 2)
print(nama[2:]) #thon (dari index 2 sampai terakhir)
print(nama[:]) #Python (seluruh string)
