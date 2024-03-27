from prettytable import PrettyTable

listmenu = [
    ['A1', 'Bagas', 'Direktur', 'Bekasi', 32],
    ['A2', 'Dio', 'Staff', 'Jawa', 23],
    ['A3', 'Hanggoro', 'Manager', 'Medan', 25],
    ['A4', 'Sri', 'Analyst', 'Surabaya', 29],
    ['A5', 'Tatang', 'Developer', 'Bandung', 27]
    
    ]



#sub menu

def menampilkan_daftar_karyawan():
    while True:  # Loop utama untuk menjaga agar submenu terus ditampilkan
        print('Daftar Menu\n')
        print('''Sub Menu menampilkan daftar karyawan
                1. Menampilkan Nama Karyawan
                2. Cari NIK Karyawan
                3. Kembali Ke Menu Utama''')
        read = input('Masukkan Nomor Sub Menu :  ')
        if read == '1':
            if listmenu:  # Kondisi untuk mengecek apakah listmenu tidak kosong
                table = PrettyTable(['Index', 'NIK', 'Nama', 'Posisi', 'Alamat', 'Umur'])
                for idx, data in enumerate(listmenu, start=1):
                    table.add_row([idx] + data)
                print(table)
            else:
                print('Data kosong')  # Pesan ketika listmenu kosong
        elif read == '2':
            if listmenu:  # Kondisi untuk mengecek apakah listmenu tidak kosong
                by_id = input('Masukkan NIK Karyawan yang Ingin Anda Cari :  ')
                found = False
                for data in listmenu:
                    if data[0] == by_id:
                        table = PrettyTable(['ID Karyawan', 'Nama', 'Posisi', 'Alamat', 'Umur'])
                        table.add_row(data[:5])
                        print(table)
                        found = True
                        break  # Break setelah menemukan karyawan dengan NIK yang dicari
                if not found:
                    print('NIK Karyawan tidak tersedia')  # Pesan ketika NIK karyawan tidak ditemukan
            else:
                print('Data kosong')  # Pesan ketika listmenu kosong
        elif read == '3':
            break  # Break setelah memilih untuk kembali ke menu utama
        else:
            print('Angka yang Anda masukkan tidak valid')  # Pesan ketika input tidak valid



# menambah karyawan

