peminjaman={
    'pengukur tekanan darah':0,
    'termometer':0,
    'stetostop':0,
    'tensi':0
}

peminjaman['pengukur tekanan darah']+=2
peminjaman['termometer']+=3
peminjaman['stetostop']+=4

# print(peminjaman)

peminjaman['pengukur tekanan darah']-=1
peminjaman['termometer']-=2
peminjaman['stetostop']-=3

peminjaman['tensi']+=2

for alat, jumlah in peminjaman.items():
    print(f'{alat}:{jumlah}')













