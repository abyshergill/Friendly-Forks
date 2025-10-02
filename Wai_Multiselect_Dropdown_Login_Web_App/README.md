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
```bash
├── main.py 
├── upload.py 
├── filterlogic.py 
├── users.txt 
├── requriments.txt 
├── license.txt 
├── uploaded_files/ 
├── icon/ 
└── README.md 
```

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abyshergill/utility_space/tree/main/Wai_Multiselect_Dropdown_Login_Web_App.git
   cd your-repo
- Create a virtual environment (recommended):

  ```bash
  python -m venv venv
  source venv/bin/activate  
  venv\Scripts\activate     
  ```
- Install 📦 Dependencies :
  ```bash
  pip install -r requirements.txt
  ```

## 📌 Usage
- Add your credentials inside users.txt (format: username:password):
  ```bash
  # inside user.text
  admin:admin
  user:password
  ```
- Run the Streamlit app:

  ```bash
  streamlit run main.py
  Open the browser at: http://localhost:8501
  ```
## 🖼 Screenshots
🔑 Login Page

![Login](assests\login.jpg)

📤 Upload Excel

![upload](assests\upload.jpg)

🔎 Filter Data

![Filter Data](assests\filter.jpg)

## 👨‍💻 Author
- Designed & Maintained by Kuldeep Singh (Aby) 📅 2025
- Email : shergillkuldeep@outlook.com

## 📜 License
This project is licensed under the MIT License – free to use and modify.

---
