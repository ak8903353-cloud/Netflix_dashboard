# Netflix Dashboard 

## 📌 Project Overview

The **Netflix  Dashboard** is a Python-based data analysis and visualization project developed using Streamlit, Pandas, and Plotly Express.

The project analyzes the Netflix titles dataset and presents useful insights about movies and TV shows through an interactive dashboard. Users can apply different filters, explore visualizations, view key statistics, and search for specific titles.

The main objective of this project is to understand the Netflix content catalogue through data analysis and interactive visual representation.

## 🎯 Project Objectives

- Analyze the distribution of Movies and TV Shows.
- Explore Netflix content based on country and rating.
- Understand content distribution across different release years.
- Identify popular genres in the dataset.
- Display important statistics through interactive charts.
- Provide filters to make data exploration easier.
- Allow users to search for specific Netflix titles.

## ✨ Key Features

- **Interactive Dashboard:** Displays Netflix dataset insights in a user-friendly interface.
- **Content Type Filter:** Filter data between Movies and TV Shows.
- **Country Filter:** Explore titles based on selected countries.
- **Rating Filter:** Analyze content according to ratings.
- **Release Year Filter:** Select a specific range of release years.
- **Key Metrics:** Displays total titles, movies, TV shows, and countries.
- **Interactive Visualizations:** Includes pie charts, line charts, and bar charts.
- **Genre Analysis:** Shows the distribution of different genres.
- **World Map Visualization:** Displays country-wise content distribution.
- **Title Search:** Search for specific movies or TV shows.
- **Dataset Preview:** View the filtered dataset directly in the dashboard.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12.10 | Programming language |
| Pandas | Data loading, processing, filtering and analysis |
| Streamlit | Interactive dashboard development |
| Plotly Express | Interactive charts and geographical visualization |
| CSV | Dataset storage |
| GitHub | Project version control and repository hosting |

## 📂 Project Structure

```text
Netflix-Data-Analysis/
│
├── main.py
│   └── Main Python application and dashboard code
│
├── netflix_titles.csv
│   └── Netflix titles dataset
│
├── requirements.txt
│   └── Required Python libraries
│
└── README.md
    └── Project documentation
```

## 📊 Dataset Information

The project uses the Netflix Titles dataset obtained from Kaggle.

- **Dataset Name:** Netflix Titles
- **File Name:** netflix_titles.csv
- **Total Records:** 8,807
- **Total Columns:** 12
- **Content Types:** Movies and TV Shows
- **Release Year Range:** 1925–2021

The dataset contains information such as:
- Show ID
- Type
- Title
- Director
- Cast
- Country
- Date Added
- Release Year
- Rating
- Duration
- Listed In (Genres)
- Description

**Note:** This dataset is a historical snapshot and does not represent Netflix's current catalogue. It does not contain actual viewer counts or viewing statistics.

## ⚙️ Installation and Setup

Follow these steps to run the project on your local computer.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Replace `YOUR_GITHUB_REPOSITORY_LINK` with your actual GitHub repository URL.

### Step 2: Open the Project Folder

```bash
cd Netflix-Data-Analysis
```

### Step 3: Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Run the Dashboard

```bash
streamlit run main.py
```

The dashboard will open in your default web browser.

If it does not open automatically, use the local URL displayed in the terminal. The default address is:

```text
http://localhost:8501
```

## 📦 Requirements

The project uses the following Python libraries:

```text
pandas
streamlit
plotly
```

These dependencies are listed in `requirements.txt`.

## 📈 Dashboard Analysis

The dashboard provides the following analysis:

1. Movies and TV Shows distribution.
2. Content added over different years.
3. Country-wise content distribution.
4. Rating-wise content analysis.
5. Genre-wise content distribution.
6. Geographical visualization of Netflix titles.
7. Search and filtering of individual titles.

## 🔮 Future Enhancements

The project can be improved in the future by adding:

- Additional filters for genre, director, and cast.
- Improved data cleaning and preprocessing.
- Downloadable filtered datasets.
- Cloud deployment for online access.
- Content-based recommendation features after further development.

## ⚠️ Project Limitations

- The dataset is a static snapshot and is not updated automatically.
- Some dataset columns contain missing values.
- The analysis is descriptive and does not predict future trends.
- No database or external API integration is implemented.
- The project does not use Machine Learning algorithms for prediction.

## 👨‍💻 Author

**Aryan Kumar**  
B.Tech – Computer Science and Engineering

## 📚 Dataset Source

Kaggle – Netflix Titles Dataset

https://www.kaggle.com/

---

⭐ If you find this project useful, feel free to explore the code and dashboard.
