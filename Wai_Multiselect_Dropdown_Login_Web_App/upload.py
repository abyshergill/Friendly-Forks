import streamlit as st
import os
import pandas as pd
from io import BytesIO

def UPLOAD_FILE():
    UPLOAD_FOLDER = "uploaded_files"

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    uploaded_file = st.file_uploader("Upload a file", type=[".xlsx", ".xls"])
    if uploaded_file is not None: 
        with st.spinner("Wai, data is uploading, please wait..."):
            try:
                df = pd.read_excel(uploaded_file, sheet_name='All_Master')
                csv_file_location = os.path.join(UPLOAD_FOLDER, "extracted_file.csv")
                
                csv_buffer = BytesIO()
                df.to_csv(csv_buffer, index=False)
                csv_buffer.seek(0)
                
                df.to_csv(csv_file_location, index=False)
                
                st.success("Wai, Data is extracted Successfully")
                
                st.download_button(
                    label="Download Original CSV",
                    data=csv_buffer,
                    file_name="extracted_file.csv", 
                    mime="text/csv"
                )
            except Exception as e:
                st.warning(f" Wai, Some Issue with your Excel File | Error: {e}")

if __name__ == "__main__":
    UPLOAD_FILE()