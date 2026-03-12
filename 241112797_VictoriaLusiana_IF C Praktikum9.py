class Subject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event_type, data):
        for observer in self._observers:
            observer.update(event_type, data)


class Victoria(Subject):
    def __init__(self):
        super().__init__()
        self.data_mahasiswa = [
            {"nim": "241112797", "nama": "Angelica", "nohp": "088262392155", "jenis_kelamin": "P"},
            {"nim": "241112222", "nama": "Anasta", "nohp": "081212341233", "jenis_kelamin": "P"},
            {"nim": "241113333", "nama": "Cindy", "nohp": "085367891234", "jenis_kelamin": "P"},
            {"nim": "241114444", "nama": "Jelita", "nohp": "085167889876", "jenis_kelamin": "P"},
            {"nim": "241115555", "nama": "Afni", "nohp": "081209876783", "jenis_kelamin": "P"}
        ]

        self.data_dosen = [
            {"nip": "123456789", "nama": "Bu Rina", "nohp": "081234567890", "jenis_kelamin": "P"},
            {"nip": "987654321", "nama": "Pak Iwan", "nohp": "082112345678", "jenis_kelamin": "L"}
        ]

    def input_angka(self, prompt, min_len):
        while True:
            data = input(prompt)
            if data.isdigit() and len(data) >= min_len:
                return data
            print(f" Input harus angka dan minimal {min_len} digit.\n")

    def input_jk(self, prompt="Jenis Kelamin (L/P): "):
        while True:
            jk = input(prompt).upper()
            if jk in ["L", "P"]:
                return jk
            print(" Input harus 'L' (Laki-laki) atau 'P' (Perempuan).\n")

    
    def tambah_mahasiswa(self):
        print("\n=== TAMBAH DATA MAHASISWA ===")
        nim = self.input_angka("Masukkan NIM (min 9 angka): ", 9)
        nama = input("Nama: ")
        nohp = self.input_angka("No HP (min 12 angka): ", 12)
        jk = self.input_jk() # Input Jenis Kelamin

        for m in self.data_mahasiswa:
            if m["nim"] == nim:
                print(" NIM sudah ada.")
                return

        data = {"nim": nim, "nama": nama, "nohp": nohp, "jenis_kelamin": jk}
        self.data_mahasiswa.append(data)

        self.notify("mahasiswa_added", data) # Notifikasi penambahan
        print(f"✔ Mahasiswa {nama} berhasil ditambahkan.\n")

    def tambah_dosen(self):
        print("\n=== TAMBAH DATA DOSEN ===")
        nip = self.input_angka("Masukkan NIP (min 9 angka): ", 9)
        nama = input("Nama Dosen: ")
        nohp = self.input_angka("No HP (min 12 angka): ", 12)
        jk = self.input_jk() # Input Jenis Kelamin

        for d in self.data_dosen:
            if d["nip"] == nip:
                print(" NIP sudah ada.")
                return

        data = {"nip": nip, "nama": nama, "nohp": nohp, "jenis_kelamin": jk}
        self.data_dosen.append(data)

        self.notify("dosen_added", data) # Notifikasi penambahan
        print(f"✔ Dosen {nama} berhasil ditambahkan.\n")

    def hapus_mahasiswa(self):
        print("\n=== HAPUS DATA MAHASISWA ===")
        nim_hapus = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
        
        for i, m in enumerate(self.data_mahasiswa):
            if m["nim"] == nim_hapus:
                data_dihapus = self.data_mahasiswa.pop(i)
                self.notify("mahasiswa_deleted", data_dihapus) # Notifikasi penghapusan
                print(f"✔ Mahasiswa {data_dihapus['nama']} ({nim_hapus}) berhasil dihapus.\n")
                return
        
        print(f" NIM {nim_hapus} TIDAK ditemukan.\n")

    def hapus_dosen(self):
        print("\n=== HAPUS DATA DOSEN ===")
        nip_hapus = input("Masukkan NIP Dosen yang ingin dihapus: ")
        
        for i, d in enumerate(self.data_dosen):
            if d["nip"] == nip_hapus:
                data_dihapus = self.data_dosen.pop(i)
                self.notify("dosen_deleted", data_dihapus) # Notifikasi penghapusan
                print(f"✔ Dosen {data_dihapus['nama']} ({nip_hapus}) berhasil dihapus.\n")
                return
        
        print(f" NIP {nip_hapus} TIDAK ditemukan.\n")

    def absensi(self):
        print("\n=== ABSENSI (MAHASISWA & DOSEN) ===")

        try:
            jumlah = int(input("Masukkan jumlah NIM/NIP yang ingin dicek: "))
        except ValueError:
            print("Input harus berupa angka.")
            return

        hadir = 0
        tidak = 0

        for i in range(jumlah):
            key = input(f"Masukkan NIM/NIP ke-{i+1}: ")
            
            # Cari di data mahasiswa
            found = next((m for m in self.data_mahasiswa if m["nim"] == key), None)

            if found:
                print(f"{found['nama']} (Mahasiswa - {found['jenis_kelamin']}) HADIR.")
                self.notify("absensi", found)
                hadir += 1
                continue

            # Cari di data dosen
            found = next((d for d in self.data_dosen if d["nip"] == key), None)

            if found:
                print(f"{found['nama']} (Dosen - {found['jenis_kelamin']}) HADIR.")
                self.notify("absensi", found)
                hadir += 1
                continue

            print(f"{key} TIDAK ditemukan.")
            tidak += 1

        print("\n--- Rekap Absensi ---")
        print(f"Hadir: {hadir}")
        print(f"Tidak hadir: {tidak}")

    def tampilkan_data(self):
        print("\n=== DATA MAHASISWA ===")
        if not self.data_mahasiswa:
            print("Belum ada data mahasiswa.")
        for m in self.data_mahasiswa:
            print(f"NIM: {m['nim']}, Nama: {m['nama']} ({m['jenis_kelamin']}), No HP: {m['nohp']}")

        print("\n=== DATA DOSEN ===")
        if not self.data_dosen:
            print("Belum ada data dosen.")
        for d in self.data_dosen:
            print(f"NIP: {d['nip']}, Nama: {d['nama']} ({d['jenis_kelamin']}), No HP: {d['nohp']}")


