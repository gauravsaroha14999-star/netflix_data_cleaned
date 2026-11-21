# 🎬 Netflix Content Strategy & Catalog Exploratory Data Analysis

An end-to-end data cleaning, feature engineering, and exploratory data analysis (EDA) project examining Netflix's global catalog of **8,807 titles** (Movies & TV Shows) from 1925 to 2021.

---

## 📁 Repository Structure

```text
├── data/
│   └── netflix_data_cleaned.csv    # Cleaned & feature-engineered dataset (8,807 rows)
├── scripts/
│   ├── eda_analysis.py             # Python script for summary stats & visualizations
│   └── netflix_queries.sql         # SQL queries for business insights
└── README.md                       # Project documentation
```

---

## 🧹 Data Cleaning & Feature Engineering Pipeline

The raw dataset (`netflix_data.csv`) was processed into `netflix_data_cleaned.csv` with the following transformations:

1. **Text Standardization & Deduplication:** Stripped leading/trailing whitespace across all string columns and verified **0 duplicate records**.
2. **Data Anomaly Correction:** Realigned misplaced duration strings (e.g., `74 min`, `84 min`, `66 min`) that were mistakenly recorded in the `rating` column, moving them to `duration` and standardizing their ratings to `"Not Rated"`.
3. **Missing Value Imputation:**
   - `director`, `cast`, `country` $\rightarrow$ `"Unknown"`
   - `rating` $\rightarrow$ `"Not Rated"`
4. **Date & Temporal Feature Extraction:**
   - Parsed `date_added` into ISO format `date_added_clean` (`YYYY-MM-DD`).
   - Engineered `year_added`, `month_added`, `month_name_added`, and `years_to_netflix` (`year_added - release_year`).
5. **Granular Feature Splitting:**
   - Split `duration` into numeric `duration_value` and `duration_unit` (`Minutes` vs. `Seasons`).
   - Extracted `primary_country`, `country_count`, `primary_genre`, and `genre_count` from multi-value comma-separated lists.

---

## 📊 Key Dataset Insights

* **Catalog Composition:** **69.6%** Movies (6,131 titles) vs. **30.4%** TV Shows (2,676 titles).
* **Content Recency:** While release years span from **1925 to 2021**, the median release year is **2017** (Mean: `2014.2`, SD: `8.8`).
* **Runtime & Seasons:**
  * **Movies:** Median runtime of **98 minutes** (Range: `3` to `312` mins).
  * **TV Shows:** Median of **1 season** (Mean: `1.8`, Max: `17` seasons), highlighting a strong focus on limited series and single-season releases.
* **Top Producing Markets (Primary Country):** United States (`3,211`), India (`1,008`), United Kingdom (`628`), and Canada (`271`).
* **Top Primary Genres:** Dramas (`1,600`), Comedies (`1,210`), Action & Adventure (`859`), and Documentaries (`829`).

---

## 🚀 How to Run

### 1. Python Analysis
Install the required libraries and run the EDA script:
```bash
pip install pandas matplotlib seaborn
python scripts/eda_analysis.py
```

### 2. SQL Analysis
Import `netflix_data_cleaned.csv` into PostgreSQL, MySQL, BigQuery, or SQLite as a table named `netflix_titles` and execute the queries in `scripts/netflix_queries.sql`.