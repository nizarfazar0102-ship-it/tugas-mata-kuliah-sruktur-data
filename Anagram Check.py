def is_anagram(str1, str2):
    # Menghapus spasi dan mengubah ke huruf kecil
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    # Jika panjang tidak sama, bukan anagram
    if len(s1) != len(s2):
        return False
    
    # Menghitung frekuensi karakter menggunakan dict
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Mengurangi hitungan dengan karakter dari string kedua
    for char in s2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
    
    # Jika semua nilai dict adalah 0, maka anagram
    return all(count == 0 for count in char_count.values())

# Contoh Penggunaan
print(is_anagram("listen", "silent")) # Output: True
print(is_anagram("hello", "world"))   # Output: False
