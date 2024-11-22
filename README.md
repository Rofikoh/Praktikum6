# Praktikum6
Tugas Praktikum 6 Mata Kuliah Program Komputer dan Praktek

Program Daftar Nilai Mahasiswa

Program ini digunakan untuk mengelola data mahasiswa, menghitung nilai akhir, dan menampilkan daftar mahasiswa dalam format tabel. berikut perintah programnya :

![Sebelumcooding](https://github.com/user-attachments/assets/b1b3626c-1432-4c29-b521-deee97b19d57)

Fungsi hitung_nilai_akhir
Tujuan

Menghitung nilai akhir mahasiswa berdasarkan nilai tugas, UTS, dan UAS.
Parameter

    nilai_tugas: Nilai tugas mahasiswa (float).
    nilai_uts: Nilai UTS mahasiswa (float).
    nilai_uas: Nilai UAS mahasiswa (float).

Rumus

Nilai akhir dihitung dengan rumus: Akhir = (Tugas * 0.3) + (UTS * 0.35) + (UAS * 0.35)
Return

Mengembalikan nilai akhir yang telah dihitung (float).
Inisialisasi Data

    data_mahasiswa : Menyimpan data mahasiswa dengan NIM sebagai kunci dan informasi mahasiswa (nama, nilai tugas, UTS, UAS, dan nilai akhir) sebagai nilai.

Input Data Mahasiswa

Menggunakan while True untuk membuat loop yang terus berulang hingga pengguna memilih untuk berhenti. Program meminta pengguna untuk memasukkan data mahasiswa dalam format berikut:

    Nama: Nama lengkap mahasiswa.
    NIM: Nomor Induk Mahasiswa.
    Nilai Tugas: Nilai yang diperoleh dari tugas.
    Nilai UTS: Nilai yang diperoleh dari Ujian Tengah Semester.
    Nilai UAS: Nilai yang diperoleh dari Ujian Akhir Semester.

Menggunakan fungsi hitung_nilai_akhir untuk menghitung nilai akhir.
Menyimpan Data

Menyimpan data mahasiswa beserta nilai akhirnya ke dalam dictionary data_mahasiswa dengan NIM sebagai kuncinya.
Menanyakan Tambah Data

Menanyakan kepada pengguna apakah ingin menambahkan data lagi. jika pengguna ingin berhenti, maka loop akan berakhir.
Menampilkan Daftar Mahasiswa

Setelah pengguna memilih untuk tidak menambah data lagi, program menampilkan daftar semua mahasiswa yang telah dimasukkan dalam format tabel. Tabel mencakup:

    No: Nomor urut mahasiswa.
    Nama: Nama lengkap mahasiswa.
    NIM: Nomor Induk Mahasiswa.
    Tugas: Nilai tugas mahasiswa.
    UTS: Nilai Ujian Tengah Semester.
    UAS: Nilai Ujian Akhir Semester.
    Akhir: Nilai akhir yang telah dihitung.

Contoh Output

![Hasilcooding](https://github.com/user-attachments/assets/88b60c60-1149-4524-8c9c-8850520ea6f7)

Flowchart

![flowchart Labspy4 docx](https://github.com/user-attachments/assets/4837afca-b06d-4021-84fd-28d2fa89c43c)
