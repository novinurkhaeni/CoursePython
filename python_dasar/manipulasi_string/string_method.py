nama = "Alice"
nama_upper = nama.upper()
print(nama_upper) #ALICE
nama_lower = nama.lower() #alice
print(nama_lower)

nama = "john doe"
nama_title = nama.title()
print(nama_title) #John Doe
nama_capitalize = nama.capitalize()
print(nama_capitalize) #John Doe

nama = " Alice Monrow "
nama_strip = nama.strip()
print(nama_strip) #AliceMonrow

kalimat = "I love Java"
kalimat_baru = kalimat.replace("Java", "Python")
print(kalimat_baru) #I love Python

nama = "Mississippi"
jumlah_s = nama.count("s")
print(jumlah_s) #4

kalimat = "Python Programming"
posisi = kalimat.find("Programming")
print(posisi) #7
