# Algoritma

Muhammad Alif Risaldy

F55123055

Kelas Informatika B

Best case untuk metode Naive (Bubble Sort) terjadi ketika array sudah terurut dengan urutan yang diinginkan, baik itu secara ascending maupun descending. Dalam kasus ini, pada setiap iterasi, perbandingan elemen-elemen array akan menunjukkan bahwa tidak ada elemen yang perlu ditukar, sehingga tidak ada pertukaran yang dilakukan. Meskipun tidak ada pertukaran, algoritma tetap akan melakukan perbandingan untuk setiap pasangan elemen, yang berarti kompleksitas waktu tetap O(n²), di mana n adalah jumlah elemen dalam array. Namun, jika ada optimasi seperti pengecekan apakah sudah tidak ada pertukaran selama satu iterasi, maka pada best case, algoritma akan berhenti lebih awal, mengurangi jumlah iterasi yang diperlukan dan menjadikan waktu eksekusi lebih cepat.


Best case untuk metode Divide and Conquer, seperti yang diterapkan dalam Quick Sort, terjadi ketika pivot yang dipilih membagi array secara seimbang, menghasilkan dua sub-array yang hampir sama besar pada setiap langkah rekursif. Pembagian yang seimbang ini memastikan bahwa kedalaman rekursi adalah log(n), dan pada setiap tingkat rekursi, perbandingan yang dilakukan adalah n. Dengan demikian, total kompleksitas waktu dalam best case adalah O(n log n), yang menunjukkan efisiensi optimal algoritma ini saat elemen-elemen array dibagi dengan merata pada setiap langkah.
