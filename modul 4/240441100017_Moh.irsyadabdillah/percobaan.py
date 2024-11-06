# list_angka = [3,4,5,6,7]
# print(list_angka)
# for i in list_angka:
#     print(i)
from datetime import datetime

# Inisialisasi daftar to-do list
daftar_item = []

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== Menu ===")
    print("1. Tambah item")
    print("2. Lihat Daftar item")
    print("3. Hapus item")
    print("4. Tandai item yang sudah di beli")
    print("5. Keluar")

# Fungsi untuk menambah tugas dengan jadwal
def tambah_item():
    tugas = input("Masukkan item: ")
    waktu = input("Masukkan jadwal (format HH:MM): ")
    try:
        # Memvalidasi format waktu
        jadwal = datetime.strptime(waktu, "%H:%M")
        daftar_item.append({"tugas": tugas, "selesai": False, "jadwal": jadwal})
        print("item berhasil ditambahkan!")
    except ValueError:
        print("Format waktu tidak valid. Gunakan format HH:MM.")

# Fungsi untuk melihat daftar tugas yang diurutkan sesuai jadwal
def lihat_item():
    if not daftar_item:
        print("Tidak ada tugas dalam daftar.")
    else:
        # Mengurutkan daftar tugas berdasarkan jadwal
        daftar_tugas_terurut = sorted(daftar_item, key=lambda x: x["jadwal"])
        print("\nDaftar Tugas (diurutkan berdasarkan jadwal):")
        for i, item in enumerate(daftar_tugas_terurut, start=1):
            status = "Selesai" if item["selesai"] else "Belum selesai"
            waktu_str = item["jadwal"].strftime("%H:%M")
            print(f"{i}. {item['tugas']} - {waktu_str} - {status}")

# Fungsi untuk menghapus tugas
def hapus_item():
    lihat_item()
    try:
        nomor_tugas = int(input("Masukkan nomor item yang ingin dihapus: "))
        if 1 <= nomor_tugas <= len(daftar_item):
            tugas_dihapus = daftar_item.pop(nomor_item - 1)
            print(f"Tugas '{tugas_dihapus['tugas']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid, masukkan nomor tugas.")

# Fungsi untuk menandai tugas selesai
def tandai_item_selesai():
    lihat_item()
    try:
        nomor_tugas = int(input("Masukkan nomor tugas yang selesai: "))
        if 1 <= nomor_tugas <= len(daftar_item):
            daftar_item[nomor_tugas - 1]["selesai"] = True
            print("Tugas berhasil ditandai sebagai selesai.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input tidak valid, masukkan nomor tugas.")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_tugas()
    elif pilihan == "2":
        lihat_item()
    elif pilihan == "3":
        hapus_item()
    elif pilihan == "4":
        tandai_item_selesai()
    elif pilihan == "5":
        print("Keluar dari program. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih lagi.")










