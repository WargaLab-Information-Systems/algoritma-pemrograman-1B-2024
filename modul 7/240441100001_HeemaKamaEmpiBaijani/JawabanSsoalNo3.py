import os

"""
    |--------------------------------------------------------------------------
    | Pertanyaan
    |--------------------------------------------------------------------------
    |
    | Sebuah lembaga bimbingan intensif Gema Ripah hanya menyediakan kursi 3 orang
    | siswa di setiap kelasnya. Apabila terdapat siswa yang melebihi 3 dan kelipatannya
    | akan dibukakan sebuah kelas baru. Untuk keperluan absensi, dibutuhkan nama, kelas,
    | asal sekolah dan plotting bimbingan intensif. Bantulah Sujin sebagai staff
    | administrasi untuk mengelompokkan siswa berdasarkan data tersebut, sehingga
    | selain staff administrasi dan pengajar dapat mengetahui nama-nama siswa yang ada
    | di plotting bimbingan tersebut! (program diinputkan secara dinamis untuk setiap
    | data yang ada dan mengandung CRUD)
    |
    |
    |
"""
# setiap kelas ada 3 kursi
# akan dibuatkan kelas baru jika kelebihan 3 siswa
# data yang dibutuhkan absensi: nama, kelas, asal sekolah, plotting bimbingan intensif

"""
Schema

classrooms = {
    id_kelas: {
        id_siswa: [int, int, int],
        plotting: str | None
    },
    ...
}

students = [
     {
        id_siswa: int
        nama: str,
        id_kelas: id_kelas | None,
        asal_sekolah: str,
    },
    ...
]
"""


classrooms = {
    0: {
        'id_siswa': [0],
        'plotting': None
    },
}

students = [
    {
        "id_siswa": 0,
        "nama": "John Doe",
        "id_kelas": 0,
        "asal_sekolah": "SMA 1 Jakarta",
    }
]

error = {
    "show": False,
    "message": ""
}

def update_error(show=False, message=None):
    error["show"] = show
    error["message"] = message

def tambah_siswa(student):
    """Tambah Siswa

    Args:
        student: {'nama': str, 'asal_sekolah': str}
    """
    # buat id siswa baru
    new_id_student = 0 if len(students) == 0 else max(students, key=lambda student: student['id_siswa'])['id_siswa'] + 1
    student["id_siswa"] = new_id_student
    # cek apakah kelas sudah penuh atau belum
    last_id_classroom = 0 if len(classrooms) == 0 else max(classrooms.keys())
    # print(len(classrooms[last_id_classroom]))
    if len(classrooms[last_id_classroom]["id_siswa"]) < 3:
        # jika belum penuh, tambahkan siswa ke kelas tersebut
        classrooms[last_id_classroom]['id_siswa'].append(new_id_student)
        student["id_kelas"] = last_id_classroom
        students.append(student)
    else:
        # jika sudah penuh, buat kelas baru dan tambahkan siswa ke kelas tersebut
        new_id_classroom = max(classrooms.keys()) + 1
        classrooms[new_id_classroom] = {'id_siswa': [new_id_student], 'plotting': None}
        student["id_kelas"] = new_id_classroom
        students.append(student)

def hapus_siswa(student_id):
    """Hapus Siswa

    Args:
        student_id: int
    """
    # validasi args
    if student_id not in [student['id_siswa'] for student in students]:
        update_error(True, "ID tidak valid")
        return
    # cari kelas siswa tersebut
    for id_classroom, data in classrooms.items():
        if student_id in data['id_siswa']:
            # hapus siswa dari kelas tersebut
            data['id_siswa'].remove(student_id)
            # hapus siswa dari data siswa
            for student in students:
                if student['id_siswa'] == student_id:
                    students.remove(student)
                    break

def hapus_kelas(classroom_id):
    """Hapus Kelas
    Args:
    	classroom_id: int
    """
    # validasi args
    if len(classrooms.keys()) == 1:
        update_error(True, "Gagal menghapus kelas, pastikan terdapat dua atau lebih kelas yang tersisa")
        return
    elif classroom_id not in classrooms:
        update_error(True, "ID tidak valid")
        return
    else:
        pass
    # hapus kelas dari data kelas
    del classrooms[classroom_id]
    # hapus siswa dari data siswa
    for student in students:
        if student['id_kelas'] == classroom_id:
            students.remove(student)

