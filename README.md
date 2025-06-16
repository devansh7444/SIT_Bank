# 💰 Sit Bank – A Streamlit Banking Application

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange?logo=streamlit)](https://streamlit.io)

🔗 *Live App*: [Click here to use Sit Bank](https://devansh.streamlit.app/)

---

## 📸 Screenshots

| Interface           | Screenshot |
|---------------------|------------|
| 🏠 Home Page         | ![Home Page](https://github.com/Xtrmcoder/Sit_Bank/blob/a7289ea176d4e9b79cec91bf682afc4536e7b6bf/Sit%20Bank%20Interface.png) |

> 📌 Replace the placeholders (your-image-link-here) with the actual URLs to your screenshots (e.g., from Imgur, GitHub, or local images/ folder).

---
## 📌 Overview

*Sit Bank* is a simple, interactive, and lightweight banking simulation application built using *Python* and *Streamlit*. It allows users to perform essential banking operations in real-time, including viewing balances, depositing funds, and making withdrawals.

This project demonstrates object-oriented design, modular Python coding, and Streamlit-based web development.

---

## ✨ Features

- 👤 *Account Interface*
  - Basic account creation and management via backend logic.
  
- 💵 *Balance Inquiry*
  - View your current bank account balance instantly.

- ➕ *Deposit Money*
  - Deposit any amount into your virtual account.

- ➖ *Withdraw Money*
  - Withdraw money with real-time balance verification.

- ⚡ *Responsive & Minimal UI*
  - Built with Streamlit for a fast and intuitive experience.

---

## 🛠 Tech Stack

| Technology | Description |
|------------|-------------|
| 🐍 Python | Core banking logic |
| 🧱 OOP | Account and transaction abstraction |
| 🌐 Streamlit | Web app interface |

---

## 📂 Project Structure

```bash
sit-bank/
├── app.py                # Main Streamlit app file
├── Banking/
│   ├── account.py        # Account class definitions (BankAccount, SavingsAccount, etc.)
│   └── transaction.py    # Functions to deposit and withdraw
├── src/
│   └── utils.py          # Utility functions (optional or helper methods)
├── README.md             # Documentation file
