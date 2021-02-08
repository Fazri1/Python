# Kelompok TI01-C
# Fitur tambahan :
# -Loading
# -Minimal : setoran awal, setoran tunai, tarik tunai, transfer
# -Maksimal : setoran tunai, tarik tunai
# -Fitur Info Saldo

import random
import sys
import time
import string

# waktu jeda


def tunggu(teks):
    for i in teks + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1)

# buka file nasabah


def fileNasabah():
    global f
    f = open('nasabah.txt')
    for i in f:
        i = i.split(',')
        dataNasabah[i[0]] = [i[1], int(i[2])]

# buka file transfer


def fileTransfer():
    global f
    f = open('transfer.txt')
    for each_line in f:
        data = each_line.split(",")
        dataTransfer.append([data[0], data[1], data[2], data[3]])
        dataTransferSumber.append(data[1])
    for i in dataTransfer:
        for j in i:
            dataTransferSingle.append(j)

# fitur buka rekening


def bukaRekening():
    print("\n", "*"*3, "BUKA REKENING", "*"*3, "\n")
    nama = input("Masukkan nama: ")
    setoranAwal = int(input("Masukkan setoran awal: "))
    if setoranAwal < 100000:
        print('Minimal setoran awal: 100000')
    else:
        norek = "REK" + ''.join(random.choice(string.digits) for i in range(3))
        tunggu(".....")
        print("Pembukaan rekening dengan nomor",
              norek, "atas nama", nama, "berhasil.")
        nasabah = [norek, nama, str(setoranAwal)]
        myfile = open('nasabah.txt', 'a+')
        myfile.write(','.join(nasabah) + '\n')
        myfile.close()

# fitur setoran tunai


def setoranTunai():
    print("\n", "*"*3, "SETORAN TUNAI", "*"*3)
    nomorRekening = input("Masukkan nomor rekening: ")
    nominal = int(input("Masukkan nominal yang akan disetor: "))
    nomorRekening = nomorRekening.upper()
    if nomorRekening in dataNasabah:
        for i in dataNasabah:
            if i == nomorRekening:
                if nominal < 20000 or nominal > 10000000:
                    print('Minimal: 20000. Maksimal: 10000000. Setoran tunai gagal')
                else:
                    print("Setoran tunai sebesar", nominal,
                          "ke rekening", nomorRekening, "berhasil.")
                    dataNasabah[nomorRekening][1] += nominal
                    f = open('nasabah.txt', 'w')
                    for k, v in dataNasabah.items():
                        data = [k, v[0], str(v[1])]
                        f.write(','.join(data) + '\n')
    else:
        print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")

# fitur tarik tunai


def tarikTunai():
    print("\n", "*"*3, "TARIK TUNAI", "*"*3)
    nomorRekening = input("\nMasukkan nomor rekening: ")
    nominal = int(input("Masukkan nominal yang akan ditarik: "))
    nomorRekening = nomorRekening.upper()
    if nomorRekening in dataNasabah:
        for i in dataNasabah:
            if i == nomorRekening:
                if nominal > dataNasabah[nomorRekening][1]:
                    print("Saldo tidak mencukupi. Tarik tunai gagal.")
                elif nominal < 10000 or nominal > 5000000:
                    print('Minimal: 10000. Maksimal: 5000000')
                else:
                    dataNasabah[nomorRekening][1] -= nominal
                    f = open('nasabah.txt', 'w')
                    for k, v in dataNasabah.items():
                        data = [k, v[0], str(v[1])]
                        f.write(','.join(data) + '\n')
                    print("Tarik tunai sebesar", nominal,
                          "dari rekening", nomorRekening, "berhasil.\n")
    else:
        print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")

# fitur transfer


