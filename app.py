import streamlit as st
import time
from datetime import datetime

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Healthy Food Reminder", page_icon="🥗")

# ----------------- TITLE -----------------
st.title("🥗 Healthy Food Suggestion Project with Reminder")
st.write("Healthy food suggestions based on time with reminders.")

# ----------------- FOOD LISTS (200 ITEMS) -----------------
breakfast_foods = [
    "Oatmeal", "Boiled Eggs", "Fruit Salad", "Whole Wheat Toast",
    "Greek Yogurt", "Smoothie", "Banana", "Apple",
    "Avocado Toast", "Porridge"
] * 5

lunch_foods = [
    "Brown Rice", "Grilled Chicken", "Vegetable Curry", "Dal",
    "Salad Bowl", "Chickpeas", "Quinoa", "Fish Curry",
    "Beans", "Steamed Vegetables"
] * 5

snack_foods = [
    "Nuts", "Fruit Bowl", "Yogurt", "Popcorn",
    "Dates", "Roasted Peanuts", "Energy Bar",
    "Sprouts", "Smoothie", "Dark Chocolate"
] * 5

dinner_foods = [
    "Vegetable Soup", "Grilled Fish", "Steamed Chicken",
    "Chapati", "Dal", "Salad", "Paneer",
    "Boiled Vegetables", "Rice & Vegetables", "Light Curry"
] * 5

# ----------------- TIME BASED SUGGESTION -----------------
 from datetime import datetime, timedelta
current_hour = (datetime.utcnow() + timedelta(hours=5)).hour
if 6 <= current_hour < 12:
    st.subheader("🍳 Breakfast Time")
    food_list = breakfast_foods
elif 12 <= current_hour < 17:
    st.subheader("🍛 Lunch Time")
    food_list = lunch_foods
elif 17 <= current_hour < 20:
    st.subheader("🍎 Snack Time")
    food_list = snack_foods
else:
    st.subheader("🍽 Dinner Time")
    food_list = dinner_foods

st.write("### Recommended Healthy Foods:")
st.write(food_list[:10])

# ----------------- 20 SECOND REMINDER -----------------
st.write("### ⏰ 20-Second Reminder")

if st.button("Start 20-Second Reminder"):
    with st.spinner("Waiting 20 seconds..."):
        time.sleep(20)
    st.success("✅ Time to eat healthy food!")

