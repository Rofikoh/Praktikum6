def tambah_data():
    mahasiswa = []
    while True:
        nama = input("Nama: ")
        nim = input("NIM: ")
        nilai_tugas = float(input("Nilai Tugas: "))
        nilai_uts = float(input("Nilai UTS: "))
        nilai_uas = float(input("Nilai UAS: "))

        nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

        mahasiswa.append({
            "Nama": nama,
            "NIM": nim,
            "Nilai Tugas": nilai_tugas,
            "Nilai UTS": nilai_uts,
            "Nilai UAS": nilai_uas,
            "Nilai Akhir": nilai_akhir
        })

        lanjut = input("Tambah data (y/t)? ")
        if lanjut.lower() != 'y':
            break

    return mahasiswa

def tampilkan_data(data):
    print("No\tNama\tNIM\tTugas\tUTS\tUAS\tAkhir")
    for i, mahasiswa in enumerate(data, start=1):
        print(f"{i}\t{mahasiswa['Nama']}\t{mahasiswa['NIM']}\t{mahasiswa['Nilai Tugas']:.2f}\t{mahasiswa['Nilai UTS']:.2f}\t{mahasiswa['Nilai UAS']:.2f}\t{mahasiswa['Nilai Akhir']:.2f}")

if __name__ == "__main__":
    data_mahasiswa = tambah_data()
    tampilkan_data(data_mahasiswa)
