import streamlit as st
import pandas as pd
from datetime import date

# Title
st.title("📚 Student Grade Dashboard")

# Data
data = {
    "Name": ["Aisha", "Bob", "Clara", "Dev", "Eva",
             "Finn", "Grace", "Hiro", "Ines", "Jay"],

    "Math": [88, 52, 76, 91, 43, 67, 85, 59, 78, 95],

    "Science": [72, 45, 88, 83, 38, 71, 90, 62, 55, 80],

    "English": [65, 70, 82, 77, 60, 58, 74, 88, 91, 73],

    "Art": [90, 85, 60, 55, 78, 92, 68, 75, 83, 61]
}

df = pd.DataFrame(data)

# Average column
df["Average"] = (
    df[["Math", "Science", "English", "Art"]]
    .mean(axis=1)
    .round(1)
)

# Student count
st.write(f"Total Students: {len(df)}")

# KPI Metrics
c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Class Average",
    round(df["Average"].mean(), 1)
)

c2.metric(
    "Highest Average",
    df["Average"].max()
)

c3.metric(
    "Lowest Average",
    df["Average"].min()
)

c4.metric(
    "Above 70",
    (df["Average"] >= 70).sum()
)

# Styled DataFrame
st.header("Student Marks")

styled_df = df.style.map(
    lambda x: "color:green"
    if x >= 70
    else "color:red",
    subset=["Average"]
)

st.dataframe(
    styled_df,
    hide_index=True,
    use_container_width=True
)

# Top 3 Students
st.header("Top 3 Students")

top3 = (
    df.sort_values(
        "Average",
        ascending=False
    )
    .head(3)
)

st.table(
    top3[["Name", "Average"]]
)

# JSON Summary
st.header("Subject Summary")

summary = {
    "Math": {
        "min": int(df["Math"].min()),
        "max": int(df["Math"].max()),
        "mean": round(df["Math"].mean(), 1)
    },
    "Science": {
        "min": int(df["Science"].min()),
        "max": int(df["Science"].max()),
        "mean": round(df["Science"].mean(), 1)
    },
    "English": {
        "min": int(df["English"].min()),
        "max": int(df["English"].max()),
        "mean": round(df["English"].mean(), 1)
    },
    "Art": {
        "min": int(df["Art"].min()),
        "max": int(df["Art"].max()),
        "mean": round(df["Art"].mean(), 1)
    }
}

st.json(summary)

# Footer
st.markdown("---")
st.caption(
    f"Salih | Student Grade Dashboard | {date.today()}"
)