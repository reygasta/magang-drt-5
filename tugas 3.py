harga_permak = {
    1: {"jenis": "pasang kancing", "harga": 10000},
    2: {"jenis": "tambal lubang", "harga": 20000},
    3: {"jenis": "permak celana", "harga": 30000},
    4: {"jenis": "permak baju", "harga": 40000},
}

def hitung_total(pilihan, jumlah):
    harga = harga_permak[pilihan]["harga"]
    total_harga = harga * jumlah
    return harga, jumlah, total_harga

def daftar_permak():
    print("Daftar permak:")
    for nomor, permak in harga_permak.items():
        print(f"{nomor}. {permak['jenis']}: Rp{permak['harga']}")

def diterima():
    nomor_permak = int(input("Pilih nomor permak: "))
    jumlah = int(input("Jumlah yang dibeli: "))
    return nomor_permak, jumlah

def cetak_struk(jenis_permak, jumlah, total_harga):
    print("Struk permak baju")
    print(f"Jenis permak: {harga_permak[jenis_permak]['jenis']}")
    print(f"Jumlah yang dibeli: {jumlah}")
    print(f"Total harga: Rp{total_harga}")

daftar_permak()
nomor_permak, jumlah = diterima()
harga, jumlah_beli, total_harga = hitung_total(nomor_permak, jumlah)
cetak_struk(nomor_permak, jumlah_beli, total_harga)
