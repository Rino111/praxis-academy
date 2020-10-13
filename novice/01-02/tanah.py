def tambah (a,b):
    print(a,'+',b,'=',a+b)
    print('penambahan')

def perkalian(a,b):
    print('perkalian')
    return a * b

def BubbleSort(val):
    for namber in range(len(val)-1,0,-1):
        for i in range(namber):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 