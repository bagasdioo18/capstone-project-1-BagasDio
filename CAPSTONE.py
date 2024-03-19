from prettytable import PrettyTable

listmenu = [
    ['A1', 'Bagas', 'Direktur', 'Bekasi', 32],
    ['A2', 'Dio', 'Staff', 'Jawa', 23],
    ['A3', 'Hanggoro', 'Manager', 'Medan', 25],
    ['A4', 'Sri', 'Analyst', 'Surabaya', 29],
    ['A5', 'Tatang', 'Developer', 'Bandung', 27]
    
    ]

#sub menu
def menampilkan_daftarkaryawan1():
    while True:
        print('Daftar Menu\n')
        print('''Sub Menu menampilkan daftar karyawan
                1. Menampilkan Nama Karyawan
                2. Cari NIK Karyawan
                3. Kembali Ke Menu Utama''')
        read = input('Masukkan NIK Yang Ingin Dicari :  ')
        if read == '1':
            if listmenu != []:
                table = PrettyTable(['Index', 'NIK', 'Nama', 'Posisi', 'Alamat', 'Umur'])
                for idx, data in enumerate(listmenu, start=1):
                    table.add_row([idx] + data)
                print(table)
            elif listmenu == []:
                print ('Data kosong')
        elif read == '2':
            if listmenu != []:
                by_id = input('Masukan NIK Karyawan Yang Ingin Anda Cari :  ')
                for data in listmenu:
                    if data[0] == by_id:
                        table = PrettyTable(['ID Karyawan', 'Nama', 'Posisi', 'Alamat', 'Umur'])
                        table.add_row(data[:5])
                        print(table)
                        break  # Menghentikan loop setelah menampilkan tabel 
            elif listmenu == []:
                print ('Data kosong')
        elif read == '3':
            break  # Menghentikan loop dan kembali ke menu utama
        else:
            print('Angka yang anda masukkan tidak valid')




