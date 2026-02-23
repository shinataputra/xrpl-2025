import requests
import textwrap

URL = "https://api.npoint.io/99c279bb173a6e28359c/data"

res = requests.get(URL)
data = res.json()

print("=" * 60)
print("DAFTAR SURAT AL-QUR'AN")
print("=" * 60)

for surat in data[:5]:  # batasi biar terminal nggak meledak
    print(f"Nomor     : {surat['nomor']}")
    print(f"Nama      : {surat['nama']} ({surat['asma']})")
    print(f"Arti      : {surat['arti']}")
    print(f"Tempat    : {surat['type'].upper()}")
    print(f"Ayat      : {surat['ayat']}")
    print(f"Audio     : {surat['audio']}")
    print("Keterangan:")

    ket = surat["keterangan"].replace("<i>", "").replace("</i>", "")
    print(textwrap.fill(ket, width=60))

    print("-" * 60)
