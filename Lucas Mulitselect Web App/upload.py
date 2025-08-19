import streamlit as st
import os
import pandas as pd

def UPLOAD_FILE():
	UPLOAD_FOLDER = "uploaded_files"

	os.makedirs(UPLOAD_FOLDER, exist_ok=True)

	uploaded_file = st.file_uploader("Upload a file", type=[".xlsx", ".xls"])
	if uploaded_file is not None:	
		try:
			df = pd.read_excel(uploaded_file, sheet_name='TARGET')
			csv_file_location = os.path.join(UPLOAD_FOLDER, "extracted_file.csv")

			for file in os.listdir(UPLOAD_FOLDER):
				os.remove(csv_file_location)
				st.success("Lucas, Old File is removed Successfully")

			df.to_csv(csv_file_location)
			st.success("Lucas, Data is extracted Successfully")

		except Exception as e:
			st.warning(f"Lucas, Some Issue with your Excel File | Error {e}")

if __name__ == "__main__":
	UPLOAD_FILE()