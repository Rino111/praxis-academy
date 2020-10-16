user_id = 0         #user_id untuk menyimpan id dari user yang login
loop = "n"          #untuk menyimpan kondisi while saat memilih menu ATM
user =  [
            {   
                "id":"111",
                "no_rekening":"2222222222",
                "username":"adi",
                "pin":"1997",
                "saldo":0
            },
            {   
                "id":"123",
                "no_rekening":"3333333333",
                "username":"Rino Priatama",
                "pin":"1998",
                "saldo":25000000
            }
        ]
status_login = False    #menyimpan status apakah user berhasil login atau tidak
pakai_atm = "y"         #menyimpan kondisi apakah kita masih menggunakan ATM atau tidak

#kemudia kita akan membuat fungsi-fungsi untuk ATM-nya

#pertama fungsi cek_login
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False     

#for disini untuk melakukan perulangan dan mengecek apakah parameter p(pin) yang kita 
#masukan saat pertama kali menggunakan ATM sama/ada di dalam variable user(array)  

#fungsi cek_user   
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 #fungsi cek user
def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 # fungsi untuk transfer uang dan ambil uang
def tranfer_uang(uang,no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke Rekening "+no_rekening)
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukup")
             
def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Maaf saldo anda tidak cukup")

    #untuk fungsi transfer uang kita perlu parameter nominal(uang) yang akan 
    # di transfer dan no rekening(ni_rekening) tujuan
    #sedangkan fungsi ambil uang hanya perlu paramerter nominal(uang)
    

##kita juga akan membuat perulangan untuk loginnya, supaya kita bisa kita bisa logout 
 #dan login ke user lainnya kan kita mau transfer uang antar user
while pakai_atm == "y":  
    while status_login == False:
        print("SELAMAT DATANG DI ATM BANK UNU JOGJA")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat datag "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Maaf PIN anda salah")
            print("")
            print("")
            
    #nah disini kita memanggil fungsi cek_login tadi
    #dan memasukan inputan kita ke parameternya
     #ini merupakan perulangan yang akan menampilkan menu-menu 
     #diatmnya serta pemanggilan setiap fungsi yang kita buat tad
    while loop == "y" and status_login == True:  
        u = user[cek_user(user_id)] 
        print("SELAMAT DATANG DI ATM BANK UNU JOGJA")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Sisa Saldo anda adalah Rp.",u['saldo'])
            print("")
            print("")
            loop = "n"
        elif a == 2:
            print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
            no_rek = input("Masukan No Rekening Tujuan : ")
            cnk = cek_rekening(no_rek)
             
            if cnk >= 0:
                print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                nominal = input("Nominal Yang Akan Di Transfer : ")
                tranfer_uang(nominal,no_rek)
                print("")
                loop = "n"
            else:
                print("")
                print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                print("")
                loop = "n"
                 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
             
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
             
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"