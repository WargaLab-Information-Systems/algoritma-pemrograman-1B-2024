def Menghitung_deret_Aritmatika():
    # Informasi yang diberikan
    suku_ke_5 = 11  # Suku ke-5
    jumlah_suku_8_12 = 52  # Jumlah suku ke-8 dan ke-12

    # Langkah 1: Buat persamaan
    # 1. Suku ke-5: a + 4d = 11
    # 2. Suku ke-8: a + 7d
    # 3. Suku ke-12: a + 11d
    # 4. a + 7d + a + 11d = 52  => 2a + 18d = 52

    # Langkah 2: Selesaikan sistem persamaan
    # Dari suku ke-5: a = 11 - 4d
    # Substitusi ke persamaan kedua: 2(11 - 4d) + 18d = 52
    # 22 - 8d + 18d = 52
    # 10d = 52 - 22
    # 10d = 30
    d = 30 / 10  # Dapatkan nilai d
    a = suku_ke_5 - 4 * d  # Dapatkan nilai a

    # Langkah 3: Temukan jumlah nilai 8 suku pertama
    jumlah_suku_pertama_8 = (8 / 2) * (2 * a + (8 - 1) * d)

    # Cetak hasil
    print("Suku pertama:", a)
    print("Beda:", d)
    print("Jumlah nilai 8 suku pertama:", jumlah_suku_pertama_8)

Menghitung_deret_Aritmatika()