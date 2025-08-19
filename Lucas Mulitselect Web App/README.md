## Lucas Mulitselect : An Excel Data Filter Web App
### Objective
The Lucas web application addresses the inefficiency of sharing large Excel files among multiple users by providing a centralized solution for data filtering and access. Users can upload a single Excel file to a virtual machine, and then anyone with access can filter, view, and download the data without needing to share the large file itself. This improves efficiency and is especially beneficial for older systems with limited memory that may struggle with large Excel files.

### How It Works
The application features two main pages: 
* **Upload**
* **Extract**
---

#### Upload Page
On this page, you can upload a new Excel file. The application performs the following actions:
- **File Validation:** It checks if the uploaded file is either an `.xlsx or .xls format.`
- **Worksheet Extraction:** It looks for a worksheet named `"TARGET"` within the Excel file.
- **File Management:** It removes any old extracted_file.csv from the uploaded_files folder.
- **Data Conversion:** It converts the data from the `"TARGET"` worksheet into a new `extracted_file.csv` and saves it in the uploaded_files folder.

 ![ ](assests\upload.jpg)

#### Extract Page
This page is where the data filtering takes place.
- The data from the `extracted_file.csv` is displayed.
- You can use multi-select filters for the following columns: Part(s), Vendor(s), Size(s), and Incoming Date(s). The data in the table updates automatically based on your selections.

 ![ ](assests\extract.jpg)

- The total incoming quantity is displayed at the bottom of the page, calculated from the Incoming Quantity column based on your filtered results.

 ![ ](assests\total_quantity.jpg)

#### Other Options
The application provides additional functionalities for better data interaction:
- **Download:** You can download the filtered data.
- **Zoom:** You can zoom in and out of the displayed table for better viewing.

 ![ ](assests\other_options.jpg)

### Project Structure
The expected project directory structure is as follows:
```bash
Multiselect_Streamlit_App/
├── main.py                 # The main application file that runs filterlogic.py and upload.py
├── icon/
│   └── icon.png            # Application icon (Optional)
├── assets/                 
│   └── extract.jpg
│   └── other_options.jpg
│   └── total_quanity.jpg
│   └── upload.jpg
├── uploaded_files/
│   └── extracted_file.csv  # The extracted data is saved here as a .csv file
├── filterlogic.py          # Contains the logic for filtering the data
├── upload.py               # Handles file uploading and data extraction
├── README.md               
├── samplefile.xlsx
├── license.md
└── requirements.txt
```
## Short Video How to use

[![Watch the video](assests\upload.jpg)](https://www.youtube.com/watch?v=JGvEicmJsOo&feature=youtu.be)

### License
This project is licensed under the MIT License.

### Creator Information:
Email: shergillkuldeep@outlook.com