import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    """
    Tanggal: 28 Agustus 2022
    Waktu: 15:09:56 WIB
    Magnitudo: 4.3
    Kedalaman: 33 km
    Lokasi: 9.49 LS - 117.14 BT
    Pusat gempa: berada dilaut 87 km Tenggara SumbawaBarat
    Dirasakan: (Skala MMI) II-III Sumbawa Barat
    :return:
"""
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content .status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(',')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = soup.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1




        hasil = dict()
        hasil['Tanggal'] = tanggal #'28 Agustus 2022'
        hasil['Waktu'] = waktu #'15:09:56 WIB'
        hasil['Magnitudo'] = 4.3
        hasil['Koordinat'] = {'LS': 9.49, 'BT': 117.14}
        hasil['Lokasi'] = 'laut 87 km Tenggara SumbawaBarat'
        hasil['Dirasakan'] = '(Skala MMI) II-III Sumbawa Barat'

        #print(hasil)
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('Tidak ada data gempa terkini')
        return
    print('\nGempa terakhir terjadi pada:')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Koordinat LS: {result['Koordinat']['LS']}, BT: {result['Koordinat']['BT']}")
    print(f"Lokasi {result['Lokasi']}")
    print(f"Dirasakan {result['Dirasakan']}")
