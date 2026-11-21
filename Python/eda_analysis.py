"""
Netflix Movies & TV Shows - Exploratory Data Analysis & Visualization
Author: Data Analytics Portfolio Project
Input:  netflix_data_cleaned.csv
Output: Console KPI summary + netflix_eda_dashboard.png
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_eda(data_path: str = "netflix_data_cleaned.csv", chart_path: str = "netflix_eda_dashboard.png") -> None:
    df = pd.read_csv(data_path)

    # --- 1. Summary Statistics ---
    print("=" * 55)
    print("NETFLIX CATALOG - KEY METRICS SUMMARY")
    print("=" * 55)
    print(f"Total Titles: {len(df):,}")
    print("\nContent Type Breakdown:")
    print(df["type"].value_counts().to_string())

    movies = df[df["type"] == "Movie"]["duration_value"].dropna()
    tv_shows = df[df["type"] == "TV Show"]["duration_value"].dropna()
    print(f"\nMovie Runtime (mins) -> Mean: {movies.mean():.1f} | Median: {movies.median():.0f} | Max: {movies.max():.0f}")
    print(f"TV Shows (seasons)   -> Mean: {tv_shows.mean():.1f} | Median: {tv_shows.median():.0f} | 1-Season Share: {(tv_shows == 1).mean()*100:.1f}%")

    print("\nTop 5 Primary Producing Countries:")
    print(df[df["primary_country"] != "Unknown"]["primary_country"].value_counts().head(5).to_string())

    print("\nTop 5 Primary Genres:")
    print(df["primary_genre"].value_counts().head(5).to_string())

    # --- 2. 4-Panel Visualization Dashboard ---
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("Netflix Catalog Exploratory Data Analysis (8,807 Titles)", fontsize=16, fontweight="bold", y=0.98)

    palette = {"Movie": "#E50914", "TV Show": "#221F1F"}

    # Panel A: Content Growth Over Time (2015-2021)
    yearly = df[df["year_added"].between(2015, 2021)].groupby(["year_added", "type"]).size().unstack(fill_value=0)
    yearly.plot(kind="bar", ax=axes[0, 0], color=[palette["Movie"], palette["TV Show"]], width=0.75)
    axes[0, 0].set_title("Titles Added by Year (2015–2021)", fontweight="bold")
    axes[0, 0].set_xlabel("Year Added")
    axes[0, 0].set_ylabel("Number of Titles")
    axes[0, 0].tick_params(axis="x", rotation=0)
    axes[0, 0].legend(title="Type")

    # Panel B: Top 10 Primary Countries
    top_countries = df[df["primary_country"] != "Unknown"]["primary_country"].value_counts().head(10).sort_values()
    top_countries.plot(kind="barh", ax=axes[0, 1], color="#B81D24")
    axes[0, 1].set_title("Top 10 Content-Producing Countries", fontweight="bold")
    axes[0, 1].set_xlabel("Number of Titles")
    axes[0, 1].set_ylabel("")

    # Panel C: Top 10 Primary Genres
    top_genres = df["primary_genre"].value_counts().head(10).sort_values()
    top_genres.plot(kind="barh", ax=axes[1, 0], color="#4A4E69")
    axes[1, 0].set_title("Top 10 Primary Genres", fontweight="bold")
    axes[1, 0].set_xlabel("Number of Titles")
    axes[1, 0].set_ylabel("")

    # Panel D: Movie Runtime Distribution
    sns.histplot(movies, bins=30, kde=True, ax=axes[1, 1], color="#E50914")
    axes[1, 1].axvline(movies.median(), color="#221F1F", linestyle="--", linewidth=1.5, label=f"Median: {movies.median():.0f} min")
    axes[1, 1].set_title("Movie Runtime Distribution (Minutes)", fontweight="bold")
    axes[1, 1].set_xlabel("Duration (Minutes)")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].legend()

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(chart_path, dpi=300)
    print(f"\nSaved dashboard chart to '{chart_path}'")


if __name__ == "__main__":
    run_eda()
