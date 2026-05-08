# ● Karena kondisi harus bernilai boolean, artinya kita bisa menggunakan operator,
# misal operator logika, seperti and, or dan not

umur = int(input("Masukkan umur Anda: "))
punya_sim = input("Punya SIM? (ya/tidak): ")

if umur >= 17 and punya_sim == "ya":
    print("Boleh mengendarai motor")
else:
    print("Tidak boleh mengendarai motor")