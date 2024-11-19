# def cek_palindrom(kata):
#     kata = kata.replace(" ", "").lower()
    
#     return kata == kata[::-1]

# kata = input("masukkan kata:")

# print(f"kata:{kata} adalah palindrom: {cek_palindrom(kata)}")

# murit = {
#     "nama":"udin",
#     "umur": 18,
#     "kota":"bandung",
#     "favcolor": ["yellow","red","blue"],
#     "ppp":True
# }
# print(murit)
# print(murit["favcolor"][0])
# print(murit)
siswa = {
    "001": {
        "nama": "Andi",
        "umur": 17,
        "nilai": {
            "matematika": 85,
            "bahasa_indonesia": 90,
            "bahasa_inggris": 88
        }
    },
    "002": {
        "nama": "Budi",
        "umur": 16,
        "nilai": {
            "matematika": 78,
            "bahasa_indonesia": 80,
            "bahasa_inggris": 85
        }
    },
    "003": {
        "nama": "Citra",
        "umur": 17,
        "nilai": {
            "matematika": 92,
            "bahasa_indonesia": 89,
            "bahasa_inggris": 94
        }
    },
    "004": {
        "nama": "bintang",
        "umur": 20,
        "nilai": {
            "matematika": 95,
            "bahasa_indonesia": 80,
            "bahasa_inggris": 100
        }
    }
}

# Akses data dari dictionary bersarang
# Misalnya, kita ingin mengambil nilai Bahasa Inggris dari siswa dengan ID "002"
nilai_bahasa_inggris_budi = siswa["002"]["nilai"]["bahasa_inggris"]
nilai_bahasa_inggris_citra = siswa["003"]["nilai"]["bahasa_inggris"]
nilai_bahasa_inggris_Andi = siswa["001"]["nilai"]["bahasa_inggris"]
nilai_bahasa_inggris_bintang = siswa["004"]["nilai"]["bahasa_inggris"]
print("Nilai Bahasa Inggris Andi:", nilai_bahasa_inggris_Andi)
print("Nilai Bahasa Inggris Budi:", nilai_bahasa_inggris_budi)
print("Nilai Bahasa Inggris citra:", nilai_bahasa_inggris_citra)
print("Nilai Bahasa Inggris bintang:", nilai_bahasa_inggris_bintang)


