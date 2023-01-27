import os

# Struktur Database
TEMPLATE = {
    "nopol": 30*" ",
    "tipe": 30*" ",
    "warna": 30*" ",
    "pemilik": 30*" ",
    "kontak": 30*" ",
    "status": 30*" ",
    "biaya": 30*" ",
}

# Fungsi Tampilan Menu
def menu():
    os.system("clear")
    print("="*50)
    print("Selamat Datang Di Program".center(50))
    print("Rental Mobil".center(50))
    print("="*50 + "\n")
    print("1. Lihat daftar mobil")
    print("2. tambah daftar mobil")
    print("3. Memperbarui data mobil")
    print("4. Menghapus data mobil")
    print("5. Keluar\n")

# Fungsi Menampilkan Data
def daftar_mobil():
    print("="*93)
    print("NO |   NOPOL   |    TIPE   |  WARNA   |     PEMILIK     |   KONTAK    |  STATUS  |   BIAYA  |")
    print("="*93)

    with open("garasi.txt", "r") as file:
        data = file.readlines() 
        
        for index,data in enumerate(data):
            content = data.split(",")
            nopol =  content[0]
            tipe = content[1]
            warna = content[2]
            pemilik = content[3]
            kontak = content[4]
            status = content[5]
            biaya = content[6]

            print(f"{index+1:2} | {nopol:.9} | {tipe:.9} | {warna:.8} | {pemilik:.15} | {kontak:.11} | {status:.8} | Rp{biaya:.13}")

    print("="*93)
    x = input("")

# Fungsi Menambah daftar mobil
def memasukkan_data():
    os.system("clear")
    nopol = input("Masukkan Nopol : ")
    tipe = input("Tipe           : ")
    warna = input("Warna          : ")
    pemilik = input("Pemilik        : ")
    kontak = input("Kontak         : ")
    status = input("Status         : ")
    biaya = input("Biaya          : ")

    database = TEMPLATE.copy()

    database["nopol"] = nopol + TEMPLATE["nopol"][len(nopol):]
    database["tipe"] = tipe + TEMPLATE["tipe"][len(tipe):]
    database["warna"] = warna + TEMPLATE["warna"][len(warna):]
    database["pemilik"] = pemilik + TEMPLATE["pemilik"][len(pemilik):]
    database["kontak"] = kontak + TEMPLATE["kontak"][len(kontak):]
    database["status"] = status + TEMPLATE["status"][len(status):]
    database["biaya"] = biaya + TEMPLATE["biaya"][len(biaya):]

    data = f'{database["nopol"]},{database["tipe"]},{database["warna"]},{database["pemilik"]},{database["kontak"]},{database["status"]},{database["biaya"]}\n'

    with open("garasi.txt", "a") as file:
        file.write(data)

## Fungsi Memperbarui data
def memperbarui_mobil():
    daftar_mobil()
    index = int(input("Masukkan Nomor Data : "))

    with open("garasi.txt", "r+") as file:
        data = file.readlines()

        for no,content in enumerate(data):
            content = content.split(",")
            if no == index - 1:
                break

        nopol =  content[0]
        tipe = content[1]
        warna = content[2]
        pemilik = content[3]
        kontak = content[4]
        status = content[5]
        biaya = content[6].replace("\n", "")

        os.system("clear")
        print(f"1. Nopol   : {nopol}")
        print(f"2. Tipe    : {tipe}")
        print(f"3. Warna   : {warna}")
        print(f"4. Pemilik : {pemilik}")
        print(f"5. Kontak  : {kontak}")
        print(f"6. Status  : {status}")
        print(f"7. Biaya   : {biaya}")
        
        pilihan = input("Masukkan Pilihan [1,2,3,4,5,6,7] : ")

        match pilihan:
            case "1": nopol = input("Masukkan nopol baru : ")
            case "2": tipe = input("Masukkan tipe baru : ")
            case "3": warna = input("Masukkan warna baru : ")
            case "4": pemilik = input("Masukkan pemilik baru : ")
            case "5": kontak = input("Masukkan kontak baru : ")
            case "6": status = input("Masukkan status baru : ")
            case "7": biaya = input("Masukkan biaya baru : ")

        database = TEMPLATE.copy()

        database["nopol"] = nopol + TEMPLATE["nopol"][len(nopol):]
        database["tipe"] = tipe + TEMPLATE["tipe"][len(tipe):]
        database["warna"] = warna + TEMPLATE["warna"][len(warna):]
        database["pemilik"] = pemilik + TEMPLATE["pemilik"][len(pemilik):]
        database["kontak"] = kontak + TEMPLATE["kontak"][len(kontak):]
        database["status"] = status + TEMPLATE["status"][len(status):]
        database["biaya"] = biaya + TEMPLATE["biaya"][len(biaya):]

        data = f'{database["nopol"]},{database["tipe"]},{database["warna"]},{database["pemilik"]},{database["kontak"]},{database["status"]},{database["biaya"]}\n'
        panjang_data = len(data)

        with open("garasi.txt", "r+",encoding="utf-8") as file:
            file.seek(panjang_data * (index - 1))
            file.write(data)

while True:
    menu()
    opsi = input("Masukkan Opsi : ")

    match opsi:
        case "1": daftar_mobil()
        case "2": memasukkan_data()
        case "3": memperbarui_mobil()
        case "1": pass
        case "1": pass
