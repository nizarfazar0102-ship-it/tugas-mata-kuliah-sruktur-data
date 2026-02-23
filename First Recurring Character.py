def find_first_recurring_char(string):
    # Set digunakan untuk menyimpan karakter yang sudah pernah dilihat
    seen_characters = set()
    
    for char in string:
        # Jika karakter sudah ada di dalam set, ini adalah yang pertama berulang
        if char in seen_characters:
            return char
        # Jika belum, tambahkan karakter ke dalam set
        seen_characters.add(char)
        
    # Mengembalikan None jika tidak ada karakter yang berulang
    return None

# Contoh Penggunaan:
input_str = "bcaba"
result = find_first_recurring_char(input_str)
print(f"Input: {input_str}")
print(f"Karakter berulang pertama: {result}") # Output: b
