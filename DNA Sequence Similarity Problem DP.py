import time

def calculate_similarity(dna1, dna2):
    # Menghitung panjang rangkaian DNA
    length1 = len(dna1)
    length2 = len(dna2)
    
    # Inisialisasi variabel untuk menghitung kemunculan karakter yang sesuai dan total pengecekan
    match_count = 0
    total_checks = 0

    # Buat matriks dua dimensi dengan ukuran (length1 + 1) x (length2 + 1)
    matrix = [[0] * (length2 + 1) for _ in range(length1 + 1)]

    # Mulai mengukur waktu eksekusi
    start_time = time.time()

    # Isi matriks dengan pendekatan bottom-up
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            # Menambahkan jumlah total pengecekan
            total_checks += 1
            
            if dna1[i - 1] == dna2[j - 1]:
                # Jika karakter pada posisi i-1 sama dengan karakter pada posisi j-1, tambahkan 1 ke panjang LCS
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                # Juga tambahkan 1 ke hitungan karakter yang sesuai
                match_count += 1
            else:
                # Jika karakter tidak sama, ambil nilai maksimum dari atas atau kiri sebagai panjang LCS
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    # Menghentikan pengukuran waktu eksekusi
    end_time = time.time()
    # Menghitung waktu eksekusi dalam detik
    execution_time = end_time - start_time

    # Menghitung panjang Longest Common Subsequence (LCS) dari kedua rangkaian DNA
    lcs_length = matrix[length1][length2]

    # Menghitung persentase kesamaan berdasarkan panjang LCS
    similarity_percentage = (lcs_length / max(length1, length2)) * 100

    # Mengembalikan similarity percentage, match count, total checks, dan execution time
    return similarity_percentage, match_count, total_checks, execution_time

# Contoh penggunaan
dna_sequence1 = "ATCGTACGTGACAGTATCGTACGTTCAGTACGA"
dna_sequence2 = "ATCGTACGTGAGTGACTCATGCATGCATGCATG"

# Memanggil fungsi calculate_similarity dengan dua rangkaian DNA
similarity, match_count, total_checks, execution_time = calculate_similarity(dna_sequence1, dna_sequence2)

# Menampilkan hasil similarity percentage, match count, total checks, dan execution time
print(f"DNA Sequence 1: {dna_sequence1}")
print(f"DNA Sequence 2: {dna_sequence2}")
print(f"Similarity percentage: {similarity}%")
print(f"Match count: {match_count}")
print(f"Total checks: {total_checks}")
print(f"Execution time: {execution_time} seconds")
