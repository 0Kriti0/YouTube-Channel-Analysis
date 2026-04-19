# 📊 YouTube Top 1000 Channels Analysis

## 📌 Project Overview
This project performs Exploratory Data Analysis (EDA) and Machine Learning on a dataset of the top 1000 YouTube channels based on subscribers.

The goal is to uncover trends in:
- Channel growth over time  
- Country-wise dominance  
- Content category performance  
- Relationship between videos, views, and subscribers  
- Statistical comparison of channel performance  

---

## 📂 Dataset
- File Used: youtube_top_1000_by_subscribers.csv
- Contains:
  - Channel name (title)
  - Subscribers
  - Views
  - Number of videos
  - Country
  - Topic categories
  - Channel creation date (published_at)

---

## 🧹 Data Cleaning & Preprocessing
Steps performed:
- Converted published_at to datetime format
- Removed missing/null values
- Created new feature:
  - channel_age_years
- Created filtered dataset for country-based analysis
- Extracted clean category from topic_categories

---

## 📊 Exploratory Data Analysis (EDA)

### 🔹 Correlation Analysis
- Heatmap between:
  - Subscribers
  - Views
  - Videos
  - Channel age

### 🔹 Distribution & Outliers
- Histogram of subscribers (in crores)
- Boxplot for outlier detection
- IQR method used to detect extreme values

---

## ❓ Key Questions & Insights

### 1️⃣ Channel Creation Trends
- Analyzed how YouTube channel creation evolved over time (post-2005)
- Line plot shows growth patterns of top channels

### 2️⃣ Top Countries by Subscribers
- Aggregated subscribers by country
- Top 10 countries visualized (in crores)

### 3️⃣ Top Content Categories
- Extracted categories from raw data
- Identified top-performing content types

### 4️⃣ Predictive Modeling

#### 📌 Videos → Subscribers
- Linear Regression model
- Input: Number of videos  
- Output: Subscribers (in crores)

#### 📌 Views → Subscribers
- Linear Regression model  
- Input: Views (in billions)  
- Output: Subscribers (in crores)

Metrics Used:
- Mean Squared Error (MSE)
- R² Score

---

### 5️⃣ Hypothesis Testing
Compared subscribers:
- Before 2015  
- After 2015  

Test Used:
- Two-sample independent t-test  

Hypotheses:
- H0: No difference in means  
- H1: Significant difference exists  

---

### 6️⃣ Top 10 Channels Analysis
Visualized top channels based on:
- Subscribers  
- Views  
- Number of videos  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Seaborn  
- Matplotlib  
- Scikit-learn  
- SciPy  

---

## 📈 Key Learnings
- Strong relationship between views and subscribers  
- Content category significantly impacts growth  
- Older channels don’t always dominate  
- Views are a better predictor than number of videos  

---

## ▶️ How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
python your_script_name.py
```

## 👤 Author
Kriti Pandey
