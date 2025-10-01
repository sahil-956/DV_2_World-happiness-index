import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("2015.csv")
    return df

def main():
    st.set_page_config(layout="wide")
    st.title("🌍 World Happiness Report 2015 Explorer")

    df = load_data()

    # Rename columns for easier use
    df = df.rename(columns={
        "Happiness Score": "Happiness_Score",
        "Economy (GDP per Capita)": "GDP_per_Capita"
    })

    # Sidebar
    st.sidebar.header("Filters")
    regions = st.sidebar.multiselect(
        "Select Region(s)", 
        df["Region"].unique(), 
        default=df["Region"].unique()
    )

    df_filtered = df[df["Region"].isin(regions)]

    # Show dataset preview
    st.subheader("📊 Dataset Preview")
    st.dataframe(df_filtered.head(20))

    # Scatter plot: GDP vs Happiness
    st.subheader("💰 GDP per Capita vs Happiness Score")
    fig_scatter = px.scatter(
        df_filtered,
        x="GDP_per_Capita",
        y="Happiness_Score",
        color="Region",
        hover_name="Country",
        size="Happiness_Score",
        labels={"GDP_per_Capita": "GDP per Capita", "Happiness_Score": "Happiness Score"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Choropleth map
    st.subheader("🗺 World Map of Happiness Scores")
    fig_map = px.choropleth(
        df_filtered,
        locations="Country",
        locationmode="country names",
        color="Happiness_Score",
        hover_name="Country",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_map, use_container_width=True)

    # Top 10 happiest countries
    st.subheader("🏆 Top 10 Happiest Countries")
    top10 = df_filtered.nlargest(10, "Happiness_Score")[["Country", "Happiness_Score"]]
    st.table(top10)

    # Correlation heatmap
    st.subheader("📈 Correlation Heatmap")
    numeric_df = df_filtered.select_dtypes(include="number")
    fig_corr = px.imshow(
        numeric_df.corr(),
        text_auto=True,
        title="Correlation Between Factors"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

if __name__ == "__main__":
    main()
