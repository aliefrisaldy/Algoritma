
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

 
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


def analisis_algoritma_pengurutan(nama_algoritma):
    if nama_algoritma == "Merge Sort":
        print("\n--- Analisis Merge Sort ---")
        print("1. Worst Case (Kasus Terburuk):")
        print("   -Kompleksitas: O(n log n)")
        print("   -Penjelasan: Merge Sort selalu membagi array menjadi dua bagian yang sama besar dan melakukan penggabungan (merge) pada setiap langkah.")
        print("2. Best Case (Kasus Terbaik):")
        print("   -Kompleksitas: O(n log n)")
        print("   -Penjelasan: Bahkan jika array sudah diurutkan, Merge Sort tetap membagi array menjadi dua bagian dan melakukan penggabungan.")
        print("3. Average Case (Kasus Rata-rata):")
        print("   -Kompleksitas: O(n log n)")
        print("   -Penjelasan: Karena algoritma selalu melakukan pembagian dan penggabungan secara rekursif.")
    elif nama_algoritma == "Quick Sort":
        print("\n--- Analisis Quick Sort ---")
        print("1. Worst Case (Kasus Terburuk):")
        print("   -Kompleksitas: O(n²)")
        print("   -Penjelasan: Kasus terburuk terjadi ketika elemen pivot selalu menjadi elemen terkecil atau terbesar di array.")
        print("2. Best Case (Kasus Terbaik):")
        print("   -Kompleksitas: O(n log n)")
        print("   -Penjelasan: Kasus terbaik terjadi ketika pivot selalu membagi array menjadi dua bagian yang sama besar.")
        print("3. Average Case (Kasus Rata-rata):")
        print("   -Kompleksitas: O(n log n)")
        print("   -Penjelasan: Dalam rata-rata, pemilihan pivot menghasilkan pembagian yang cukup seimbang.")


if __name__ == "__main__":
    # Data input
    X = [1, 5, 6, 4, 3, 3, 7, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    print("Data Awal:", X) 

  
    merge_sorted = X.copy()
    print("\n--- Merge Sort ---")
    print("Sebelum Diurutkan:", merge_sorted)
    merge_sort(merge_sorted)
    print("Setelah Diurutkan:", merge_sorted)

    print("\n--- Quick Sort ---")
    quick_sorted = X.copy()
    print("Sebelum Diurutkan:", quick_sorted)
    quick_sorted = quick_sort(quick_sorted)
    print("Setelah Diurutkan:", quick_sorted)

    while True:
        print("\nPilih Hasil Analisis Algoritma Sorting Untuk Worst Case, Best Case, Dan Avarage Case:")
        print("1. Merge Sort")
        print("2. Quick Sort")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan Anda (1/2/3): ")

        if pilihan == "1":
            analisis_algoritma_pengurutan("Merge Sort")
        elif pilihan == "2":
            analisis_algoritma_pengurutan("Quick Sort")
        elif pilihan == "3":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
