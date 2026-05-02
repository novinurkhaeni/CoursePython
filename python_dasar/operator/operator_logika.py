# ● Operator logika digunakan untuk menggabungkan atau memodifikasi nilai 
# boolean.
# ● and (dan), menghasilkan True jika kedua kondisi True
# ● or (atau), menghasilkan True jika salah satu kondisi True
# ● not (tidak), membalik nilai boolean

umur = 25
print(umur > 18 and umur < 30)
#true, karena 25 > 18 adalah true, 25 < 30 adalah true
#jika kedua kondisi true, maka hasilnya adalah true

hari = "Sabtu"
print(hari == "Sabtu" or hari == "Minggu")
#true,karena Sabtu == Sabtu adalah true, atau Sabtu == Minggu adalah false
#jika salah satu kondisi benar, maka hasilnya adalah benar

aktif = True
print(not aktif) # kebalikan true adalah false