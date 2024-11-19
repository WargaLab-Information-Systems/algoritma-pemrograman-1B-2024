# # # membuat dictionary 
# # siswa = {
# #     "nama" : "budi",
# #     "umur" : 17,
# #     "kelas" : "10A",
# #     "favoritColor" : ["yellow", "red", "blue"],
# #     "pppp" : True
# # }

# # # mengubah data 
# # siswa['kelas'] = "11A"
# # print(siswa["kelas"])

# # # gatauu 
# # print(siswa["favoritColor"][0])
# # print(siswa["umur"])
# # print(siswa["pppp"])

# # # menambah data 
# # siswa["sekolah"] = "smas antartika"
# # print(siswa["sekolah"])

# # # menghapus data 
# # del siswa ["pppp"]
# # print(siswa)

# # # dictionary bersarang  
# # siswa1 = {
# #     "nama" : "jeno",
# #     "umur" : 16,
# #     "nilai" :{
# #         "Matematika" : 80,
# #     }
# # }

# # print(siswa1["nilai"]["Matematika"])

# # # menambah data
# # siswa1["nilai"]["ipa"] : 80
# # print(siswa1["nilai"])
# # print(siswa1)

# # HIMPUNAN SET 
# buah = {"apel", "jeruk", "mangga",12, True, 155.5}
# print("")
# print(buah)

# # menambah data 
# buah.add(22)
# print(buah)

# # mengahapus data
# buah.remove("mangga")
# print(buah)

# # update data



# dict = {'name' : 'jeno', 'age' : 20, 'class' : 'second'}
# print("dict['name] : ", dict['name'])
# print("dict['age] : ", dict['age'])

# # update dictionary
# dict = {'name' : 'jeno', 'age' : 20, 'class' : 'second'}
# dict['age'] = 23;
# dict['school'] = "ABC School"

# print("dict['age'] : ", dict['age'])
# print("dict['school'] : ", dict['school'])

# # menghapus elemen Dictionary 
# dict = {'name' : 'jeno', 'age' : 20, 'class' : 'second'}
# del dict['name']
# dict.clear()
# del dict

# print("dict['age'] : ", dict['age'])
# print("dict['school'] : ", dict['school'])


# angka1 = {1, 2, 3}
# angka2 = {3, 4, 5}
# angka3 = angka1.difference(angka2)
# print(angka3)

angka1 = {1, 2, 3}
angka2 = {3, 4, 5}
angka3 = angka1.symmetric_difference(angka2)
print(angka3)
