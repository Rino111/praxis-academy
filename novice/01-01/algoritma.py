#Fungsi pada Python, dibuat dengan kata kunci def kemudian diikuti dengan nama fungsinya.

def pemandangan():
     print ("sangat indah sekali")

#Sama seperti blok kode yang lain, kita juga harus memberikan identasi
#(tab atau spasi 2x) untuk menuliskan isi fungsi.

#Setelah kita buat, kita bisa memanggilnya

pemandangan()
pemandangan ()

#apapun yang ada di dalam fungsi, ketika dipanggil itulah yang akan dilakukan.

#memberikan input nilai ke dalam fungsi dengan parameter
#Parameter adalah variabel yang menampung nilai untuk diproses di dalam fungsi.

def gunung(sindoro):
    print(sindoro)

#Pada contoh diatas, kita membuat fungsi dengan parameter ucapan.

#Cara pemanggilan fungsi yang memiliki parameter adalah seperti ini:

gunung("sindoro")
# "sindoro" adalah nilai parameter yang kita berikan.

#ketika parameternya lebih dari satu?
#Kita bisa menggunakan tanda koma (,) untuk memisahnya.

def luastanah(panjang, lebar):
    luas = (panjang * lebar) / 2
    print ("Luas Tanah: %f" % luas)

luastanah(10, 5)

def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
             if val[i]>val[i+1]:
                 temp = val[i]
                 val[i] = val[i+1]
                 val[i+1] =temp

                DaftarAngka = [23,7,32,99,4,15,11,20]
                BubbleSort(DaftarAngka)
                print(DaftarAngka)
