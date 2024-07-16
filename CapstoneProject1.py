karyawan = [{'id_karyawan':'001', 'nama':'Jake', 'gender':'Laki-laki', 'jabatan':'Supervisor', 'departemen':'Marketing','status_karyawan':'Tetap'}, 
            {'id_karyawan':'002', 'nama':'Evan', 'gender':'Laki-laki', 'jabatan':'Staf', 'departemen':'Sales', 'status_karyawan':'Kontrak'},
            {'id_karyawan':'003', 'nama':'Seno', 'gender':'Laki-laki', 'jabatan':'Supervisor', 'departemen':'Sales', 'status_karyawan':'Tetap'}]

def menu():
    print("\n========| MENU UTAMA |========")
    main_menu = ['1. Daftar Karyawan',
                 '2. Menambah Data Karyawan',
                 '3. Mengubah Data Karyawan',
                 '4. Menghapus Data Karyawan',
                 '5. Exit']
    for display in main_menu: 
        print(display)

def lihat_Data():
        while True:
            print("\n--------| Daftar Karyawan |--------")
            print("1. Daftar Seluruh Karyawan")
            print("2. Daftar Karyawan Berdasar ID")
            print("3. Daftar Karyawan Berdasar Nama")
            print("4. Daftar Karyawan Berdasar Departemen")
            print("5. Daftar Karyawan Berdasar Status Karyawan")
            print("6. Kembali ke Menu Utama")
            subMenu = input("Pilih sub menu daftar karyawan (1-6): ")

            if subMenu == '1':
                if not karyawan:
                   print("Tidak ada data. Harap masukkan data terlebih dahulu melalui menu 2. Menambah Data Karyawan.")
                else:  
                    print ("\n<<< Daftar Seluruh Karyawan >>>") 
                    for data_karyawan in karyawan:
                        print("ID: {}, Nama: {}, Jenis Kelamin: {}, Jabatan: {}, Departemen: {}, Status: {}".format(data_karyawan['id_karyawan'], data_karyawan['nama'], data_karyawan['gender'], data_karyawan['jabatan'], data_karyawan['departemen'], data_karyawan['status_karyawan']))
            
            elif subMenu == '2':
                id_karyawan = input("\nMasukan nomor ID Karyawan: ")
                exist = False
                for data_karyawan in karyawan:
                    if data_karyawan['id_karyawan'] == id_karyawan:
                        print("ID: {}, Nama: {}, Jenis Kelamin: {}, Jabatan: {}, Departemen: {}, Status: {}".format(data_karyawan['id_karyawan'], data_karyawan['nama'], data_karyawan['gender'], data_karyawan['jabatan'], data_karyawan['departemen'], data_karyawan['status_karyawan']))
                        exist = True   
                if not exist: 
                    print("Karyawan dengan ID {} tidak ditemukan.".format(id_karyawan))
            
            elif subMenu == '3':
                nama = input("\nMasukan Nama Karyawan: ").lower()
                exist = False
                for data_karyawan in karyawan:
                    if data_karyawan['nama'].lower() == nama:
                        print("ID: {}, Nama: {}, Jenis Kelamin: {}, Jabatan: {}, Departemen: {}, Status: {}".format(data_karyawan['id_karyawan'], data_karyawan['nama'], data_karyawan['gender'], data_karyawan['jabatan'], data_karyawan['departemen'], data_karyawan['status_karyawan']))
                        exist = True    
                if not exist:
                    print("Karyawan dengan nama {} tidak ditemukan.".format(nama))    
            
            elif subMenu == '4':
                departemen = input("\nMasukan Nama Departemen: ").lower()
                exist = False
                for data_karyawan in karyawan:
                    if data_karyawan['departemen'].lower() == departemen:
                        print("ID: {}, Nama: {}, Jenis Kelamin: {}, Jabatan: {}, Departemen: {}, Status: {}".format(data_karyawan['id_karyawan'], data_karyawan['nama'], data_karyawan['gender'], data_karyawan['jabatan'], data_karyawan['departemen'], data_karyawan['status_karyawan']))
                        exist = True    
                if not exist:
                    print("Tidak ada karyawan pada Departemen {}.".format(departemen))       
            
            elif subMenu == '5':
                status_karyawan = input("\nMasukan status karyawan: ").lower()
                exist = False
                for data_karyawan in karyawan:
                    if data_karyawan['status_karyawan'].lower() == status_karyawan:
                        print("ID: {}, Nama: {}, Jenis Kelamin: {}, Jabatan: {}, Departemen: {}, Status: {}".format(data_karyawan['id_karyawan'], data_karyawan['nama'], data_karyawan['gender'], data_karyawan['jabatan'], data_karyawan['departemen'], data_karyawan['status_karyawan']))
                        exist = True          
                if not exist:
                    print("Tidak ada karyawan dengan status {}.".format(status_karyawan))                             
            
            elif subMenu == '6':
                break
            else: 
                print("Pilihan tidak valid.")