class AbsensiObserver:
    def __init__(self):
        self.log = []
    
    def update(self, event_type, data):
        if event_type == "mahasiswa_added":
            print(f"[Observer] Mahasiswa baru ditambahkan: {data['nama']}")
        elif event_type == "dosen_added":
            print(f"[Observer] Dosen baru ditambahkan: {data['nama']}")
        elif event_type == "mahasiswa_deleted":
            print(f"[Observer] Mahasiswa dihapus: {data['nama']}")
        elif event_type == "dosen_deleted":
            print(f"[Observer] Dosen dihapus: {data['nama']}")
        elif event_type == "absensi":
            print(f"[Observer] Absensi dicatat: {data['nama']}")

        self.log.append((event_type, data))


class Menu:
    def __init__(self):
        self.system = Victoria()
        self.observer = AbsensiObserver()
        self.system.attach(self.observer)
    
    def run(self):
        while True:
            print("\n=== MENU ===")
            print("1. Tambah Mahasiswa")
            print("2. Tambah Dosen")
            print("3. Hapus Mahasiswa")
            print("4. Hapus Dosen")
            print("5. Lihat Data")
            print("6. Absensi")
            print("7. Keluar")

            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.system.tambah_mahasiswa()
            elif pilih == "2":
                self.system.tambah_dosen()
            elif pilih == "3":
                self.system.hapus_mahasiswa() # Menu Hapus Mahasiswa
            elif pilih == "4":
                self.system.hapus_dosen()    # Menu Hapus Dosen
            elif pilih == "5":
                self.system.tampilkan_data()
            elif pilih == "6":
                self.system.absensi()
            elif pilih == "7":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid.\n")

Menu().run()