import random


random.seed(40)

data = [random.randint(0, 100) for _ in range(50)]

def devideAndconquer_ascending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return devideAndconquer_ascending(left) + middle + devideAndconquer_ascending(right)

def devideAndConquer_descending(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return devideAndConquer_descending(left) + middle + devideAndConquer_descending(right)
while True:
    print("\nPilih metode sorting untuk Devide And Conquer:")
    print("1. Ascending")
    print("2. Descending")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ").strip()

    if choice == '1':
        print("\nData Asli:", data)  
        sorted_data = devideAndconquer_ascending(data.copy())
        print("Data setelah sorting (Devide And Conquer Secara Ascending):", sorted_data)
    elif choice == '2':
        print("\nData Asli:", data) 
        sorted_data = devideAndConquer_descending(data.copy())
        print("Data setelah sorting (Devide And Conquer Secara Descending):", sorted_data)
    elif choice == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
