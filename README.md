# tugas-mata-kuliah-sruktur-data

Penjelasan Metode Deduplikasi:
1.	set() (seen): Menggunakan set untuk mengecek apakah suatu elemen sudah pernah muncul atau belum. Pengecekan ini sangat cepat (O(1) dibandingkan mengecek di dalam list (O(n).
2.	list() (unique_list): Menyimpan urutan elemen yang unik.
3.	Order Preserved: Elemen yang pertama kali muncul akan dipertahankan, dan duplikat berikutnya akan diabaikan.

Penjelasan Metode Intersection Dua Array :
1.	set(arr1): Mengonversi arr1 menjadi set (himpunan) membutuhkan waktu (O(n). Set di Python menggunakan hash table, yang membuat pengecekan apakah suatu elemen ada di dalamnya (member check) menjadi (O(1) 
 (konstan).
2.	for x in arr2 if x in set1: Iterasi melalui arr2 (waktu O(m) dan mengecek keberadaan setiap elemen di set1 (0(1).
3.	Total Waktu: O(n+m), jauh lebih cepat daripada menggunakan loop bersarang (nested loop) O(n x m)

Penjelasan Anagram Check:
1.	Fungsi ini membersihkan string dari spasi dan mengubahnya menjadi huruf kecil agar pengecekan konsisten.
2.	Dictionary (char_count) menyimpan karakter sebagai kunci dan jumlah kemunculannya sebagai nilai.
3.	Kedua string dibandingkan frekuensi karakternya; jika sama persis, maka anagram

Penjelasan First Recurring Character:
1.	seen_characters = set(): Membuat set kosong. Set dipilih karena pencarian (char in seen_characters) memiliki kecepatan rata-rata O(1), menjadikannya sangat efisien.
2.	for char in string:: Mengulang string karakter demi karakter dari kiri ke kanan.
3.	if char in seen_characters:: Mengecek apakah karakter saat ini sudah pernah muncul sebelumnya.
4.	return char: Mengembalikan karakter tersebut segera setelah ditemukan ulang.
5.	seen_characters.add(char): Jika belum berulang, karakter ditambahkan ke set. 
Contoh dengan "google":
•	'g': tidak ada di set -> set: {'g'}
•	'o': tidak ada di set -> set: {'g', 'o'}
•	'o': ada di set -> kembalikan 'o'.

Cara Kerja Program Simulasi Buku Telepon:
1.	buku_telepon = {}: Program menginisialisasi dictionary kosong untuk menyimpan kontak (Nama: Nomor).
2.	tambah_kontak: Menambahkan pasangan key:value baru ke dalam dictionary.
3.	lihat_kontak: Mengiterasi (loop) dictionary dan menampilkan semua entri.
4.	cari_kontak: Mencari nomor berdasarkan nama (key) yang diinput pengguna.
5.	hapus_kontak: Menghapus data dari dictionary menggunakan del.
6.	main(): Loop utama yang terus berjalan menampilkan menu hingga pengguna memilih opsi 5 (Keluar).

