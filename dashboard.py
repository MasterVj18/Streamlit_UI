import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------
# Dashboard Title & Description
# -------------------------------
st.set_page_config(page_title="Sample Dashboard", layout="wide")
st.title("📊 Sample Dashboard UI")
st.markdown("This is a simple interactive dashboard created with Streamlit. You can use it as a template for ML apps or data visualization.")

# -------------------------------
# Sidebar Menu
# -------------------------------
st.sidebar.header("🔧 Controls")

# Dropdown
selected_option = st.sidebar.selectbox(
    "Select an Option",
    ["Option 1", "Option 2", "Option 3"]
)

# Slider
slider_value = st.sidebar.slider("Adjust a Value", 0, 100, 50)

# Text Input
user_input = st.sidebar.text_input("Enter some text", "Hello Streamlit!")

# Button
if st.sidebar.button("Submit"):
    st.sidebar.success(f"You entered: {user_input}")

# -------------------------------
# Main Dashboard Area
# -------------------------------
st.subheader("📈 Example Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

st.subheader("📊 Example Bar Chart")
st.bar_chart(chart_data)

# -------------------------------
# Placeholder for a Data Table
# -------------------------------
st.subheader("📋 Sample Data Table")
data = pd.DataFrame({
    "Feature 1": np.random.rand(10),
    "Feature 2": np.random.rand(10),
    "Feature 3": np.random.randint(0, 100, size=10)
})
st.dataframe(data, use_container_width=True)

# -------------------------------
# User Feedback
# -------------------------------
st.success(f"✅ You selected: {selected_option} and adjusted slider to {slider_value}")
