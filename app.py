import streamlit as st
from src.bank import Bank

st.set_page_config(page_title="Bank App", layout="centered")

# Initialize bank instance in session state
if 'bank' not in st.session_state:
    st.session_state.bank = Bank()

st.title("🏦 Simple Bank App")

menu = st.sidebar.selectbox("Menu", ["Create Account", "Deposit", "Withdraw", "Check Balance"])

if menu == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Account Holder Name")
    initial = st.number_input("Initial Deposit", min_value=0.0, step=10.0)
    if st.button("Create"):
        acc_num = st.session_state.bank.create_account(name, initial)
        st.success(f"Account created! Account Number: {acc_num}")

elif menu == "Deposit":
    st.header("Deposit Money")
    acc_num = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0.0, step=10.0)
    if st.button("Deposit"):
        try:
            st.session_state.bank.deposit(acc_num, amount)
            st.success("Deposit successful!")
        except Exception as e:
            st.error(str(e))

elif menu == "Withdraw":
    st.header("Withdraw Money")
    acc_num = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0.0, step=10.0)
    if st.button("Withdraw"):
        try:
            st.session_state.bank.withdraw(acc_num, amount)
            st.success("Withdrawal successful!")
        except Exception as e:
            st.error(str(e))

elif menu == "Check Balance":
    st.header("Check Account Balance")
    acc_num = st.text_input("Account Number")
    if st.button("Check"):
        try:
            balance = st.session_state.bank.get_balance(acc_num)
            st.info(f"Balance: ₹{balance}")
        except Exception as e:
            st.error(str(e))