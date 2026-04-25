# f-strings dapat mengeksekusi ekspresi langsung di dalamnya

harga = 100000
jumlah = 3

#operasi matematika dalam f-string
total = f"Total: Rp {harga*jumlah}"
print(total) #Total: Rp 300,000

#memanggil method di dalam f-string
nama = "john doe"
salam = f"Halo {nama.upper()}!"
print(salam) #Halo John Doe!