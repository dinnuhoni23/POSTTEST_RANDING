import os
os.system("cls")
#Fungsi isinstance() mengembalikan True jika objek yang ditentukan adalah tipe yang ditentukan, jika tidak, False.

def seperate(item):
    result = []
    for variable in item:
        if isinstance(variable, list):
            for i in variable:
                if isinstance(i, list):
                    for a in i :
                        # print(int(a))
                        result.append (int (a))
                elif isinstance(i, int) :
                    # print(i)
                    result.append (i)
        else :
            # print(variable)
            result.append(variable)
    return result

def partition(l, bawah, atas):
  pivot = l[bawah] 
  pos_batas = bawah+1
  for j in range(bawah+1,atas):
    if l[j] < pivot:
      l[pos_batas],l[j]=l[j],l[pos_batas]
      pos_batas += 1
  l[pos_batas-1],l[bawah] = l[bawah],l[pos_batas-1]
  return pos_batas

def quicksort(l, bawah, atas):
  if bawah < atas:
    pi = partition(l, bawah, atas)
    quicksort(l, bawah, pi -1)
    quicksort(l, pi + 1, atas)

def func(l):
  s = seperate(l)

  quicksort(s, 0, len(s))

  return s

variable = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]

print('Sebelum sorting:',variable)
t = func(variable)
print('Setelah sorting:',t)