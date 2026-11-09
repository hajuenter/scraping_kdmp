# Scraping & Analisis Data

## Koperasi Desa Merah Putih

Proyek ini mengumpulkan dan menganalisis komentar dari media sosial terkait topik **Koperasi Desa Merah Putih**. Data diambil menggunakan teknik scraping dan API resmi, lalu diolah untuk analisis lebih lanjut seperti pelabelan sentimen dan visualisasi hasil.

---

## Teknologi yang Digunakan

- **Python + Jupyter Notebook (`.ipynb`)**
- **Apify** → scraping komentar TikTok dan balasan X (Twitter)
- **YouTube Data API v3** → mengambil komentar video YouTube
- **Pandas** → pengolahan dan manipulasi data
- **Matplotlib** → pembuatan grafik visualisasi
- **python-dotenv** → manajemen API key melalui environment variables

---

## Struktur Project

```text
scraping/
│
├── scrape_tiktok/
│   └── scraping.ipynb              # scraping komentar TikTok
│
├── scrape_x/
│   └── scraping.ipynb              # scraping balasan X (Twitter)
│
├── scrape_youtube/
│   └── scraping.ipynb              # scraping komentar YouTube
│
├── label/
│   └── tiktok/
│       └── tiktok_comments_labeled.csv   # dataset berlabel sentimen & aspek
│
├── results/
│   ├── tiktok/                     # hasil scraping TikTok (.csv/.xlsx)
│   ├── x/                          # hasil scraping X (.csv/.xlsx)
│   └── youtube/                    # hasil scraping YouTube (.csv/.xlsx)
│
├── visualisation/
│   ├── code/
│   │   └── tiktok_result_visual.py # generator grafik
│   └── results/                    # output grafik (.png)
│
├── link_video_scraping.txt         # daftar URL sumber data
├── propmt_labelling.txt            # prompt acuan pelabelan
├── requirements.txt                # daftar dependency
├── LICENSE                         # lisensi MIT
└── README.md                       # dokumentasi project
```

> `results/`, `label/`, dan `visualisation/results/` berisi data lokal dan **tidak ikut di-commit** ke repository (lihat `.gitignore`).

---

## Konfigurasi Environment

Buat file `.env` di root project:

```env
API_TOKEN=your_apify_token
YOUTUBE_API_KEY=your_youtube_api_key
X_COOKIES=auth_token=xxx; ct0=yyy; twid=zzz
```

---

## Instalasi

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

---

## Cara Menjalankan

### 1. Scraping TikTok

Buka `scrape_tiktok/scraping.ipynb`, atur daftar `postURLs` dan jumlah komentar, lalu jalankan semua cell. Hasil disimpan ke `results/tiktok/`.

### 2. Scraping YouTube

Buka `scrape_youtube/scraping.ipynb`, tambahkan atau ubah `VIDEO_IDS`, lalu jalankan semua cell. Semua video diproses dari satu notebook dan hasilnya digabung menjadi satu file:

- `results/youtube/youtube_comments_all.csv`
- `results/youtube/youtube_comments_all.xlsx`

Kolom: `text`, `likes`, `publishedAt`, `videoId`, `videoUrl`, `commentId`, `authorDisplayName`, `authorChannelId`, `updatedAt`, `totalReplyCount`, `textOriginal`.

### 3. Scraping X (Twitter)

Buka `scrape_x/scraping.ipynb`, atur `TWEET_URLS`, `MAX_DEPTH`, dan `ONLY_DIRECT_REPLIES`, lalu jalankan semua cell. Butuh Apify actor [Twitter (X) Comment Scraper](https://apify.com/muhammetakkurtt/twitter-x-comment-scraper) dan cookie akun X di `X_COOKIES`.

Hasil disimpan ke:

- `results/x/x_comments.csv`
- `results/x/x_comments.xlsx`

Kolom: `tweet_id`, `tweet_url`, `conversation_id`, `in_reply_to_tweet_id`, `text`, `created_at`, `lang`, `favorite_count`, `reply_count`, `retweet_count`, `quote_count`, `views_count`, `reply_to_username`, `user_screen_name`, `user_name`, `user_is_blue_verified`, `sourceTweetUrl`.

### 4. Pelabelan

Dataset berlabel tersedia di `label/tiktok/tiktok_comments_labeled.csv` dengan kolom tambahan:

- `Sentimen` → Negatif, Netral, atau Positif
- `Aspek` → Regulasi atau Politik, Infrastruktur Fisik, Kelembagaan atau Tata Kelola, Ekonomi atau Unit Usaha, Operasional dan Pengadaan

Acuan pelabelan ada di `propmt_labelling.txt`.

### 5. Visualisasi

Dari root project:

```bash
python visualisation/code/tiktok_result_visual.py
```

Output grafik disimpan di `visualisation/results/`:

- `sentiment_distribution.png`
- `aspect_distribution.png`
- `sentiment_by_aspect.png`

---

## Output Data

- `.csv` → untuk pemrosesan data
- `.xlsx` → untuk analisis manual
- `.png` → grafik untuk laporan

---

## Lisensi

Proyek ini menggunakan lisensi **MIT**. Lihat file [LICENSE](LICENSE).

Copyright (c) 2026 ACH. BAHRUL MA'ARIP

---

## Tujuan Pengembangan

Proyek ini merupakan bagian dari:

- Pengumpulan dataset media sosial
- Analisis sentimen masyarakat
- Studi terhadap persepsi publik terkait **Koperasi Desa Merah Putih**

Project ini dikembangkan untuk keperluan penelitian dan pembelajaran dalam bidang data science dan machine learning.
