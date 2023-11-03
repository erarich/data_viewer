import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from functions import *

# PAGE CONFIGURATION
# favicon = Image.open("favicon.png")
# favicon2array = np.array(favicon)
st.set_page_config("Streamlit test", None, "wide", "auto",
                   {"Get help": None, "Report a Bug": None, "About": None})


def main():
    st.title('Streamlit test')

    st.text("Upload a csv file to begin!")

    uploaded_file = st.file_uploader("Choose a .csv file", type=[
        'csv'], accept_multiple_files=False)

    if uploaded_file is not None:
        dataframe = convert_to_dataframe(uploaded_file)
        file_information = get_file_information(uploaded_file, dataframe)

        list_of_attributes = file_information[3]
        list_of_datatypes = file_information[4]

        with st.expander("View information about file"):
            st.write("      - **File name:** ", file_information[0])
            st.write("      - **Number of attributes:** ", file_information[1])
            st.write("      - **Instances:** ", file_information[2])
            st.write("      - **List of attributes:**")
            st.write(list_of_attributes)
            st.write("      - **List of data types:**")
            st.write(list_of_datatypes)

        with st.expander("Display all dataframe"):
            st.dataframe(dataframe)

        with st.expander("Display the attributes line chart"):
            selected_date_column = st.selectbox(
                'Select the date column',
                (list_of_attributes),
                key='sb_one',
            )

            only_numeric_columns = []
            for column in list_of_attributes:
                if (dataframe.dtypes[column] == 'float64'):
                    only_numeric_columns.append(column)

            print(only_numeric_columns)

            selected_attribute = st.selectbox(
                'Select the attribute',
                (only_numeric_columns),
                key='sb_two',
            )
            print(selected_date_column)
            print(selected_attribute)
            attribute_position = only_numeric_columns.index(selected_attribute)
            st.line_chart(dataframe, x=selected_date_column, y=selected_attribute
                          )


if __name__ == "__main__":
    main()
