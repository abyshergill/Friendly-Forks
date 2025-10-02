import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import io
import os

def get_filter_options(df, column_name):
        if column_name in df.columns:
            return sorted(df[column_name].dropna().unique().tolist())
        return []

def main():
    file_path = "uploaded_files/extracted_file.csv"
    df = pd.read_csv(file_path)
    part_col = "Part" if "Part" in df.columns else None
    vendor_col = "Vendor" if "Vendor" in df.columns else None
    size_col = "Size" if "Size" in df.columns else None
    
    date_col = None
    for col in df.columns:
        if "date" in col.lower():
            date_col = col
            break

    col1, col2, col3, col4 = st.columns(4)
    selected_parts = col1.multiselect("Select Part(s)", get_filter_options(df, part_col), key="part_filter")
    selected_vendors = col2.multiselect("Select Vendor(s)", get_filter_options(df, vendor_col), key="vendor_filter")
    selected_sizes = col3.multiselect("Select Size(s)", get_filter_options(df, size_col), key="size_filter")
    selected_dates = col4.multiselect(f"Select {date_col if date_col else 'Date'}(s)", get_filter_options(df, date_col), key="date_filter")

    filtered_df = df.copy()
    if selected_parts and part_col:
        filtered_df = filtered_df[filtered_df[part_col].isin(selected_parts)]
    if selected_vendors and vendor_col:
        filtered_df = filtered_df[filtered_df[vendor_col].isin(selected_vendors)]
    if selected_sizes and size_col:
        filtered_df = filtered_df[filtered_df[size_col].isin(selected_sizes)]
    if selected_dates and date_col:
        filtered_df = filtered_df[filtered_df[date_col].isin(selected_dates)]

    st.write("### Filtered Data")
    st.dataframe(filtered_df)

    qty_col = None
    for col in df.columns:
        if "incoming" in col.lower() and "qty" in col.lower():
            qty_col = col
            break
            
    if qty_col:
        total_qty = filtered_df[qty_col].sum()
        st.write(f"**Total Incoming Quantity:** {total_qty:,.0f}")

if __name__ == "__main__":
    main()