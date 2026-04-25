# ● String interpolation adalah cara modern untuk menggabungkan variabel dengan
# teks.
# ● Ini lebih mudah dibaca dan lebih efisien daripada concatenation menggunakan +
# (plus).
# ● f-strings adalah cara terbaru dan paling direkomendasikan untuk string
# interpolation di Python, yaitu dengan menambah huruf f di awal ketika membuat
# string
# ● Selanjutnya di dalam nilai string, kita bisa menggunakan kurung kurawal untuk
# mengakses variabel lain

nama = "Alice"
umur = 25
kota = "Jakarta"

# Menggunakan f-string
profil = f"Hallo, nama saya {nama}, umur {umur} tahun, tinggal di {kota}"
print(profil)

# lebih jelas dibandingkan concatenation +
profil_lama = "Halo, nama saya, " + nama + ", umur " + str(umur) + " tahun, tinggal di " + kota
print(profil_lama)