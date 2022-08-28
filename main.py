"""
    Aplikasi deteksi gempa terkini

    Tanggal: 28 Agustus 2022
    Waktu: 15:09:56 WIB
    Magnitudo: 4.3
    Kedalaman: 33 km
    Lokasi: 9.49 LS - 117.14 BT
    Pusat gempa: berada dilaut 87 km Tenggara SumbawaBarat
    Dirasakan: (Skala MMI) II-III Sumbawa Barat
    :return:
"""
def ekstraksi_data():

    hasil = dict()
    hasil['Tanggal'] = '28 Agustus 2022'
    hasil['Waktu'] = '15:09:56 WIB'
    hasil['Magnitudo'] = 4.3
    hasil['Lokasi'] = {'LS': 9.49, 'BT': 117.14}
    hasil['Pusat Gempa'] = 'laut 87 km Tenggara SumbawaBarat'
    hasil['Dirasakan'] = '(Skala MMI) II-III Sumbawa Barat'

    print(hasil)
    return hasil

def tampilkan_data(result):
    print('\nGempa terakhir terjadi pada:')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Lokasi LS: {result['Lokasi']['LS']}, BT: {result['Lokasi']['BT']}")
    print(f"Pusat Gempa {result['Pusat Gempa']}")
    print(f"Dirasakan {result['Dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)