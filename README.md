# Scraping & Analisis Data

## Koperasi Desa Merah Putih

Proyek ini bertujuan untuk mengumpulkan dan menganalisis data komentar dari berbagai platform media sosial terkait topik **Koperasi Desa Merah Putih**. Data dikumpulkan menggunakan teknik scraping dan API resmi, kemudian diproses untuk keperluan analisis lebih lanjut seperti sentiment analysis.

---

## Teknologi yang Digunakan

* **Python (Jupyter Notebook / `.ipynb`)**
* **Apify** → scraping data dari TikTok (dan dapat diperluas ke Instagram)
* **YouTube Data API v3** → mengambil komentar dari video YouTube
* **Pandas** → pengolahan dan manipulasi data
* **python-dotenv** → manajemen API key melalui environment variables

---

## 📁 Struktur Project

```
scraping/
│
├── tiktok/
│   └── tiktok.ipynb        # scraping komentar TikTok
│
├── youtube/
│   └── youtube.ipynb       # scraping komentar YouTube
│
├── results/
│   ├── *.csv               # hasil dalam format csv
│   └── *.xlsx             # hasil dalam format Excel
│
├── .env                   # menyimpan API key
├── requirements.txt       # daftar dependency
└── README.md              # dokumentasi project
```

---

## Konfigurasi Environment

Buat file `.env` di root project:

```env
API_TOKEN=your_apify_token
YOUTUBE_API_KEY=your_youtube_api_key
```
---

## Instalasi

Aktifkan virtual environment, lalu install dependency:

```bash
pip install -r requirements.txt
```
---

## Output Data

Data hasil scraping disimpan dalam format:

* `.csv` → untuk pemrosesan data
* `.xlsx` → untuk analisis manual
---

---

## Tujuan Pengembangan

Proyek ini merupakan bagian dari:

* Pengumpulan dataset media sosial
* Analisis sentimen masyarakat
* Studi terhadap persepsi publik terkait **Koperasi Desa Merah Putih**

---

Project ini dikembangkan untuk keperluan penelitian dan pembelajaran dalam bidang data science dan machine learning.