def transfer():
    print("\n", "*"*3, "TRANSFER", "*"*3)
    norekSumber = input("\nMasukkan nomor rekening sumber: ")
    norekTujuan = input("Masukkan nomor rekening tujuan: ")
    nominal = int(input("Masukkan nominal yang akan ditransfer: "))
    norekSumber = norekSumber.upper()
    norekTujuan = norekTujuan.upper()
    if norekSumber in dataNasabah and norekTujuan in dataNasabah:
        for i in dataNasabah:
            if i == norekSumber:
                if nominal < 20000:
                    print('Minimal transfer: 20000')
                elif nominal > dataNasabah[norekSumber][1]:
                    print("Saldo tidak mencukupi. Transfer gagal.")
                else:
                    dataNasabah[norekSumber][1] -= nominal
                    dataNasabah[norekTujuan][1] += nominal
                    f = open('nasabah.txt', 'w')
                    for k, v in dataNasabah.items():
                        data = [k, v[0], str(v[1])]
                        f.write(','.join(data) + '\n')
                    noTransfer = "TRF" + \
                        ''.join(random.choice(string.digits)
                                for i in range(3))
                    transfer = [noTransfer, norekSumber,
                                norekTujuan, str(nominal)]
                    print("Transfer sebesar", nominal, "dari rekening",
                          norekSumber, "ke rekening", norekTujuan, "berhasil.")
                    f = open('transfer.txt', 'a+')
                    f.write(','.join(transfer) + '\n')
    elif norekSumber not in dataNasabah:
        print("Nomor rekening sumber tidak terdaftar. Transfer gagal.")
    else:
        print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.")

# fitur daftar transfer


def daftarTransfer():
    fileTransfer()
    print("\n", "*"*3, "LIHAT DATA TRANSFER", "*"*3)
    norek = input("Masukkan nomor rekening sumber transfer: ")
    norek = norek.upper()
    if norek in dataTransferSumber:
        for k in range(len(dataTransfer)):
            if norek == dataTransfer[k][1]:
                print(dataTransfer[k][0], dataTransfer[k][1],
                      dataTransfer[k][2], int(dataTransfer[k][3]))
    elif norek not in dataTransferSingle:
        print("Nomor rekening sumber tidak terdaftar.")
    else:
        print("Tidak ada data yang ditampilkan")
    dataTransfer.clear()

# fitur info saldo


def infoSaldo():
    print("\n", "*"*3, "INFO SALDO", "*"*3)
    norek = input("Masukkan nomor rekening: ")
    norek = norek.upper()  # variabel norek dijadikan huruf kapital
    fileNasabah()  # memanggil fungsi fileNasabah
    if norek in dataNasabah:  # kondisional jika variabel norek ada di variabel dataNasabah
        for i in dataNasabah:  # perulangan dalam variabel dataNasabah
            if i == norek:  # jika variabel i adalah norek, isi dari variabel i adalah key dari variabel dataNasabah
                # value index 1 dalam key dari dictionary diprint
                print("Saldo rekening anda:", dataNasabah[norek][1])
    else:
        print("Nomor rekening tidak terdaftar.")


dataNasabah = {}
dataTransfer = []
dataTransferSingle = []
dataTransferSumber = []

# daftar menu
while True:
    fileNasabah()
    print("\n", "*"*5, "SELAMAT DATANG DI NF BANK", "*"*5)
    print("\n" + """MENU:
[1] Buka rekening
[2] Setoran tunai
[3] Tarik tunai
[4] Transfer
[5] Lihat daftar transfer
[6] Keluar
[7] Info saldo""" + "\n")
    menu = input("Masukkan menu pilihan anda: ")

    if menu == "1":
        bukaRekening()
    elif menu == "2":
        setoranTunai()
    elif menu == "3":
        tarikTunai()
    elif menu == "4":
        transfer()
    elif menu == "5":
        daftarTransfer()
    elif menu == "6":
        print("Terima kasih atas kunjungan Anda...")
        f.close()
        break
    elif menu == "7":
        infoSaldo()
    else:
        print("Pilihan anda salah. Ulangi.")
