# ● elif (else if) digunakan untuk mengecek beberapa kondisi secara berurutan

nilai = int(input("Masukkan nilai: "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
elif nilai >= 60:
    print("Grade D")
else:
    print("Grade E")