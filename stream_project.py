# trip_day2.py
# A minimal Streamlit "Trip Day 2" planner you can learn from, line by line.

import datetime as dt
import pandas as pd
import streamlit as st

# ---------- Page setup ----------
st.set_page_config(page_title="Trip Planner - Day 2", page_icon="🗺️", layout="centered")
st.title("🗺️ Trip Planner — Day 2")
st.caption("Plan your day, estimate costs, and export your schedule.")

# ---------- Sidebar inputs ----------
st.sidebar.header("Trip Inputs")
trip_date = st.sidebar.date_input("Date", value=dt.date.today())
destination = st.sidebar.text_input("Destination", value="Andaman (Example)")
budget = st.sidebar.number_input("Budget (₹)", value=3000, step=100)

st.sidebar.write("---")
st.sidebar.write("**Hint:** Adjust activities below and export as CSV.")

# ---------- Activity builder ----------
st.subheader("Build Your Day 2 Schedule")

default_rows = [
    {"Time": "08:00", "Activity": "Breakfast", "Location": "Hotel", "Cost (₹)": 200},
    {"Time": "10:00", "Activity": "Beach Visit", "Location": "Radhanagar Beach", "Cost (₹)": 0},
    {"Time": "13:00", "Activity": "Lunch", "Location": "Local Restaurant", "Cost (₹)": 350},
    {"Time": "16:00", "Activity": "Snorkeling", "Location": "Elephant Beach", "Cost (₹)": 1200},
    {"Time": "19:30", "Activity": "Dinner", "Location": "Seafood Place", "Cost (₹)": 600},
]

df = pd.DataFrame(default_rows)

st.write("Edit the table to match your plan:")
edited = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True,
    key="schedule_editor"
)

# ---------- Summary ----------
total_cost = int(edited["Cost (₹)"].fillna(0).sum())
remaining = budget - total_cost

st.write("### Summary")
col1, col2, col3 = st.columns(3)
col1.metric("Date", trip_date.strftime("%Y-%m-%d"))
col2.metric("Total Cost (₹)", f"{total_cost:,}")
col3.metric("Budget Left (₹)", f"{remaining:,}")

if remaining < 0:
    st.error("You are over budget. Consider reducing some costs.")

# ---------- Export ----------
csv = edited.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Download Day 2 Schedule (CSV)",
    data=csv,
    file_name=f"day2_schedule_{trip_date}.csv",
    mime="text/csv"
)

st.success(f"Trip planned for **{destination}** on **{trip_date}**. Happy travels!")
