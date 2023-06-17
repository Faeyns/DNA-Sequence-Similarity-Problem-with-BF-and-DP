import time

def calculate_similarity_BF(dna1, dna2):
    # Menghitung panjang rangkaian DNA
    length1 = len(dna1)
    length2 = len(dna2)
    
    # Inisialisasi variabel untuk menghitung kemunculan karakter yang sesuai dan total pengecekan
    match_count = 0
    total_checks = 0

    # Mulai mengukur waktu eksekusi
    start_time = time.time()

    # Melakukan iterasi sebanyak minimum dari panjang dna1 dan dna2
    for i in range(min(length1, length2)):
        # Menambahkan jumlah total pengecekan
        total_checks += 1
        
        # Memeriksa apakah karakter pada posisi i sama pada kedua rangkaian DNA
        if dna1[i] == dna2[i]:
            # Jika karakter sama, tambahkan ke hitungan karakter yang sesuai
            match_count += 1

    # Menghentikan pengukuran waktu eksekusi
    end_time = time.time()
    
    # Menghitung waktu eksekusi dalam detik
    execution_time = end_time - start_time

    # Menghitung similarity percentage berdasarkan jumlah karakter yang sesuai
    similarity_percentage = (match_count / max(length1, length2)) * 100
    
    # Mengembalikan similarity percentage, match count, total checks, dan execution time
    return similarity_percentage, match_count, total_checks, execution_time

# Contoh penggunaan
dna_sequence1 = "ATCGTACGTGACAGTATCGTACGTTCAGTACGA"
dna_sequence2 = "ATCGTACGTGAGTGACTCATGCATGCATGCATG"

# Memanggil fungsi calculate_similarity_BF dengan dua rangkaian DNA
similarity, match_count, total_checks, execution_time = calculate_similarity_BF(dna_sequence1, dna_sequence2)

# Menampilkan hasil similarity percentage, match count, total checks, dan execution time
print(f"DNA Sequence 1: {dna_sequence1}")
print(f"DNA Sequence 2: {dna_sequence2}")
print(f"Similarity percentage: {similarity}%")
print(f"Match count: {match_count}")
print(f"Total checks: {total_checks}")
print(f"Execution time: {execution_time} seconds")
