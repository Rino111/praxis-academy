#Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data.
#List adalah struktur data yang menyimpan koleksi data terurut
#kita dapat menyimpan sequence / rangkaian item menggunakan list.
#item dalam list ditutup menggunakan kurung siku [] (list literal)
#Setelah list dibuat anda bisa menambah, mengurangi, dan mencari item pada list


fruits = ["duren", "salak", "mangga", "kelapa"]
#List dapat kita buat seperti membuat variabel biasa,
#namun nilai variabelnya diisi dengan tanda kurung siku ([]).
#Apabila list-nya memiliki lebih dari satu isi, maka kita bisa memisahnya dengan tanda koma

print (fruits[2])
#Setelah kita tahu cara membuat dan menyimpan data di dalam List, mari kita coba mengambil datanya.
#List sama seperti array, list juga memiliki nomer indeks untuk mengakses data atau isinya.
#Nomer indeks list selalu dimulai dari nol (0).
#Nomer indeks ini yang kita butuhkan untuk mengambil isi (item) dari list.

print(f"Semua buah: ada {len(fruits)} buah")
for b in fruits:
    print (b)
#Pada kode di atas, kita menggunakan fungsi len() untuk mengambil panjang list.

fruits.insert(2, "jeruk")
print(fruits)
#Tedapat Tiga metode (method) atau fungsi yang bisa digunakan untuk menambahkan isi atau item ke List:
#kalau insert menambahkan item dari indeks tertentu


del fruits[3]
print (fruits)
#Untuk menghapus salah satu isi dari List, kita bisa menggunakan perintah del.
#Perintah del akan menghapus sebuah variabel dari memori.

print (fruits[1:5])
#Memotong list
#Seperti string, list juga dapat dipotong-potong.

f = fruits.pop(1)
print(f)

#menghapus item pada indexs yang ada diberikan dari daftar
#dan mengembalikan item yang dihapus.

print (fruits.count("duren"))


print (fruits.index("kelapa"))




