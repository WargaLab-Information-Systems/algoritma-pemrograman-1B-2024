prioritas = {
    "darurat" : 3,
    "biasa" : 2,
    "non-darurat" : 1
}

data_barang = [
    # id_barang, nama_barang, prioritas
]

def show_data_barang():
    print("Data Barang:")
    print("+----+" + "-" * 20 + "+" + "-" * 30 + "+")
    print("| ID | \tNama Barang\t  | Prioritas\t\t\t |")
    print("+----+" + "-" * 20 + "+" + "-" * 30 + "+")
    for data in data_barang:
        print(f"|{str(data[0]).center(3)} | {data[1].ljust(18)} | {data[2].ljust(28)} |")
    print("+----+" + "-" * 20 + "+" + "-" * 30 + "+")

def bubble_sort(data_barang, prioritas):
    n = len(data_barang)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            prioritas_1 =  prioritas[data_barang[j][2]]
            prioritas_2 =  prioritas[data_barang[j + 1][2]]
            if prioritas_1 < prioritas_2:
                data_barang[j], data_barang[j + 1] = data_barang[j + 1], data_barang[j]

def main():
    print("Prgram pengelola barang")
    while True:
        print("Input Data Barang")
        id_barang = int(input("Masukkan ID Barang: "))
        nama_barang = input("Masukkan Nama Barang: ")
        prioritas_barang = input("Masukkan Prioritas Barang (darurat/biasa/non-darurat): ")
        if prioritas_barang not in prioritas.keys():
            print("Prioritas tidak valid. Silakan masukkan prioritas yang benar.")
            print("=" * 100)
            continue

        data_barang.append((id_barang, nama_barang, prioritas_barang))

        bubble_sort(data_barang, prioritas)
        show_data_barang()

        print("=" * 100)
        if input("Tambah data lagi? (y/n): ") != "y":
            break
        print("=" * 100)

if __name__ == "__main__":
    main()