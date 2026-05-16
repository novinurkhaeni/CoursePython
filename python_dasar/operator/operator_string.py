# ● Operator khusus untuk bekerja dengan string.
# ● Concatenation (+), menambah string
# ● Repetition (*), mengulang string sejumlah angka
# ● Membership (in), mengecek apakah text ada dalam string

nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap) #John Doe

kata = "Hello"
print(kata * 3) #HelloHelloHello

garis = "-"
print(garis * 20) #--------------------

kalimat = "Python adalah bahasa pemrograman"
print("Python" in kalimat) #true
print("Golang" in kalimat) #false
print("adalah" in kalimat) #true

# Berikan nilai pada variabel berikut
nama_depan = 'Keisya'
nama_belakang = 'Azizah'
kelas = '11 Rpl 1'
sekolah = "Smk Ma'arif 9 kebumen"

# tampilkan gabungan dari semua variabel diatas
print("nama " + nama_depan + " " + nama_belakang + ", kelas " + kelas + ", sekolah " + sekolah)
print("Nama", nama_depan, nama_belakang + ",", kelas + ",", sekolah)