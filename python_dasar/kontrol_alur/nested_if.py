# ● Kita bisa menempatkan if di dalam if yang lain

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "123456":
        print("Login berhasil")
        print("Selamat datang Admin")
    else:
        print("Password salah")
else:
    print("Username tidak ditemukan")