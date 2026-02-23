def remove_duplicates(input_list):
    # Set digunakan untuk melacak elemen yang sudah dilihat (kompleksitas O(1))
    seen = set()
    # List baru untuk menyimpan elemen unik
    unique_list = []
    
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

# Contoh Penggunaan:
data = [1, 2, 2, 3, 4, 1, 5, 3]
hasil = remove_duplicates(data)
print(hasil) # Output: [1, 2, 3, 4, 5]
