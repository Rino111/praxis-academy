def BubbleSort(val):
    for namber in range(len(val)-1,0,-1):
        for i in range(namber):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

DaftarAngka = [50,7,2,69,4,45,14,220]
BubbleSort(DaftarAngka)
print(DaftarAngka)