# menambah karyawan
def menambah_Karyawan():
    while True:
        print('''
        Sub Menu Menambah Daftar Karyawan               
        1. Menambah Karyawan
        2. Kembali Ke Menu Utama      
        ''')
        read = input('Masukkan Nomor Yang Ingin Dipilih :  ')
        try:
            if read == '1':
                # Memastikan input ID karyawan sesuai dengan kriteria
                while True:
                    primarykey = input('Masukkan NIK Karyawan : ')
                    if len(primarykey) <= 8 and primarykey.isalnum():  
                        nik_exists = False
                        for data in listmenu:
                            if data[0] == primarykey:
                                nik_exists = True
                                break
                        if not nik_exists:
                            break
                        else:
                            print("NIK sudah ada. Harap masukkan NIK yang berbeda.")
                    else:
                        print("NIK harus terdiri dari maksimal 8 karakter, hanya huruf dan angka.")
                
                # Memastikan input nama sesuai dengan kriteria
                while True:
                    namakaryawan = input('Masukkan Nama Karyawan : ')
                    if len(namakaryawan) <= 20 and namakaryawan.isalpha():  
                        break
                    else:
                        print("Nama harus terdiri dari maksimal 20 huruf dan tidak boleh mengandung angka.")
                
                jabatankaryawan = input('Masukan Jabatan Karyawan : ')
                alamatkaryawan = input('Masukan Alamat Karyawan : ')
                
                # Memastikan input umur adalah angka dan hanya 2 angka
                while True:
                    umurkaryawan = input('Masukan Umur Karyawan : ')
                    if umurkaryawan.isdigit() and len(umurkaryawan) == 2:  
                        umurkaryawan = int(umurkaryawan)
                        if 18 <= umurkaryawan <= 45:  
                            break
                        else:
                            print("Umur harus berada dalam rentang 18-45 tahun.")
                    else:
                        print("Umur harus berupa 2 angka.")
                
                listmenu.append([primarykey, namakaryawan, jabatankaryawan, alamatkaryawan, umurkaryawan])
                print("Karyawan berhasil ditambahkan.")
                
                # Tampilkan informasi tabel terbaru setelah menambahkan karyawan
                print("Informasi Tabel Terbaru:")
                table = PrettyTable(['NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                for karyawan in listmenu:
                    table.add_row(karyawan)
                print(table)
                
                while True:
                    ulangi = input("Tambahkan karyawan lagi? (ya/tidak): ").lower()
                    if ulangi not in ['ya', 'tidak']:
                        print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
                    else:
                        break  # Keluar dari loop saat input valid

                if ulangi == 'tidak':
                    break  # Keluar dari loop utama dan kembali ke menu utama

            elif read == '2':
                break
            else:
                print("Angka yang anda masukkan tidak valid")
        except ValueError:
            print("DATA SALAH, TIDAK DAPAT DI INPUT. Umur harus berupa bilangan bulat.")






             

# menghapus karyawan
from prettytable import PrettyTable

def menampilkan_daftarkaryawan():
    table = PrettyTable(['NIK', 'Nama', 'Posisi', 'Alamat', 'Umur'])
    for karyawan in listmenu:
        table.add_row(karyawan)
    print(table)

def menghapus_karyawan():
    while True:
        print('''
        Sub Menu Menghapus Daftar Karyawan               
        1. Menghapus Karyawan
        2. Kembali Ke Menu Utama      
        ''')
        read = input('Masukkan Nomor Yang Ingin Dipilih :  ')
        if read == '1':
            try:
                print("Daftar Karyawan Sebelum Penghapusan:")
                menampilkan_daftarkaryawan()
                nik_hapus = input('Masukkan NIK Karyawan yang Ingin Dihapus: ')
                # Mencari karyawan berdasarkan NIK dan menghapusnya jika ditemukan
                karyawan_ditemukan = False
                for karyawan in listmenu:
                    if karyawan[0] == nik_hapus:
                        listmenu.remove(karyawan)
                        print(f"Karyawan dengan NIK {nik_hapus} berhasil dihapus.")
                        karyawan_ditemukan = True
                        break
                if not karyawan_ditemukan:
                    print(f"Karyawan dengan NIK {nik_hapus} tidak ditemukan.")
            except ValueError:
                print("DATA SALAH, TIDAK DAPAT DI INPUT. Harap masukkan nomor yang benar.")
            finally:
                while True:
                    ulangi = input("Hapus karyawan lain? (ya/tidak): ").lower()
                    if ulangi not in ['ya', 'tidak']:
                        print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
                    else:
                        break
                if ulangi.lower() != 'ya':
                    break  # Kembali ke menu utama jika tidak ingin menghapus karyawan
        elif read == '2':
            break








# update karyawan
def mengedit_karyawan():
    while True:
        print('Daftar Menu\n')
        print('''
        Sub Menu mengedit daftar karyawan               
        1. Update NIK
        2. Update Nama
        3. Update Jabatan
        4. Update Alamat
        5. Update Umur
        6. Kembali Ke Menu Utama
        ''')
        read = input('Masukkan Nomor Kolom Yang Ingin Dipilih :  ')
        
        if read in ['1', '2', '3', '4', '5']:
            try:
                table = PrettyTable(['Index', 'NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                for idx, data in enumerate(listmenu, start=1):
                    table.add_row([idx] + data)
                print(table)
                
                indexmenu = int(input('Masukkan Index karyawan yang ingin diupdate : ')) - 1
                if 0 <= indexmenu < len(listmenu):
                    if read == '1':
                        # Update NIK
                        while True:
                            primarykey = input('Masukkan NIK Yang Baru : ')
                            nik_exists = any(primarykey == data[0] for data in listmenu)
                            if not nik_exists and len(primarykey) <= 8 and primarykey.isalnum():  
                                break
                            elif nik_exists:
                                print("NIK sudah ada dalam daftar. Masukkan NIK yang berbeda.")
                            else:
                                print("NIK harus terdiri dari huruf dan angka maksimal 8 karakter.")
                        listmenu[indexmenu][0] = primarykey
                    elif read == '2':
                        # Update Nama
                        namakaryawan = input('Masukkan Nama Karyawan Yang Baru : ')
                        listmenu[indexmenu][1] = namakaryawan
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
                            if umurkaryawan.isdigit() and 18 <= int(umurkaryawan) <= 45:  
                                break
                            else:
                                print("Umur harus berupa angka dan berada dalam rentang 18-45 tahun.")
                        listmenu[indexmenu][4] = int(umurkaryawan)
                    print("Data karyawan berhasil diupdate.")
                    
                    # Tampilkan laporan tabel terbaru setelah selesai mengupdate
                    print("Laporan Tabel Terbaru:")
                    table = PrettyTable(['Index', 'NIK', 'Nama', 'Jabatan', 'Alamat', 'Umur'])
                    for idx, data in enumerate(listmenu, start=1):
                        table.add_row([idx] + data)
                    print(table)
                else:
                    print('Index Tidak Valid')
            except ValueError:
                print("DATA SALAH, TIDAK DAPAT DI INPUT. Harap masukkan data yang benar.")
            finally:
                while True:
                    ulangi = input("Apakah Anda ingin mengedit karyawan lain? (ya/tidak): ")
                    if ulangi.lower() not in ['ya', 'tidak']:
                        print("Input tidak valid. Harap masukkan 'ya' atau 'tidak'.")
                    else:
                        if ulangi.lower() != 'ya':
                            return  # Langsung kembali ke menu utama
                        else:
                            break  # Lanjutkan ke proses berikutnya jika pengguna memilih "ya"
        elif read == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor menu yang valid.")











while True:
    pilihanMenu = input('''
                Daftar Karyawan 2024
                      
                List Menu:
                1. Menampilkan Daftar Karyawan
                2. Menambah Karyawan
                3. Menghapus Nama Karyawan
                4. Update Data Karyawan
                5. Keluar (Exit) Program
                Masukkan nomor Menu yang ingin dijalankan :   ''')
    
    
    if pilihanMenu == '1':
        menampilkan_daftarkaryawan1()
    elif pilihanMenu == '2':
        menambah_Karyawan()
    elif pilihanMenu == '3':
        menghapus_karyawan()
    elif pilihanMenu == '4':
        mengedit_karyawan()
    elif pilihanMenu == '5':
        print("                \U0001F44B ! CLOSED ! \U0001F44B")
        break