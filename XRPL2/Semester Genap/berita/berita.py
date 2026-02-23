import requests

url = "https://newsapi.org/v2/everything"
params = {
    "q": "tesla",
    "from": "2025-12-27",
    "sortBy": "publishedAt",
    "apiKey": "44ba3ff5c6ce464883cc40912d62c480"
}

res = requests.get(url, params=params)
data = res.json()

print("="*60)
print("ISI BERITA")
print("="*60)

for i, a in enumerate(data["articles"][:3], start=1):
    print(f"{i}. {a['title']}")
    print(f"Sumber   : {a['source']['name']}")
    print(f"Waktu    : {a['publishedAt']}")
    print()

    # ISI BERITA
    if a["content"]:
        print(a["content"])
    else:
        print("(Isi berita tidak tersedia, buka link asli)")

    print(f"\nLink: {a['url']}")
    print("-"*60)
