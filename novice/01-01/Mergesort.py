def ms(list):
    print('Memecah List', list)
    n = len(list)
    if n < 2:
        return list
    else:
        mid=n//2
        left=list[:mid]
        right=list[mid:]
        ms(left)
        ms(right)
        i=0
        j=0
        k=0
        while i < len (left) and j < len (right):
            if left[i]>right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i < len (left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j < len (right):
            list[k]=right[j]
            j=j+1
            k=k+1
    print('Menggabungkan List', list)
list = [2,5,60,43,27,10,89,17]
ms(list)