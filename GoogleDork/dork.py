import requests
from bs4 import BeautifulSoup

# Google dork sorgusu
site = input("Taranacak site linkini giriniz:")
dork_query = site, "ext:doc OR ext:pdf OR ext:jpg"

# Google arama sonuçlarının sayfa sayısı
num_pages = 5

# Arama sonuçlarının kaçıncı sayfadan başlayacağı
start_page = 0

# Sonuçları kaydedilecek dosya adı
file_name = "dork.txt"

# Google arama sonuçlarının sayfa başına kaç sonuç içereceği
results_per_page = 10

# Döngüde kullanılacak sayaç
count = 0

# Ana döngü
for page in range(start_page, num_pages):

    # Google arama sonuçlarını çekmek için istek gönder
    url = f"https://www.google.com/search?q={dork_query}&start={page*results_per_page}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    res = requests.get(url, headers=headers)

    # HTML verilerini çek ve BeautifulSoup kütüphanesiyle ayrıştır
    soup = BeautifulSoup(res.text, "html.parser")

    # Tüm arama sonuçlarını bul
    links = soup.find_all("a")

    # Her bir arama sonucu için işlem yap
    for link in links:
        # Linkin adresini çek
        href = link.get("href")

        # Linkin hedef web sitesi olup olmadığını kontrol et
        if href is not None and "http" in href and not "google" in href:
            # Sonuçları dosyaya yaz
            with open(file_name, "a") as f:
                count += 1
                f.write(f"{count}. {href}\n")