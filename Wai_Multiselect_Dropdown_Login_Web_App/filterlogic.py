import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import io
import os
import plotly.express as px
				
def load_data(file_path):
    return pd.read_csv(file_path, low_memory=False)


def apply_filters(df, filters):
    filtered_df = df.copy()
    for column, selected_values in filters.items():
        filtered_df = filtered_df[filtered_df[column].isin(selected_values)]
    return filtered_df

def select_model(main_df):
    filters = {}
    df_model = main_df[['config_sn_list']]
    for column in df_model.columns:
            unique_values = df_model[column].unique().tolist()
            selected_models = st.multiselect(f"Select Model", unique_values, default=None)
            filters[column] = selected_models
            return selected_models			
			
def selected_component():
    component_mapping = {
        'COMPONENT_1': ('COMPONENT_1_Vender_Code', 'COMPONENT_1_Vender_DC'),
        'COMPONENT_2': ('COMPONENT_2_Vender_Code', 'COMPONENT_2_Vender_DC'),
    }

    selected_component = st.selectbox("Select Component: ", list(component_mapping.keys()))
    vendor_information, date_code_information = component_mapping[selected_component]
    
    return vendor_information, date_code_information


def selected_vendor(vendor_info, main_df):
    filters = {}
    df_model = main_df[[vendor_info]]
    for column in df_model.columns:
        unique_values = df_model[column].unique().tolist()
        selected_vendor = st.selectbox(f"Select Vendor", unique_values)
        filters = selected_vendor
        return selected_vendor

def selected_dc(date_code, main_df):
    filters = {}
    df_model = main_df[[date_code]]
    for column in df_model.columns:
            unique_values = df_model[column].unique().tolist()
            selected_dc = st.multiselect(f"Select DC", unique_values)
            filters[column] = selected_dc
            return selected_dc
          
def main():
    file_path = "uploaded_files/extracted_file.csv"

    if file_path is not None:
        df_main = load_data(file_path)
        col1 = st.columns(4)

        with col1[0]:
            selected_models = select_model(df_main)
  
        with col1[1]:
            vendor, dc = selected_component()

        with col1[2]:
            vendor_info = selected_vendor(vendor, df_main)
        
        with col1[3]:
            dc_info = selected_dc(dc, df_main)    
        
        if 'filtered_df' not in st.session_state:
            st.session_state.filtered_df = None


        if st.button("Filter Data"):
            if (selected_models == [] or selected_component is None or vendor_info is None or dc_info == []):
                st.warning("All fields are not selected.")
            else:
                st.success("Data is Uploaded Successfully")
                df_model = df_main[df_main['config_sn_list'].isin(selected_models)]
                df_selected_vendor = df_model[df_model[vendor] == vendor_info]
                st.session_state.filtered_df = df_selected_vendor[df_selected_vendor[dc].isin(dc_info)] 
                st.write("### Filtered Data")
                gb = GridOptionsBuilder.from_dataframe(st.session_state.filtered_df)
                gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=20)
                gb.configure_column(st.session_state.filtered_df.columns[0], hide=True)
                gb.configure_column(st.session_state.filtered_df.columns[1], hide=True)
                gridOptions = gb.build()
                AgGrid(st.session_state.filtered_df, gridOptions=gridOptions, allow_unsafe_jscode=True)

                csv_buffer = io.StringIO()
                st.session_state.filtered_df.to_csv(csv_buffer, index=False)
                csv = csv_buffer.getvalue().encode('utf-8')

                st.download_button(
                    label="Download Filtered Data as CSV",
                    data=csv,
                    file_name="filtered_data.csv",
                    mime="text/csv",
                )

                col1, col2 = st.columns(2)
                with col1:
                    df_total = st.session_state.filtered_df['config_sn_list'].value_counts().reset_index()
                    df_total.columns = ['Model', 'Quantity']
                    st.table(df_total.style.hide(axis="index"))
                with col2:
                    fig = px.histogram(df_total, x='Model', y='Quantity', title="Model Quantity Histogram")
                    st.plotly_chart(fig)

        elif st.session_state.filtered_df is not None: 
            st.write("### Filtered Data")
            gb = GridOptionsBuilder.from_dataframe(st.session_state.filtered_df)
            gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=20)
            gb.configure_column(st.session_state.filtered_df.columns[0], hide=True)
            gb.configure_column(st.session_state.filtered_df.columns[1], hide=True)
            gridOptions = gb.build()
            AgGrid(st.session_state.filtered_df, gridOptions=gridOptions, allow_unsafe_jscode=True)

            csv_buffer = io.StringIO()
            st.session_state.filtered_df.to_csv(csv_buffer, index=False)
            csv = csv_buffer.getvalue().encode('utf-8')

            st.download_button(
                label="Download Filtered Data as CSV",
                data=csv,
                file_name="filtered_data.csv",
                mime="text/csv",
            )

            col1, col2 = st.columns(2)
            with col1:
                df_total = st.session_state.filtered_df['config_sn_list'].value_counts().reset_index()
                df_total.columns = ['Model', 'Quantity']
                st.table(df_total.style.hide(axis="index"))
            with col2:
                fig = px.histogram(df_total, x='Model', y='Quantity', title="Model Quantity Histogram")
                st.plotly_chart(fig)

if __name__ == "__main__":
    main()