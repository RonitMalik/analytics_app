import streamlit as st
import pandas as pd
import codecs
from pandas_profiling import ProfileReport
import time
from streamlit_lottie import st_lottie
import json
import klib
import requests
import numpy as np

import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

#Custom components
import sweetviz as sv

def st_display_sweetviz(report_html, width=2000, height= 1000):
    report_file = codecs.open(report_html, 'r')
    page = report_file.read()
    components.html(page, width= width, height=height, scrolling=True)


st.cache(allow_output_mutation=True)
def main():


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


    lottie_hello = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_hx7ddrx9.json')
    st_lottie(
    lottie_hello,
    speed=1,
    )

    st.title('''
    **Descriptive Analytics Tool**''')
    st.markdown("This tool used for descriptive analysis for any CSV file that you upload")
    data_file = st.file_uploader("Upload Your CSV", type=['CSV'])

    if data_file is not None:
        df = pd.read_csv(data_file)
        check_dataframe = st.checkbox('View dataframe')

        if check_dataframe:
            st.dataframe(df.head())

        #viewing the datatypes
        view_datatype = st.checkbox('View data type')
        if view_datatype:
            df_1 = df.dtypes
            st.markdown(''' Here is an overview of your datatypes in the dataset''')
            st.dataframe(df_1.astype(str))


        # if date column exist in dataset the convert to date time
        date_exist = st.checkbox('Only check this box if you have a date dimension in the dataset')
        if date_exist:
            df.columns = df.columns.str.lower() #making all column header lower case
            df['date'] = pd.to_datetime(df['date'])
            st.dataframe(df.head(1))

        # We can pick up the processed data with converted date columns and generate report
        profile = ProfileReport(df)
        if st.button("Generate Report"):
            st_profile_report(profile)


if __name__=='__main__':
    main()
