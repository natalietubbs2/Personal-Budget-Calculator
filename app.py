import streamlit as st
import pandas as pd

st.set_page_config(page_title="Personal Budget Calculator", page_icon="💰")
st.title("💰 Personal Monthly Budget Calculator")
st.write("Enter your monthly income and expenses to understand your budget.")

# Inputs are restricted to nonnegative amounts.
income = st.number_input("Monthly income ($)", min_value=0.0, value=3000.0, step=50.0)
categories = ["Rent", "Groceries", "Transportation", "Entertainment", "Other"]
expenses = {}
for category in categories:
    expenses[category] = st.number_input(f"{category} ($)", min_value=0.0, value=0.0, step=10.0)

# Calculate the monthly budget.
total_expenses = sum(expenses.values())
remaining = income - total_expenses
savings_percentage = (remaining / income * 100) if income > 0 else None

st.subheader("Your budget summary")
st.metric("Total expenses", f"${total_expenses:,.2f}")
st.metric("Money remaining", f"${remaining:,.2f}")
if savings_percentage is None:
    st.info("Enter income above $0 to calculate your savings percentage.")
else:
    st.metric("Income remaining (%)", f"{savings_percentage:.1f}%")

if total_expenses > income:
    st.warning("Your expenses exceed your monthly income!")

st.subheader("Spending by category")
if total_expenses > 0:
    chart_data = pd.DataFrame({"Category": categories, "Amount ($)": [expenses[c] for c in categories]})
    st.bar_chart(chart_data.set_index("Category"))
else:
    st.info("Enter expenses to see your spending chart.")

st.caption("This is a simple budgeting tool. Remaining income assumes all unspent money is saved.")
