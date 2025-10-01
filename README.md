
# 🌍 World Happiness Report 2015 Explorer

This project is an **interactive data visualization dashboard** built using **Streamlit**, **Pandas**, and **Plotly**.  
It allows users to explore the **World Happiness Report 2015 dataset** by filtering regions, analyzing correlations, 
and visualizing happiness scores across countries.  

The application is designed to provide meaningful insights into global happiness trends.

---

## 📂 Project Structure

```
├── app.py          # Main Streamlit application
├── 2015.csv        # Dataset: World Happiness Report 2015
└── README.md       # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone or Download**
   Place `app.py` and `2015.csv` in the same folder.

2. **Install Dependencies**
   ```bash
   pip install streamlit pandas plotly
   ```

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

4. Open browser at: [http://localhost:8501](http://localhost:8501)

---

## 📊 Features of the Dashboard

- **Dataset Preview**: Inspect the first 20 rows of the filtered dataset.  
- **Scatter Plot (GDP vs Happiness)**: Visualize the relationship between economic prosperity and happiness.  
- **World Map (Choropleth)**: Compare happiness scores globally.  
- **Top 10 Happiest Countries**: Identify top-performing nations in happiness.  
- **Correlation Heatmap**: Explore relationships between happiness factors.  

---

## 📈 Real-World Insights from Each Visualization

1. **Scatter Plot (GDP vs Happiness):**  
   Shows how economic prosperity correlates with happiness. Wealthier nations generally report higher happiness, 
   though social and cultural factors also matter.

2. **World Map (Choropleth):**  
   Provides a geographical view of happiness. Highlights regions like the Nordics with consistently high scores, 
   and contrasts them with less stable regions.

3. **Top 10 Happiest Countries:**  
   Lists global leaders in happiness. Useful for studying policies and practices that may inspire improvements 
   in other regions.

4. **Correlation Heatmap:**  
   Identifies which variables (GDP, life expectancy, freedom, etc.) most strongly influence happiness.  
   Offers data-backed insights for policy-making.

---

## 🧩 Code Overview

### `load_data()`
- Reads the CSV dataset.  
- Cached for performance efficiency.

### `main()`
- Initializes the Streamlit app.  
- Handles layout, filters, charts, and output displays.  

### Sidebar Filters
- Allows filtering by region.  
- Updates dataset and visualizations dynamically.

### Visualizations
- Scatter plot, choropleth map, top 10 happiest countries table, and correlation heatmap.

---

## 📖 Dataset Information

- Source: [World Happiness Report 2015](https://worldhappiness.report/)  
- Key Columns:  
  - `Country`, `Region`, `Happiness Score`, `Economy (GDP per Capita)`  
  - `Family`, `Health (Life Expectancy)`, `Freedom`, `Generosity`, 
    `Trust (Government Corruption)`, `Dystopia Residual`  

---

## 🛠 Requirements

- Python 3.8+  
- Libraries: `streamlit`, `pandas`, `plotly`

---

## 📜 License

This project is for **educational purposes**.  
Dataset belongs to the authors of the *World Happiness Report*.

