#MENGGABUNGKAN STRING
#  ● Untuk menggabungkan string, kita bisa menggunakan tanda + (tambah)
# ● Dan tipe data string tidak bisa digabungkan dengan tipe data lain seperti integer,
# float atau boolean, kita harus konversi dulu tipe data lain menjadi tipe data string

nama = "Budi"
umur = 25

# cara yang salah (akan error)
# jika menggabungkan string dengan tioe data lain
# pesan = "Nama saya " + nama + ", umur " + umur

# cara yang benar
pesan = "Nama saya " + nama + ", umur " + str(umur)
print(pesan)
