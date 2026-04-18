#● int(), mengubah string atau data lain menjadi integer (bilangan bulat)
#● str(), mengubah integer atau data lain menjadi string (teks)
#● float(), mengubah string atau integer menjadi float (bilangan desimal)
#● bool(), mengubah data lain menjadi boolean (True/False)

# dari string ke integer
a = "10"
b = int(a)
print(b)        # 10
print(type(b))  # <class 'int'>

# dari float ke integer
c = 5.7
d = int(c)
print(d)        # 5 (dibulatkan ke bawah)

# dari integer ke string
a = 25
b = str(a)
print(b)        # "25"
print(type(b))  # <class 'str'>

# dari float ke string
c = 3.14
d = str(c)
print(d)        # "3.14"

# dari string ke float
a = "9.8"
b = float(a)
print(b)        # 9.8
print(type(b))  # <class 'float'>

# dari integer ke float
c = 7
d = float(c)
print(d)        # 7.0

# nilai kosong atau nol -> False
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False

# nilai selain itu -> True
print(bool(1))        # True
print(bool("Halo"))   # True
print(bool([1, 2]))   # True

#contoh konversi hasil input
nama = input("Masukkan nama Anda: ")
print("Hello", nama)

panjang = input("Masukan panjang persegi panjang: ")
lebar = input("Masukan lebar persegi panjang: ")

# inputan harus dikonversi karena hasil dari input selalu string
luas = int(panjang) * int(lebar)

print("Luas persegi panjang adalah:", luas)
