def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
DaftarAngka = [200,1000,26,43,3,211,12,56]
SelectionSort(DaftarAngka)
print(DaftarAngka)