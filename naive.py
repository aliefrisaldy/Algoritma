import random

random.seed(40)

data = [random.randint(0, 100) for _ in range(50)]

def naive_ascending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def naive_descending(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


while True:
    print("\nPilih metode sorting untuk Naive:")
    print("1. Ascending")
    print("2. Descending")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ").strip()

    if choice == '1':
        print("\nData Asli:", data)  
        sorted_data = naive_ascending(data.copy())
        print("Data setelah sorting (Naive Secara Ascending):", sorted_data)
    elif choice == '2':
        print("\nData Asli:", data) 
        sorted_data = naive_descending(data.copy())
        print("Data setelah sorting (Naive Secara Descending):", sorted_data)
    elif choice == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
