"""Visualisasi hasil labeling sentimen dan aspek komentar TikTok.

Input  : label/tiktok/tiktok_comments_labeled.csv
Output : visualisation/results/*.png

Jalankan dari mana saja:
    python visualisation/code/tiktok_result_visual.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # tidak butuh display / aman saat dijalankan dari terminal

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

BASE_DIR = Path(__file__).resolve().parent          # visualisation/code
VISUALISATION_DIR = BASE_DIR.parent                  # visualisation
PROJECT_ROOT = VISUALISATION_DIR.parent              # root project
DATA_PATH = PROJECT_ROOT / "label" / "tiktok" / "tiktok_comments_labeled.csv"
OUTPUT_DIR = VISUALISATION_DIR / "results"

SENTIMENT_ORDER = ["Negatif", "Netral", "Positif"]
SENTIMENT_COLORS = {
    "Negatif": "#d9534f",
    "Netral": "#9e9e9e",
    "Positif": "#2e9e5b",
}
ASPECT_COLOR = "#3b6ea5"

plt.rcParams.update(
    {
        "figure.dpi": 200,
        "savefig.dpi": 200,
        "font.family": "DejaVu Sans",
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
        "axes.labelsize": 11,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
    }
)


def load_data() -> pd.DataFrame:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"File label tidak ditemukan: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    for column in ("Sentimen", "Aspek"):
        if column not in df.columns:
            raise ValueError(f"Kolom '{column}' tidak ada di {DATA_PATH.name}")
    return df


def save_figure(fig: plt.Figure, filename: str) -> Path:
    path = OUTPUT_DIR / filename
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


def plot_sentiment(df: pd.DataFrame) -> Path:
    counts = (
        df["Sentimen"]
        .value_counts()
        .reindex(SENTIMENT_ORDER, fill_value=0)
    )
    total = int(counts.sum())

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(
        counts.index,
        counts.values,
        color=[SENTIMENT_COLORS[s] for s in counts.index],
        width=0.6,
    )

    headroom = max(counts.values) * 0.18 if total else 1
    for bar, value in zip(bars, counts.values):
        percentage = value / total * 100 if total else 0
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + headroom * 0.12,
            f"{value}\n({percentage:.1f}%)",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
        )

    ax.set_ylim(0, max(counts.values) + headroom)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("Distribusi Sentimen Komentar TikTok")
    ax.set_xlabel("Sentimen")
    ax.set_ylabel("Jumlah Komentar")
    ax.grid(axis="x", visible=False)

    return save_figure(fig, "sentiment_distribution.png")


def plot_aspect(df: pd.DataFrame) -> Path:
    counts = df["Aspek"].value_counts().sort_values()  # terbesar di atas
    total = int(counts.sum())

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(counts.index, counts.values, color=ASPECT_COLOR, height=0.6)

    max_value = max(counts.values) if total else 1
    for bar, value in zip(bars, counts.values):
        percentage = value / total * 100 if total else 0
        ax.text(
            bar.get_width() + max_value * 0.015,
            bar.get_y() + bar.get_height() / 2,
            f"{value} ({percentage:.1f}%)",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_xlim(0, max_value * 1.18)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("Distribusi Aspek Komentar TikTok")
    ax.set_xlabel("Jumlah Komentar")
    ax.set_ylabel("Aspek")
    ax.grid(axis="y", visible=False)

    return save_figure(fig, "aspect_distribution.png")


def plot_sentiment_by_aspect(df: pd.DataFrame) -> Path:
    crosstab = pd.crosstab(df["Aspek"], df["Sentimen"]).reindex(
        columns=SENTIMENT_ORDER, fill_value=0
    )
    crosstab = crosstab.loc[crosstab.sum(axis=1).sort_values().index]
    totals = crosstab.sum(axis=1)

    fig, ax = plt.subplots(figsize=(10, 5.5))
    left = pd.Series(0, index=crosstab.index, dtype="int64")

    for sentiment in SENTIMENT_ORDER:
        values = crosstab[sentiment]
        ax.barh(
            crosstab.index,
            values,
            left=left,
            color=SENTIMENT_COLORS[sentiment],
            height=0.6,
            label=sentiment,
        )
        for index, value in values.items():
            if value >= 5:  # hindari label bertumpuk untuk segmen kecil
                ax.text(
                    left[index] + value / 2,
                    index,
                    str(value),
                    ha="center",
                    va="center",
                    color="white",
                    fontsize=9,
                    fontweight="bold",
                )
        left = left.add(values, fill_value=0)

    for index, total in totals.items():
        ax.text(
            total + totals.max() * 0.01,
            index,
            f"{total}",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_xlim(0, totals.max() * 1.12)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.set_title("Sentimen per Aspek Komentar TikTok")
    ax.set_xlabel("Jumlah Komentar")
    ax.set_ylabel("Aspek")
    ax.grid(axis="y", visible=False)
    ax.legend(title="Sentimen", loc="lower right", frameon=False)

    return save_figure(fig, "sentiment_by_aspect.png")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_data()
    outputs = [
        plot_sentiment(df),
        plot_aspect(df),
        plot_sentiment_by_aspect(df),
    ]

    print(f"Data   : {DATA_PATH} ({len(df)} baris)")
    print(f"Output : {OUTPUT_DIR}")
    for path in outputs:
        print(f"  - {path.name}")


if __name__ == "__main__":
    main()
