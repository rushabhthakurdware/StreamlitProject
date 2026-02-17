import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

# -------------------- TITLE SECTION --------------------
st.title("My First Commit")
st.write("👋 Hello Rushabh")
st.text("Let's start!")

# -------------------- GREETING SECTION --------------------
name = st.text_input("Enter your name:", key="main_name")
if st.button("Greet", key="greet_btn"):
    st.success(f"Hello, {name}!")

# -------------------- SIDEBAR --------------------
st.sidebar.title("Navigation")
st.sidebar.image("https://via.placeholder.com/300", caption="Sample Image")
st.sidebar.video("https://www.youtube.com/watch?v=H-JTC5P6RKU")

# -------------------- FILE UPLOADER --------------------
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded CSV Data")
    st.dataframe(df)

    numeric_cols = df.select_dtypes(include=np.number).columns
    if len(numeric_cols) >= 2:
        st.subheader("Line Chart")
        st.line_chart(df[numeric_cols])

        st.subheader("Bar Chart")
        st.bar_chart(df[numeric_cols])
    else:
        st.warning("Uploaded CSV must have at least 2 numeric columns.")
else:
    df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
    st.subheader("Random Data")
    st.dataframe(df)
    st.line_chart(df)
    st.bar_chart(df)

# -------------------- WIDGETS SECTION --------------------
st.text_input("What's your name?", key="extra_name")
st.text_area("Write something...", key="extra_text")
st.number_input("Pick a number", min_value=0, max_value=100, key="number")
st.slider("Choose a range", 0, 100, key="slider")
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"], key="fruit")
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"], key="toppings")
st.radio("Pick one", ["Option A", "Option B"], key="radio")
st.checkbox("I agree to the terms", key="terms")

if st.checkbox("Show Details", key="details"):
    st.info("Here are more details...")

# -------------------- LOGIN FORM --------------------
with st.form("login_form"):
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")

# -------------------- COLUMNS --------------------
col1, col2 = st.columns(2)

with col1:
    st.button("Press me in Column 1", key="col1_btn")

with col2:
    st.button("Press me in Column 2", key="col2_btn")

# -------------------- EXPANDER --------------------
with st.expander("See Explanation"):
    st.write("Here is a hidden message inside the expander.")

# -------------------- MATPLOTLIB CHART --------------------
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)

# -------------------- PLOTLY CHART --------------------
iris_df = px.data.iris()
fig2 = px.scatter(iris_df, x="sepal_width", y="sepal_length", color="species")
st.plotly_chart(fig2)
