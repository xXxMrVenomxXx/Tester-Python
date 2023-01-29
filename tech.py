# module
import os,sys,time

# clean text
def clean():
    os.system("clear")

# appearance
def menu():
    clean()
    os.system("figlet Tech Learning")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("•Author: Mr.Venom")
    print("From Lammer To Mastah")
    print("Don't Forget To")
    print("•FOLLOW •SUBSCRIBE •LIKE •COMMENT •SHARE")
    print("YT: https://youtube.com/@mrvenom6329")
    print("IG: @j0s3h3rn4nd3s__")
    print("FB: https://www.facebook.com/profile.php?id=100085581716894")
    print("WEB: https://blogfromlammertomastah.blogspot.com/")
    print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
    print("LIST MENU")
    print("1). Kenalan Dulu Lah")
    print("2). Kamu Apa Kabar?")
    print("3). Pengertian Python")
    print("4). Fungsi Program Python")
    print("5). Pencipta Python")
    example = input("select: ")
    if example =="1":
       salken = input("Saya Mr.Venom, Kamu Namanya Siapa? : ")
       print("Hai Salam Kenal Yaa.. Jgn Lupa Mampir Lagi :D")
       print("==================================================================")
    jalan = True
    while (jalan==True):

        s = input("Masukkan Angka: ")
        n = int(s)
        print("=================================================================")
        print ("Angka yang anda masukkan adalah ", n)
        if (n%2==0):
            print(n, "Adalah bilangan genap")
        else:
            print(n, "Adalah bilangan ganjil")
        print("=========≠=======================================================")
        l = input("ulang dan lagi [Y/n] : ")
        print ("Nah Gitu Dong Ga Di Ulang² Lagi xixixi, Cobain Angka SC(Script) Yg Lain Belum Dipilih, BTW SCRIPT INI SEDANG DIKEMBANGKAN AUTHOR")
        if (l=="n"):
           jalan = False
        print("=================================================================")
    if example =="2":
       kabar = input("Kalau Aku Puji Tuhan Sehat, Kamu Gimana? : ")
    elif example =="2":
         os.system("Syukur Deh Baik Dan Sehat Selalu Yaa...")

    if example =="3":
       pengertian = input("Python Adalah : ")
    elif example =="3":
         os.system("bahasa pemrograman tujuan umum yang ditafsirkan, tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan. " + pengertian)

    if example =="4":
      fungsi = input("Fungsinya Yaitu : ")
    elif example =="4":
         os.system("dapat digunakan untuk mengefisiensi program serta memudahkan programmer dalam menjalankan program besar. " + fungsi)

    if example =="5":
       pencipta = input("Ialah... : ")
    elif example =="5":
         os.system("Python Itu Berbahasa Pemrograman bertujuan umum yang ditafsirkan, tingkat tinggi. Dibuat oleh Guido van Rossum dan pertama kali dirilis pada tahun 1991, filosofi desain Python menekankan keterbacaan kode dengan penggunaan spasi putih yang signifikan. " + pencipta)
menu()
