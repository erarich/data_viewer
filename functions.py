import pandas as pd
import statistics


def convert_to_dataframe(uploaded_file, selected_separator):
    dataframe = pd.read_csv(uploaded_file, sep=selected_separator)
    dataframe = dataframe.apply(lambda x: x.str.replace(
        ',', '.') if x.dtype == 'object' else x)
    return dataframe


def get_file_information(uploaded_file, dataframe):
    get_file_name = uploaded_file.name
    get_file_number_attributes = dataframe.shape[1]
    get_file_number_instances = len(dataframe)
    list_of_columns = []
    for column in dataframe.columns:
        list_of_columns.append(column)
    datatypes = dataframe.dtypes
    return get_file_name, get_file_number_attributes, get_file_number_instances, list_of_columns, datatypes
