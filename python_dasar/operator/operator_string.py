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