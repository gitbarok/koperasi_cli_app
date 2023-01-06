import os
import datetime
from time import sleep
from utils.user import User
from utils.validation import Validation

UNDERSCORE = '-'*41
DATE_NOW = datetime.datetime.now()

class UserInterface():
    def interface():
        os.system('clear')
        hashtag = "#" * 35
        print("[" + hashtag + "]")
        print("         Koperasi Maju Bersama                   ")
        print(" ")
        print("         {}     ".format(  DATE_NOW.strftime("%m/%d/%Y, %H:%M:%S")))
        print("[" + hashtag + "]")

    def menu():
        while True:
            UserInterface.interface()
            print("          Selalu Ada Duit!\n")
            print("[1]. Login | [2]. Register | [3]. Keluar")
            print(UNDERSCORE)
            option = input("Pilih menu anda: ")
            if option == '1':
                UserInterface.login_account()
                break
            elif option == '2':
                UserInterface.register_account()
                break
            elif option == '3':
                os.system("clear")
                print("     Anda Berhasil Keluar")
                sleep(2)
                os.system("clear")
                break
            print("Menu tidak ada, silahkan pilih dengan benar")
            sleep(2)
            os.system("clear")


    def login_account():
        while True:
            UserInterface.interface()
            global no_anggota
            no_anggota = input("Masukkan Nomor Anggota: ")
            global password
            password = input("Masukkan Password: ")
            check = User()
            login_check=check.login(no_anggota, password)
            if login_check is True:
                UserInterface.menu_login()
                break
            else:
                os.system("clear")
                print("username atau password salah")
                sleep(2)

    def menu_login():
        while True:
            UserInterface.interface()
            print("          Selalu Ada Duit!\n")
            print("[1]. Minjam Uang | [2]. Info Akun  | [3]. Kembali Ke Menu")
            print(UNDERSCORE)
            option = input("Pilih menu anda: ")
            if option == '1':
                UserInterface.minjam_uang()
                break
            elif option == '2':
                UserInterface.info_akun()
                break
                # UserInterface.menu_login()
            elif option == '3':
                UserInterface.menu()
                break
            print("Menu tidak ada, silahkan pilih dengan benar")
            sleep(2)
            os.system("clear")

    def minjam_uang():
        while True:
            UserInterface.interface()
            value = str(input("Jumlah pinjaman yang diinginkan: "))
            borrow_validation = Validation.validation_borrow(value)
            if borrow_validation is True:
                int_value = int(value)
                check = User()
                minjam = check.borrow_money(int_value,no_anggota)
                print("Berhasil Meminjam Uang")
                print(UNDERSCORE)
                print("Dalam 3 detik anda akan kembali ke menu")
                sleep(2)
                UserInterface.menu_login()
                break
            else:
                print("masukkan jumlah pinjaman dengan benar. tanpa special karakter")
                sleep(2)

    def info_akun():
        while True:
            UserInterface.interface()
            info = User()
            hasil = info.account_info(no_anggota)
            print("Nama anda adalah: ",hasil[0])
            print(UNDERSCORE)
            print("Unik id anda adalah: ",hasil[1])
            print(UNDERSCORE)
            print("Balance anda adalah: ",hasil[2])
            print(UNDERSCORE)
            menu_option = input("Tekan Y/y untuk kembali ke menu? ")
            if menu_option.lower() == 'y':
                print("Dalam 3 detik anda akan kembali ke menu")
                sleep(2)
                UserInterface.menu_login()
                break
            else:
                print("menu yang anda masukkan tidak ada")
                sleep(2)

    def register_account():
        while True:
            UserInterface.interface()
            nama_depan = input("Masukkan Nama: ")
            password = input("Masukkan Password: ")
            register_validation = Validation.validation_register(nama_depan, password)
            if register_validation is True:
                akun_baru = User(nama_depan, password)
                unik_id = akun_baru.register()
                print(UNDERSCORE)
                print("Sedang membuat id unik untuk anda login")
                sleep(2)
                print(UNDERSCORE)
                print("Id Unik anda untuk login adalah : " + str(unik_id))
                print(UNDERSCORE)
                print("Dalam 3 detik anda akan kembali ke menu utama")
                sleep(2)
                UserInterface.menu()
                break
            else:
                print("Nama dan kata sandi harus lebih dari 4 karakter dan nama tidak boleh memuat karakter spesial")
                sleep(2)
            

if __name__ == "__main__":
    os.system("clear")
    UserInterface.menu()