def menambah_Karyawan():
    # Loop utama, menjalankan menu untuk menambahkan karyawan atau kembali ke menu utama
    while True:
        print('''
        Sub Menu Menambah Daftar Karyawan               
        1. Menambah Karyawan
        2. Kembali Ke Menu Utama      
        ''')
        read = input('Masukkan Nomor Yang Ingin Dipilih :  ')
        try:
            if read == '1':
                # Loop untuk memastikan NIK karyawan baru unik dan sesuai dengan kriteria
                while True:
                    # Meminta pengguna untuk memasukkan NIK Karyawan
                    primarykey = input('Masukkan NIK Karyawan : ')
                    # Memeriksa apakah NIK memiliki panjang maksimal 8 karakter dan hanya terdiri dari huruf dan angka
                    if len(primarykey) <= 8 and primarykey.isalnum():  
                        # Inisialisasi variabel untuk memeriksa apakah NIK sudah ada dalam listmenu
                        nik_exists = False
                        # Memeriksa setiap data karyawan dalam listmenu
                        for data in listmenu:
                            # Jika NIK yang dimasukkan pengguna sudah ada dalam listmenu, set nik_exists menjadi True
                            if data[0] == primarykey:
                                nik_exists = True
                                break # Jika kondisi NIK sudah True
                        # Jika NIK yang dimasukkan pengguna belum ada dalam listmenu, keluar dari loop saat ini
                        if not nik_exists:
                            break  # Keluar dari loop saat NIK karyawan valid dan tidak ada yang sama
                        else:
                            # Jika NIK yang dimasukkan pengguna sudah ada dalam listmenu, tampilkan pesan kesalahan
                            print("NIK sudah ada. Harap masukkan NIK yang berbeda.")
                    else:
                        print("NIK harus terdiri dari maksimal 8 karakter, hanya huruf dan angka.")  # Pesan jika NIK tidak sesuai kriteria
                
                # Loop untuk memastikan nama karyawan sesuai dengan kriteria
                while True:
                    namakaryawan = input('Masukkan Nama Karyawan : ')
                    if len(namakaryawan) <= 20 and namakaryawan.isalpha():  
                        break  # Keluar dari loop saat nama karyawan valid
                    else:
                        print("Nama harus terdiri dari maksimal 20 huruf dan tidak boleh mengandung angka.")  # Pesan jika nama tidak sesuai kriteria
                
                jabatankaryawan = input('Masukan Jabatan Karyawan : ')
                alamatkaryawan = input('Masukan Alamat Karyawan : ')
                
                # Loop untuk memastikan umur karyawan sesuai dengan kriteria
                while True:
                    umurkaryawan = input('Masukan Umur Karyawan : ')
                    if umurkaryawan.isdigit() and len(umurkaryawan) == 2:  
                        umurkaryawan = int(umurkaryawan)
                        if 18 <= umurkaryawan <= 45:  
                            break  # Keluar dari loop saat umur karyawan valid
                        else:
                            print("Umur harus berada dalam rentang 18-45 tahun.")  # Pesan jika umur tidak sesuai kriteria
                    else:
                        print("Umur harus berupa 2 angka.")  # Pesan jika umur tidak sesuai kriteria
                
                listmenu.append([primarykey, namakaryawan, jabatankaryawan, alamatkaryawan, umurkaryawan])
                print("Karyawan berhasil ditambahkan.")  # Pesan konfirmasi karyawan berhasil ditambahkan
                
                # Tampilkan informasi tabel terbaru setelah menambahkan karyawan
                print("Informasi Tabel Terbaru:")
                table = PrettyTable(['NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                for karyawan in listmenu:
                    table.add_row(karyawan)
                print(table)
                
                # Loop untuk meminta apakah ingin menambahkan karyawan lagi atau tidak
                while True:
                    ulangi = input("Tambahkan karyawan lagi? (ya/tidak): ").lower()
                    if ulangi not in ['ya', 'tidak']:
                        print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")  # Pesan jika input tidak valid
                    else:
                        break  # Keluar dari loop saat input valid

                # Keluar dari loop utama dan kembali ke menu utama jika pengguna tidak ingin menambahkan karyawan lagi
                if ulangi == 'tidak':
                    break  # Menghentikan loop dan kembali ke menu utama

            elif read == '2':
                break  # Keluar dari loop utama dan kembali ke menu utama setelah memilih opsi kembali
            else:
                print("Angka yang anda masukkan tidak valid")  # Pesan ketika angka yang dimasukkan tidak valid
        except ValueError:
            print("DATA SALAH, TIDAK DAPAT DI INPUT. Umur harus berupa bilangan bulat.")  # Pesan ketika terjadi kesalahan dalam memproses input Umur









             
# menghapus karyawan

def menghapus_karyawan():
    # Loop utama, menjalankan menu untuk menghapus karyawan atau kembali ke menu utama
    while True:
        print('''
        Sub Menu Menghapus Daftar Karyawan               
        1. Menghapus Karyawan
        2. Kembali Ke Menu Utama      
        ''')
        read = input('Masukkan Nomor Yang Ingin Dipilih :  ')
        
        if read == '1':
            try:
                # Menampilkan daftar karyawan sebelum penghapusan
                print("Daftar Karyawan Sebelum Penghapusan:")
                if listmenu:  # Memeriksa apakah daftar karyawan tidak kosong
                    table = PrettyTable(['NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                    for karyawan in listmenu:
                        table.add_row(karyawan)
                    print(table)
                else:
                    print('Daftar karyawan kosong.')  # Pesan jika daftar karyawan kosong

                # Loop untuk memastikan NIK yang dimasukkan valid
                while True:
                    nik_hapus = input('Masukkan NIK Karyawan yang Ingin Dihapus: ')
                    karyawan_ditemukan = False
                    
                    # Pengecekan setiap karyawan dalam daftar untuk mencocokkan NIK
                    for karyawan in listmenu:
                        if karyawan[0] == nik_hapus:  # Jika NIK ditemukan dalam daftar
                            karyawan_ditemukan = True
                            break  # Keluar dari loop jika NIK ditemukan
                    
                    # Jika NIK ditemukan, keluar dari loop
                    if karyawan_ditemukan:
                        break
                    else:
                        # Pesan jika NIK tidak ditemukan dalam daftar
                        print(f"Karyawan dengan NIK {nik_hapus} tidak ditemukan.")
                
                # Menghapus karyawan jika NIK ditemukan
                for karyawan in listmenu:
                    if karyawan[0] == nik_hapus:
                        listmenu.remove(karyawan)
                        print(f"Karyawan dengan NIK {nik_hapus} berhasil dihapus.")
                        break

            except ValueError:
                print("DATA SALAH, TIDAK DAPAT DI INPUT. Harap masukkan NIK yang benar.")  # Pesan kesalahan jika terjadi kesalahan dalam memproses input NIK

            # Menampilkan tabel terbaru setelah menghapus karyawan
            print("Informasi Tabel Terbaru:")
            if listmenu:  # Memeriksa apakah daftar karyawan tidak kosong setelah penghapusan
                table = PrettyTable(['NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                for karyawan in listmenu:
                    table.add_row(karyawan)
                print(table)
            else:
                print('Daftar karyawan kosong.')

            # Loop untuk meminta apakah ingin menghapus karyawan lain atau tidak
            while True:
                ulangi = input("Hapus karyawan lain? (ya/tidak): ").lower()
                if ulangi not in ['ya', 'tidak']:
                    print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
                else:
                    break  # Keluar dari loop pengulangan apakah ingin menghapus karyawan lain

            # Keluar dari loop utama dan kembali ke menu utama jika tidak ingin menghapus karyawan
            if ulangi.lower() != 'ya':
                break  

        elif read == '2':
            break  # Keluar dari loop utama dan kembali ke menu utama jika memilih untuk kembali ke menu utama
        else:
            print("Angka yang anda masukkan tidak valid")  # Pesan ketika angka yang dimasukkan tidak valid

# update karyawan

def mengupdate_karyawan():
    # Loop utama, menjalankan menu untuk mengupdate data karyawan atau kembali ke menu utama
    while True:
        print('Daftar Menu\n')
        print('''
        Sub Menu mengupdate daftar karyawan               
        1. Update NIK
        2. Update Nama
        3. Update Jabatan
        4. Update Alamat
        5. Update Umur
        6. Kembali Ke Menu Utama
        ''')
        read = input('Masukkan Nomor Kolom Yang Ingin Dipilih :  ')
        
        # Memeriksa apakah pilihan input berada dalam daftar menu yang valid
        if read in ['1', '2', '3', '4', '5']:
            try:
                # Menampilkan tabel karyawan sebelum proses update
                table = PrettyTable(['Index', 'NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                for idx, data in enumerate(listmenu, start=1):
                    table.add_row([idx] + data)
                print(table)
                
                # Meminta index karyawan yang ingin diupdate
                indexmenu = int(input('Masukkan Index karyawan yang ingin diupdate : ')) - 1
                
                # Memeriksa apakah index yang dimasukkan valid
                if 0 <= indexmenu < len(listmenu):
                    if read == '1':
                        # Update NIK
                        while True:
                            primarykey = input('Masukkan NIK Yang Baru : ')
                            nik_exists = any(primarykey == data[0] for data in listmenu)
                            
                            # Validasi NIK baru
                            if not nik_exists and len(primarykey) <= 8 and primarykey.isalnum():  
                                break
                            elif nik_exists:
                                print("NIK sudah ada dalam daftar. Masukkan NIK yang berbeda.")
                            else:
                                print("NIK harus terdiri dari huruf dan angka maksimal 8 karakter.")
                        listmenu[indexmenu][0] = primarykey
                    elif read == '2':
                        # Update Nama
                        while True:
                            namakaryawan = input('Masukkan Nama Karyawan Yang Baru : ')
                            
                            # Validasi nama baru
                            if namakaryawan.isalpha() and len(namakaryawan) <= 20:
                                listmenu[indexmenu][1] = namakaryawan
                                break
                            elif not namakaryawan.isalpha():
                                print("Nama harus terdiri dari huruf saja.")
                            elif len(namakaryawan) > 20:
                                print("Nama tidak boleh lebih dari 20 karakter.")
                    elif read == '3':
                        # Update Jabatan
                        jabatankaryawan = input('Masukkan Jabatan Karyawan Yang Baru : ')
                        listmenu[indexmenu][2] = jabatankaryawan
                    elif read == '4':
                        # Update Alamat
                        alamatkaryawan = input('Masukkan Alamat Karyawan Yang Baru : ')
                        listmenu[indexmenu][3] = alamatkaryawan
                    elif read == '5':
                        # Update Umur
                        while True:
                            umurkaryawan = input('Masukkan Umur Karyawan Yang Baru : ')
                            
                            # Validasi umur baru
                            if umurkaryawan.isdigit() and 18 <= int(umurkaryawan) <= 45:  
                                break # Berhenti jika umur yang dimasukkan valid
                            else:
                                print("Umur harus berupa angka dan berada dalam rentang 18-45 tahun.")
                        listmenu[indexmenu][4] = int(umurkaryawan)
                    print("Data karyawan berhasil diupdate.")
                    
                    # Menampilkan laporan tabel terbaru setelah selesai mengupdate
                    print("Laporan Tabel Terbaru:")
                    table = PrettyTable(['Index', 'NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                    for idx, data in enumerate(listmenu, start=1):
                        table.add_row([idx] + data)
                    print(table)
                else:
                    print('Index Tidak Valid')  # Pesan ketika indeks tidak valid
            except ValueError:
                print("DATA SALAH, TIDAK DAPAT DI INPUT. Harap masukkan data yang benar.")  # Pesan kesalahan jika terjadi kesalahan dalam memproses input
        elif read == '6':
            break  # Keluar dari loop utama dan kembali ke menu utama jika memilih untuk kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor menu yang valid.")  # Pesan ketika pilihan tidak valid

# Menu Utama
while True:
    pilihanMenu = input('''
                Daftar Karyawan SAGAB LINE
                      
                -------------MENU-------------
                
                1. Menampilkan Daftar Karyawan
                2. Menambah Karyawan
                3. Menghapus Nama Karyawan
                4. Update Data Karyawan
                5. Keluar (Exit) Program
                Masukkan nomor Menu yang ingin dijalankan :   ''')
    
    
    if pilihanMenu == '1':
        menampilkan_daftar_karyawan()
    elif pilihanMenu == '2':
        menambah_Karyawan()
    elif pilihanMenu == '3':
        menghapus_karyawan()
    elif pilihanMenu == '4':
        mengupdate_karyawan()
    elif pilihanMenu == '5':
        print("                \U0001F44B ! CLOSED ! \U0001F44B")
        break