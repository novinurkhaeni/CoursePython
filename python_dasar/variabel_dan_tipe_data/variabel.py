# ● Tidak boleh dimulai dengan angka
# ● Tidak boleh pakai tanda minus
# ● Tidak boleh pakai keyword Python
# ● Tidak boleh ada spasi

#gaya penulisan variabel
# snake case, contoh nama_depan
# camel case, contoh namaDepan
# pascal case, contoh NamaDepan

# assignment dasar
full_name = "John Doe" #variabel bernama full_name berisi text "John Doe"
age = 25 #variabel bernama age berisi angka 25
height = 170.5 #variabel bernama height berisi angka desimal 170.5
isStudent = True #variabel dengan nama isStudent dengan berisi boolean true
print("Nama Lengkap : ", full_name)

# multiple assignment
x = y = z = 0 #semua variabe; bernilai 0
a, b, c = 1, 2, 3 #a=1 b=2 c=3
name, age = "Maria", 25 #name = "Maria", age = 25
print("Nama Saya : ", name, ", Umur Saya: ", age)

# mengubah nilai variabel
skor = 80 #nilai awal
print("Nilai Awal : ", skor)
skor = 90 #ubah nilai skor
print("Nilai Akhir : ", skor)
skor = "A" #ubah nilai dan tipe data
print("Nilai Huruf: ", skor)

# menggunakan variabel dalam operasi
nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang

panjang = 10
lebar = 5
luas = panjang * lebar

# menggunakan variabel dalam print
print("Nama Lengkap:", nama_lengkap)
print("Luas Persegi Panjang:", luas)