def update_siswa(student_id, new_data={}, id_kelas=None):
    """Update Siswa
    Args:
    	student_id: int
        new_data: {'nama'?: str | , 'asal_sekolah'?: str}
        id_kelas: int | None
    """
    # Validasi args
    if id_kelas is not None and id_kelas not in classrooms:
        update_error(True, "ID kelas tidak valid")
        return
    elif id_kelas is not None and len(classrooms[id_kelas]["id_siswa"]) == 3:
        update_error(True, "Kelas sudah penuh, silahkan pilih kelas lain")
        return
    elif student_id not in [student['id_siswa'] for student in students]:
        update_error(True, "ID siswa tidak valid")
        return
    elif new_data == {} and id_kelas is None:
        update_error(True, "Tidak ada perubahan data")
        return

    # cari siswa tersebut
    for student in students:
        if student['id_siswa'] == student_id:
            # update data siswa tersebut
            if id_kelas is not None:
                # pindah kelas
                if student['id_kelas'] is not None:
                    classrooms[student['id_kelas']]["id_siswa"].remove(student_id)
                classrooms[id_kelas]["id_siswa"].append(student_id)
                new_data["id_kelas"] = id_kelas
            student.update(new_data)

def update_plotting(classroom_id, plotting):
    """Update Plotting Kelas
    Args:
    	classroom_id: int
        plotting: str
    """
    # Validasi args
    if classroom_id not in classrooms:
        update_error(True, "ID kelas tidak valid")
        return

    # update plotting kelas tersebut
    classrooms[classroom_id]["plotting"] = plotting

def show_data():
    """Menampilkan data siswa dan kelas"""
    print("Data Kelas:")
    print("+" + "-" * 12 + "+" + "-" * 14 + "+" + "-" * 20 + "+")
    print("| {:^10} | {:^10} | {:^18} |".format("ID Kelas", "Jumlah siswa", "Plotting"))
    print("+" + "-" * 12 + "+" + "-" * 14 + "+" + "-" * 20 + "+")
    for id_classroom, data in classrooms.items():
        print("|" + str(id_classroom).center(12) + "|" + str(len(data['id_siswa'])).center(14) + "|" + str(data['plotting']).center(20) + "|")
    print("+" + "-" * 12 + "+" + "-" * 14 + "+" + "-" * 20 + "+")

    print()
    print("Data Siswa:")
    print("+" + "-" * 12 + "+" + "-" * 27 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")
    print("| {:^10} | {:^25} | {:^18} | {:^20} |".format("ID Siswa", "Nama", "ID Kelas", "Asal Sekolah"))
    print("+" + "-" * 12 + "+" + "-" * 27 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")
    for student in students:
        print("|" + str(student['id_siswa']).center(12) + "|" + str(student['nama']).center(27) + "|" + str(student['id_kelas']).center(20) + "|" + str(student['asal_sekolah']).center(22) + "|")
    print("+" + "-" * 12 + "+" + "-" * 27 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")

    print()
    print("Data Absensi:")
    print("+" + "-" *27 + "+" + "-" * 12 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")
    print("| {:^25} | {:^10} | {:^18} | {:^20} |".format("Nama", "Kelas", "Asal Sekolah", "Plotting"))
    print("+" + "-" * 27 + "+" + "-" * 12 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")
    for student in students:
        if student['id_kelas'] is not None:
            print("|" + str(student['nama']).center(27) + "|" + str(student['id_kelas']).center(12) + "|" + str(student['asal_sekolah']).center(20) + "|" + str(classrooms[student['id_kelas']]['plotting']).center(22) + "|")
    print("+" + "-" * 27 + "+" + "-" * 12 + "+" + "-" * 20 + "+"  + "-" * 22 + "+")
    print()


def main():
    while True:
        os.system("clear")
        if error["show"]:
            print(error["message"])
            update_error(False)
        show_data()
        print("Menu:")
        print("1. Tambah Siswa")
        print("2. Update Siswa")
        print("3. Hapus Siswa")
        print("4. Hapus Kelas")
        print("5. Update Plotting Kelas")
        print("0. Keluar")

        inp = int(input("Masukan pilihan:"))

        # Tambah Siswa
        if inp == 1:
            nama = input("Masukan nama siswa:")
            asal_sekolah = input("Masukan asal sekolah siswa:")
            tambah_siswa({"nama": nama, "asal_sekolah": asal_sekolah})
        elif inp == 2:
            student_id = int(input("Masukan ID siswa:"))
            nama = input("Masukan nama siswa: ")
            asal_sekolah = input("Masukan asal sekolah siswa: ")
            id_kelas = input("Masukan ID kelas atau tekan enter untuk melewati: ") or None
            id_kelas = int(id_kelas) if id_kelas is not None else None
            update_siswa(student_id, {"nama": nama, "asal_sekolah": asal_sekolah}, id_kelas )
        elif inp == 3:
            student_id = int(input("Masukan ID siswa:"))
            hapus_siswa(student_id)
        elif inp == 4:
            id_kelas = int(input("Masukan ID kelas:"))
            hapus_kelas(id_kelas)
        elif inp == 5:
            id_kelas = int(input("Masukan ID kelas:"))
            plotting = input("Masukan plotting kelas:")
            update_plotting(id_kelas, plotting)
        elif inp == 0:
            break
        else:
            update_error(True, "Pilihan tidak valid")
            continue

if __name__ == "__main__":
    main()
