import streamlit as st
from PIL import Image
def check_eligibility(age, income):
    if age >= 18 and income >= 100000:
        return True
    else:
        return False

def calculate_interest(age, income):
    if age < 25:
        if income < 100000:
            return 8.5
        else:
            return 7.5
    elif age >= 25 and age < 40:
        if income < 100000:
            return 7.5
        else:
            return 6.5
    else:
        return 6.0

def loan_management():
    st.title("All India Loan Management System")
    st.write("Fill in the following details to check your loan eligibility and interest rate:")
    st.image("bank.jfif")

    age = st.slider("Your Age:", 18, 70)
    income = st.number_input("Your Annual Income:", min_value=0)

    if st.button("Check Eligibility"):
        if check_eligibility(age, income):
            st.success("Congratulations! You are eligible for a loan. and bhut paise denge")
            interest_rate = calculate_interest(age, income)
            st.write("Based on your details, the interest rate for your loan is:", interest_rate, "%")
            st.write("apke sath jldi baat hogi dhanyawad.")
        else:
            st.error("Sorry, agli baar aye.")

if __name__ == "__main__":
    loan_management()
