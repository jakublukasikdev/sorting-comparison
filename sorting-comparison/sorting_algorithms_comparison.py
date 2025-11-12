

import matplotlib.pyplot as plt
import random
import time

lista=[0]*1000

for n in range(0,len(lista)):
    lista[n]=random.randint(0,100)
    #print(lista[n])
lista2=lista.copy()
lista3=lista.copy()
lista4=lista.copy()
lista5=lista.copy()




def bubble_sort(lista):
    for i in range(0,len(lista)):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                s=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=s
        #print(lista[i])

def partition(lista, low, high):
    pivot = lista[high]
    i = low - 1

    for j in range(low, high):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    return i + 1

def quick_sort(lista, low=0, high=None):
    if high is None:
        high = len(lista) - 1

    while low < high:
        pivot_index = partition(lista, low, high)

        # Sortuj mniejsz¹ czêœæ rekurencyjnie, a wiêksz¹ w pêtli (optymalizacja)
        if pivot_index - low < high - pivot_index:
            quick_sort(lista, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quick_sort(lista, pivot_index + 1, high)
            high = pivot_index - 1

def merge_sort(lista):
  if len(lista) <= 1:
    return lista

  mid = len(lista) // 2
  leftHalf = lista[:mid]
  rightHalf = lista[mid:]

  sortedLeft = merge_sort(leftHalf)
  sortedRight = merge_sort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        insert_index = i
        current_value = lista[i]
        for j in range(i-1, -1, -1):
            if lista[j] > current_value:
                lista[j+1] = lista[j]
                insert_index = j
            else:
                break
        lista[insert_index] = current_value
    return lista


def binary_search(lista,x):
    left=0
    right=len(lista)-1

    while left<=right:
        mid=(left+right)//2

        if lista[mid]==x:
            return mid
        if lista[mid]<x:
            left=mid+1
        else:
            right=mid-1
    return -1

def timer(funkcja, lista):
    start = time.perf_counter()
    result = funkcja(lista)
    end = time.perf_counter()
    return end - start, result

t_bubble, _ = timer(bubble_sort, lista)
t_quick, _ = timer(quick_sort, lista2)
t_merge, lista3_sorted = timer(merge_sort, lista3)
t_insertion, _ = timer(insertion_sort, lista4)


start = time.perf_counter()
lista5.sort()
end = time.perf_counter()
timing=end-start

print("\n--- comparison of sorting algorithms ---")
print(f"{'Algorytm':<20}{'Czas [s]':>10}")
print(f"{'-'*30}")
print(f"{'Bubble Sort':<20}{t_bubble:>10.6f}")
print(f"{'Quick Sort':<20}{t_quick:>10.6f}")
print(f"{'Merge Sort':<20}{t_merge:>10.6f}")
print(f"{'Insertion Sort':<20}{t_insertion:>10.6f}")
print(f"{'Python sort()':<20}{timing:>10.6f}")


result=binary_search(lista5,5)

if result !=-1:
    print(f'szukana wartosc {lista5[result]} na indeksie: {result}')
else:
    print('brak wskazanej liczby w tablicy')



algorytmy = ["Bubble", "Quick", "Merge", "Insertion", "Python sort"]
czasy = [t_bubble, t_quick, t_merge, t_insertion, timing]

plt.bar(algorytmy, czasy)
plt.title("Porownanie algorytmow sortowania")
plt.ylabel("Czas [s]")
plt.show()

