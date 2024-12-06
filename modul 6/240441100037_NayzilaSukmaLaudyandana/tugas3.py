daftar_barang_darurat = []
daftar_barang_biasa = []
daftar_barang_non_darurat = []

def tambah_barang():
    nama = input("Masukkan Nama Barang: ")
    id_barang = input("Masukkan ID Barang: ")
    prioritas = input("Pilih Tingkat Prioritas (Darurat, Biasa, Non-Darurat): ").lower()
    
    barang = {"Nama": nama, "ID": id_barang, "Prioritas": prioritas}
 
    if prioritas == "darurat":
        daftar_barang_darurat.append(barang)
    elif prioritas == "biasa":
        daftar_barang_biasa.append(barang)
    else:
        daftar_barang_non_darurat.append(barang)

def tampilkan_barang():
    print("\nDaftar Barang yang Telah Diinput:")
    
    for barang in daftar_barang_darurat:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    
    for barang in daftar_barang_biasa:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    
    for barang in daftar_barang_non_darurat:
        print(f"Nama: {barang['Nama']}, ID: {barang['ID']}, Prioritas: {barang['Prioritas']}")
    print()

while True:
    tambah_barang()
    tampilkan_barang()
    
    ulang = input("Apakah ingin menambah barang lagi?: ")
    if ulang != "y" or ulang == "ya":
        break

print("Program selesai.")


import sys 
import time
from time import sleep

def print_lirik():
    baris = [
        ("aku tau kamu hebat", 0.05),
        ("namun selamanya diriku", 0.07),
        ("pasti berkutat", 0.09),
        ("tuk selalu jauhkanmu", 0.05),
        ("dari dunia yang jahat", 0.08),
        ("ini sumpahku padamu", 0.06),
        ("tuk biarkanmu", 0.06),
        ("tumbuh lebih baik", 0.13),
        ("cari panggilanmu", 0.1),
        ("jadi lebih baik", 0.1),
        ("dibanding diriku", 0.1),
        (",,,", 0,1),
    ]

    jeda = [1.1, 0.4, 1.7, 0.2, 1.5, 0.4, 0.5, 0.8, 0.8,
            0.8, 0.1]

    for i, (line, char_jeda) in enumerate(baris):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)
        print('')
        sleep(jeda[i])

    print_lirik()

