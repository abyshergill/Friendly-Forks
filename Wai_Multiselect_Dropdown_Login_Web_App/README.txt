# 📊 WAI Project – Master Data Uploader & Filter

This project is a **Streamlit-based web application** for uploading, extracting, and filtering **ORT Master Data** from Excel files.  
It provides a simple **login system**, **data upload**, and **advanced filtering** with visualization and CSV export support.

---

## 🚀 Features

- 🔐 **User Authentication** (credentials stored in `users.txt`)  
- 📤 **Excel Upload** (extracts data from `All_Master` sheet and saves as CSV)  
- 🔎 **Interactive Filtering**:
  - Filter by **Model**
  - Select **Component** (Vendor & Date Code info)
  - Choose **Vendor** and **Date Code**
- 📈 **Data Insights**:
  - Tabular filtered view with pagination
  - Histogram of model quantities
- 💾 **Download Options**:
  - Filtered dataset as CSV
  - Extracted raw data as CSV

---

## 🗂 Project Structure

├── main.py # Main Streamlit app (authentication + navigation)
├── upload.py # Upload Excel, extract & convert to CSV
├── filterlogic.py # Data filtering and visualization logic
├── users.txt # Stores username:password for authentication
├── uploaded_files/ # Folder for storing extracted CSV files
├── icon/ # Project icons (used in Streamlit page config)
└── README.md # Project documentation

yaml
Copy code

---

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📌 Usage
Add your credentials inside users.txt (format: username:password):

pgsql
Copy code
admin:admin
user:password
Run the Streamlit app:

bash
Copy code
streamlit run main.py
Open the browser at: http://localhost:8501

🖼 Screenshots
🔑 Login Page

📤 Upload Excel

🔎 Filter Data

📦 Dependencies
Streamlit

Pandas

Plotly

st-aggrid

Install them with:

bash
Copy code
pip install streamlit pandas plotly streamlit-aggrid
👨‍💻 Author
Designed & Maintained by Kuldeep Singh (Aby)
📅 2025

📜 License
This project is licensed under the MIT License – free to use and modify.

yaml
Copy code

---

Do you want me to also generate a **`requirements.txt`** for this repo so that anyone can install dependencies quickly?











ChatGPT can make mistakes. Check important