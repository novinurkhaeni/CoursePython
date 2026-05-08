# ● match-case adalah fitur alternatif yang lebih bersih untuk elif yang banyak

hari = input("Masukkan nama hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari kerja")
    case "sabtu" | "minggu":
        print("Hari libur")
    case _:
        print("Nama hari tidak valid")