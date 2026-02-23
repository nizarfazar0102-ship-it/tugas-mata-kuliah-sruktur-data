def intersection_dua_array(arr1, arr2):
    # 1. Konversi list pertama menjadi set untuk pencarian O(1)
    set1 = set(arr1)
    
    # 2. Gunakan metode intersection bawaan atau list comprehension
    # untuk mencari elemen arr2 yang ada di set1
    result = [x for x in arr2 if x in set1]
    
    # Optional: Jika hasil ingin unik (tanpa duplikat), gunakan set(result)
    return list(set(result))

# Contoh Penggunaan:
array1 = [1, 2, 2, 1, 3, 4]
array2 = [2, 2, 3, 5, 6]

print(intersection_dua_array(array1, array2)) 
# Output: [2, 3] (atau [3, 2] tergantung urutan)
