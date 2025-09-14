files = [
    {'nama': 'Tugas 1.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Gambar 1.jpg', 'ekstensi': 'jpg'},
    {'nama': 'Tugas 3.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Tugas 2.pdf', 'ekstensi': 'pdf'},
    {'nama': 'Arteri.mp3', 'ekstensi': 'mp3'},
    {'nama': 'gambar 2.jpg', 'ekstensi': 'jpg'},
]

while True:
    print("-" * 50)
    print("MENU SISTEM PENYORTIRAN FILE BERDASARKAN EKSTENSI")
    print("-" * 50)
    print("1. Tambah File")
    print("2. Tampilkan Daftar File")
    print("3. Edit Nama File")
    print("4. Hapus File dari Daftar")
    print("5. Sortir File")
    print("6. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == '1':
        nama = input("Nama File: ")
        ekstensi = nama.split('.')[-1] if '.' in nama else ''
        files.append({'nama': nama, 'ekstensi': ekstensi})
        print("\nFile Berhasil Ditambahkan. Daftar file Sekarang:")
        if not files:
            print("Daftar file kosong.")
        else:
            print("-" * 68)
            print("No | Nama File    | Ekstensi")
            print("-" * 68)
            for index, f in enumerate(files):
                print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
    elif pilih == '2':
        if not files:
            print("Daftar file kosong.")
        else:
            print("-" * 68)
            print("No | Nama File                                          | Ekstensi")
            print("-" * 68)
            for index, f in enumerate(files):
                print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
    elif pilih == '3':
        if not files:
            print("Daftar file kosong.")
        else:
            print("-" * 68)
            print("No | Nama File                                          | Ekstensi")
            print("-" * 68)
            for index, f in enumerate(files):
                print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
            try:
                index = int(input("Pilih nomor file yang ingin diedit: ")) - 1
                if 0 <= index < len(files):
                    nama = input(f"Masukkan Nama baru ({files[index]['nama']}): ")
                    ekstensi = nama.split('.')[-1] if '.' in nama else ''
                    files[index]['nama'] = nama
                    files[index]['ekstensi'] = ekstensi
                    print("\nNama File Berhasil Diperbarui. Daftar file Sekarang:")
                    print("No | Nama File                                          | Ekstensi")
                    print("-" * 68)
                    for idx, f in enumerate(files):
                        print(f"{idx+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
    elif pilih == '4':
        if not files:
            print("Daftar file kosong.")
        else:
            print("-" * 68)
            print("No | Nama File                                          | Ekstensi")
            print("-" * 68)
            for index, f in enumerate(files):
                print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
            try:
                index = int(input("Pilih nomor file yang ingin dihapus: ")) - 1
                if 0 <= index < len(files):
                    files.pop(index)
                    print("\nFile Dihapus dari Daftar. Daftar file Sekarang:")
                    if not files:
                        print("Daftar file kosong.")
                    else:
                        print("No | Nama File                                          | Ekstensi")
                        print("-" * 68)
                        for idx, f in enumerate(files):
                            print(f"{idx+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
                else:
                    print("Pilihan tidak valid.")
            except ValueError:
                print("Input harus berupa angka.")
    elif pilih == '5':
        if not files:
            print("Daftar file kosong.")
        else:
            print("Sortir Berdasarkan Ekstensi (A-Z)")
            sorted_files = sorted(files, key=lambda x: x['ekstensi'])
            print("Daftar file (disortir berdasarkan ekstensi (A-z)):")
            print("-" * 68)
            print("No | Nama File                                          | Ekstensi")
            print("-" * 68)
            for index, f in enumerate(sorted_files):
                print(f"{index+1:<2} | {f['nama']:<50} | {f['ekstensi']}")
    elif pilih == '6':
        print("Program Selesai Terima Kasih.")
        break
    else:
        print("Pilihan tidak valid.")