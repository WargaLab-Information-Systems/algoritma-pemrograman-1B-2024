# siswa = {
#     "nama" : "arif",
#     "umur" : 18,
#     "kelas" : "10A",
#     "FavoriteColor" : ["blue,yellow,red"]
# }
# print(siswa["umur"])
# print(siswa["FavoriteColor"][0])

# # print(siswa[""])
# siswa["nama"] = "abi"

# print(siswa["nama"])

# #delete
# del siswa["umur"]
# print(siswa)

# #dictionary bersarang

# siswa1 = {
#     "nama" : "ariffur",
#     "kelas" : "XII RPL",
#     "nilai" :{
#         "matematika" : 80,
#         "agama" : 99
#     }
# }
# print(siswa1)

# dict1 = {'apel': 5, 'banana': 3}
# dict2 = {'banana': 6, 'orange': 4}
# dict.update(dict2)
# print(dict2)

my_dict = {'apple': 5, 'banana': 3}
print{my_dict.get('orange', 'key not found')}