def tambah_Data():
    while True:
        print("\n--------| Tambah Data Karyawan |--------")
        print("1. Tambah Data Karyawan")
        print("2. Kembali ke Menu Utama")
        subMenu = input("Pilih sub menu daftar karyawan: ")

        if subMenu == '1':
            print ("\n<<< Tambah Data Karyawan >>>")
            id_karyawan = input("Masukkan nomor ID karyawan: ")
            exist = False
            for data_karyawan in karyawan:
                if data_karyawan['id_karyawan'] == id_karyawan:
                    exist = True
                    print("Data sudah terdaftar.")
            if not exist:
                nama = input("Masukkan nama karyawan: ")
                gender = input("Masukkan jenis kelamin karyawan: ")
                jabatan = input("Masukkan jabatan karyawan: ")
                departemen = input("Masukkan departemen karyawan: ")
                status = input("Masukkan status karyawan: ")

                data_karyawan = {'id_karyawan': id_karyawan, 'nama': nama, 'gender': gender, 'jabatan': jabatan, 'departemen': departemen, 'status_karyawan':status}
                warning = input("Apakah anda yakin ingin menambah data? (Y/N)\n")
                if warning == 'Y':
                    karyawan.append(data_karyawan)
                    print("Tambah data berhasil.")
                elif warning == 'N':
                    print("Tambah data gagal.")
        
        elif subMenu == '2':
            break
        else: 
            print("Pilihan tidak valid.")

def ubah_Data():
    while True:
        print("\n--------| Ubah Data Karyawan |--------")
        print("1. Ubah Data Karyawan")
        print("2. Kembali ke Menu Utama")
        subMenu = input("Pilih sub menu: ")

        if subMenu == '1':
            print ("\n<<< Ubah Data Karyawan >>>")
            id_karyawan = input("Masukkan ID karyawan yang akan diubah: ")
            exist = False

            for data_karyawan in karyawan:
                if data_karyawan['id_karyawan'] == id_karyawan:
                    exist = True
                    while True:
                        pilihan_Update = input("1. Nama \n2. Jenis Kelamin \n3. Jabatan \n4. Departemen \n5. Status Karyawan \nPilih kolom yang akan diperbarui: ")

                        if pilihan_Update == '1':
                            new_nama = input("Masukan nama baru: ")
                            warning = input("Apakah anda yakin ingin mengubah nama {} menjadi {}? (Y/N)\n".format(data_karyawan['nama'],new_nama))
                            if warning == 'Y':
                                data_karyawan['nama'] = new_nama
                                print("Data berhasil diperbarui.")
                                break
                            elif warning == 'N':
                                print("Perubahan data dibatalkan.")
                                break

                        elif pilihan_Update == '2':
                            new_gender = input("Masukkan jenis kelamin baru: ")
                            warning = input("Apakah anda yakin ingin mengubah jenis kelamin {} menjadi {}? (Y/N)\n".format(data_karyawan['gender'], new_gender))
                            if warning == 'Y':
                                data_karyawan['gender'] = new_gender
                                print("Data berhasil diperbarui.")
                                break
                            elif warning == 'N':
                                print("Perubahan data dibatalkan.")
                                break

                        elif pilihan_Update == '3':
                            new_jabatan = input("Masukkan jabatan baru: ")
                            warning = input("Apakah anda yakin ingin mengubah jabatan {} menjadi {}? (Y/N)\n".format(data_karyawan['jabatan'], new_jabatan))
                            if warning == 'Y':
                                data_karyawan['jabatan'] = new_jabatan
                                print("Data berhasil diperbarui.")
                                break
                            elif warning == 'N':
                                print("Perubahan data dibatalkan.")
                                break

                        elif pilihan_Update == '4':
                            new_departemen = input("Masukkan Departemen baru: ")
                            warning = input("Apakah anda yakin ingin mengubah departemen {} menjadi {}? (Y/N)\n".format(data_karyawan['departemen'], new_departemen))
                            if warning == 'Y':
                                data_karyawan['departemen'] = new_departemen
                                print("Data berhasil diperbarui.")
                                break
                            elif warning == 'N':
                                print("Perubahan data dibatalkan.")
                                break

                        elif pilihan_Update == '5':
                            new_status_karyawan = input("Masukkan status karyawan baru: ")
                            warning = input("Apakah anda yakin ingin mengubah status karyawan {} menjadi {}? (Y/N)\n".format(data_karyawan['status_karyawan'], new_status_karyawan))
                            if warning == 'Y':
                                data_karyawan['status_karyawan'] = new_status_karyawan
                                print("Data berhasil diperbarui.")
                                break
                            elif warning == 'N':
                                print("Perubahan data dibatalkan.")
                                break
                        else:
                            print("Kolom tidak ditemukan.")
            if not exist:
                print("Karyawan dengan ID {} tidak ditemukan.".format(id_karyawan))  
        elif subMenu == '2':
            break
        else: 
            print("Pilihan tidak valid.")   
    
def hapus_Data(): 
    while True:
        print("\n--------| Hapus Data Karyawan |--------")
        print("1. Hapus Data Karyawan")
        print("2. Kembali ke Menu Utama")
        subMenu = input("Pilih sub menu: ")

        if subMenu == '1':
            print ("\n<<< Hapus Data Karyawan >>>")
            id_karyawan = input("Masukkan nomor ID karyawan yang akan dihapus: ")
            exist = False

            for data_karyawan in karyawan:
                if data_karyawan['id_karyawan'] == id_karyawan:
                    exist = True
                    warning = input("Apakah anda yakin ingin menghapus karyawan dengan ID {}? (Y/N)\n".format(id_karyawan))
                    if warning == 'Y':
                        karyawan.remove(data_karyawan)
                        print("Data karyawan berhasil dihapus.")
                    elif warning == 'N':
                        print("Hapus data gagal.")
            if not exist:
                print("Karyawan dengan ID {} tidak ditemukan.".format(id_karyawan))
        
        elif subMenu == '2':
            break
        else: 
            print("Pilihan tidak valid.")  

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1': 
            lihat_Data()
        elif pilihan == '2':
            tambah_Data()
        elif pilihan == '3':
            ubah_Data()
        elif pilihan == '4':
            hapus_Data()
        elif pilihan == '5':
            print("Keluar dari program, sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Harap pilih menu (1-5).")

if __name__ == "__main__":
    main()
