#ALGORITMA SEARCH
import math
def jumpSearch(arr, x, n):
    prev = 0
    step = math.sqrt(n)
    while arr[int(min(step, n) - 1)] < x:
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == x:
        return prev
    return -1
#----------------------------------------------------------#
#ALGORITMA SORT
def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for j in range(bwh+1,atas):
        if l[j] < pivot:
            l[pos_batas],l[j]=l[j],l[pos_batas]
            pos_batas += 1
    l[pos_batas-1],l[bwh] = l[bwh],l[pos_batas-1]
    return pos_batas
    
def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    q = partition(l, bwh, atas)
    quicksort(l, bwh, q-1)
    quicksort(l, q, atas)
    return l

def merge_sort(lst):
    if len(lst) <= 1: 
        return lst 
    tengah = len(lst) // 2 
    kiri = merge_sort(lst[:tengah])
    kanan = merge_sort(lst[tengah:])
    return integrator(kiri, kanan)

def integrator(left, right): 
    result = []
    i, j = 0, 0 

    while i < len(left) and j < len(right): 
        if left[i] < right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1

    result += left[i:]
    result += right[j:]
    return result
#-----------------------------------------------------------#
#SEPARATOR FUNCTION
def nested_str_separator(raw_data):
    main_data = []
    nested_list = {}
    for a in range(len(raw_data)):
        if type(raw_data[a]) == str:
            main_data.append(raw_data[a])
        else:
            nested_list[a] = merge_sort(raw_data[a])
    main_data = quicksort(main_data,0,len(main_data))
    for a in nested_list:
        main_data.insert(a,nested_list[a])
    return main_data
#------------------------------------------------------------#
data = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
main_data = nested_str_separator(data)

print("Data sebelum di sort :\n",data)
print("\nData Setelah di sort :\n",main_data)

loop = True
while (loop):

    search = str(input("\nNama yang ingin dicari : "))
    print()
    for baris in reversed(range(len(main_data))):
        if type(main_data[baris]) == list:
            idx = jumpSearch(main_data[baris],search,len(main_data[baris]))
            if idx != -1:
                print(search,"berada di index ke -",baris,"kolom",idx)
        else:
            if main_data[baris] == search:
                print(search,"berada di index ke -",baris)
    choose = str(input("Apakah anda ingin mencari lagi? (y/n): "))
    if (choose) == "y":
        "p"
    else: 
        loop = False