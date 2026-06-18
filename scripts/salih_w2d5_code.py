import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px


st.title("Top 10 sub-categories by Sales")


file = st.file_uploader("Upload superstore_clean.csv", type="csv")

if file is None:
    st.info("Upload a CSV file to get started.")

else:

    df = pd.read_csv(file)

 
    st.write("Columns:", df.columns)
    top_10 = (
        df.groupby("sub_category")["sales"]
        .sum()
        .nlargest(10)
        .sort_values()
    )

  
    fig, ax = plt.subplots(figsize=(10, 6))


    bars = ax.barh(top_10.index, top_10.values)


    ax.bar_label(
        bars,
        labels=[f"${value:,.0f}" for value in top_10.values],
        padding=3
    )

    ax.set_xlabel("Sales ($)")
    ax.set_ylabel("sub-category")
    ax.set_title("Top 10 sub-categories by Sales")

    plt.tight_layout()

 
    st.pyplot(fig)
    plt.close(fig)


fig = px.scatter(
    df,
    x="sales",
    y="profit",
    color="category",
    size="quantity",
    hover_data=["sub_category"],
    title="Sales vs Profit by Product Category"
)

st.plotly_chart(fig, use_container_width=True)
monthly_sales["month"] = pd.Categorical(
    monthly_sales["month"],
    categories=month_order,
    ordered=True
)
monthly_sales = monthly_sales.sort_values("month")

fig = px.line(
    monthly_sales,
    x="month",
    y="sales",
    color="order_year",
    title="Monthly Sales by Year"
)

# Display in Streamlit
st.plotly_chart(fig, use_container_width=True)