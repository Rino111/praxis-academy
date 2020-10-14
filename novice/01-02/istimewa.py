
import tanah as jumlah

jumlah.tambah(6,5)
perkalian = jumlah.perkalian(9,5)
print(perkalian)

DaftarAngka = [50,9,62,99,2,35,41,80]
BubbleSort = jumlah.BubbleSort(DaftarAngka)
print(DaftarAngka)

angka = [53,24,83,43,44,21,91,90]
SelectionSort = jumlah.SelectionSort(angka)
print(angka)

list = [2,54,38,76,23,56,84,90]
print("Data yang akan di sort", list)
print("Insertion Sort :")
insertion = jumlah.insertion(list)

print('Menggabungkan List', list)
list = [2,5,60,43,27,10,89,17]
ms = jumlah.ms (list)


list = [67,91,87,33,49,10,16,43,65,3]
print('Data yang akan di sort :', list)
print('Quick Sort :')
qs = jumlah.qs (list,0,len(list)-1)