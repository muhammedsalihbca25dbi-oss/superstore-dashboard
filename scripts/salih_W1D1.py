import streamlit as st
from datetime import datetime

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Salih Portfolio Dashboard",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------------
# HERO SECTION
# -----------------------------------
st.title("🚀 Salih | Data Analyst & Web Developer")

st.markdown("""
### Welcome to my professional portfolio dashboard

I am passionate about **Data Analytics**, **Python Development**,
**Streamlit Applications**, and **Business Intelligence Solutions**.
""")

st.caption(f"Last Updated: {datetime.now().strftime('%d %B %Y')}")

st.markdown("---")

# -----------------------------------
# ABOUT ME
# -----------------------------------
st.header("👨‍💻 About Me", divider="blue")

st.write("""
I am an aspiring Data Analyst and Web Developer who enjoys transforming
raw data into meaningful insights. I love building interactive dashboards,
analyzing business performance, and creating modern web applications.
""")

# -----------------------------------
# PROFILE METRICS
# -----------------------------------
st.header("📈 Professional Summary", divider="green")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Projects", "15+")

with col2:
    st.metric("Python Skills", "Advanced")

with col3:
    st.metric("Dashboards Built", "10+")

with col4:
    st.metric("Learning Status", "Active")

# -----------------------------------
# SKILLS
# -----------------------------------
st.header("🛠 Technical Skills", divider="orange")

st.markdown("""
- **Python**
- **Pandas**
- **NumPy**
- **Streamlit**
- **SQL**
- **Data Visualization**
- **Power BI**
- **Excel Analytics**
""")

# -----------------------------------
# CERTIFICATIONS
# -----------------------------------
st.header("🏆 Certifications", divider="violet")

st.markdown("""
- Python for Data Analysis
- SQL Fundamentals
- Data Visualization
- Business Intelligence Basics
""")



# -----------------------------------
# STATUS
# -----------------------------------
st.header("📊 Current Status", divider="blue")

st.markdown("""
:green[✓ Available for Freelance Projects]

:blue[✓ Learning Advanced Data Analytics]

:orange[✓ Building Streamlit Applications]

:red[✓ Constantly Improving Skills]
""")

# -----------------------------------
# CODE EXAMPLE
# -----------------------------------
st.header("💻 Favorite Python Snippet", divider="green")

st.code("""
import pandas as pd

df = pd.read_csv("sales.csv")

sales = df["Sales"].sum()

print(f"Total Sales: ${sales:,.2f}")
""", language="python")

# -----------------------------------
# FORMULA
# -----------------------------------
st.header("📐 Business Formula", divider="orange")

st.latex(
    r'\text{Profit Margin}=\frac{\text{Profit}}{\text{Sales}}\times100'
)

# -----------------------------------
# CONTACT
# -----------------------------------
st.header("📞 Contact", divider="violet")

st.markdown("""
📧 Email: salih@email.com

📱 Phone: +91 9966558844

🌐 Portfolio: www.yourwebsite.com""")



# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")

st.caption(
    "Built with Streamlit | Week 1 Day 1 Project | Professional Portfolio Dashboard"
)