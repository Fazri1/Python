import random

print("""   Permaninan Tebak Angka
-----------------------------
""")
randomNumber = int(random.randint(1, 10))
nama = input("Siapa namamu? : ")
inginBermain = input("Hai {}, Ingin Bermain? (Y/N) ".format(nama))
print("Selamat datang di permainan\n")
attempt = 1

while inginBermain.lower() == "y":
    tebak = int(input("Tebak angkanya (1 sampai 10) : "))
    if tebak == randomNumber:
        print("Hore! Kamu benar.")
        print("Kamu berhasil ditebakkan yang ke-{}".format(attempt))
        mainLagi = input("\nApakah kamu ingin bermain lagi? (Y/N) ")
        if mainLagi.lower() == ('n'):
            print("Terima kasih telah bermain.")
            break
        attempt = 1
        randomNumber = int(random.randint(1, 10))
    elif tebak < 0 or tebak > 10:
        print("Tolong tebak angkanya sesuai dengan yang diberikan")
    elif tebak > randomNumber:
        print("Lebih kecil")
        attempt += 1
    elif tebak < randomNumber:
        print("Lebih besar")
        attempt += 1
else:
    print("Ok {}, mungkin dilain hari.".format(nama))
