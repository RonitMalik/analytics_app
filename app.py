import streamlit as st
import pandas as pd
import codecs
from pandas_profiling import ProfileReport

import streamlit.components.v1 as components
from streamlit_pandas_profiling import st_profile_report

st.cache(allow_output_mutation=True)
def main():

    st.title('''
    **Descriptive Analytics Tool**''')
    st.markdown("This tool used for descriptive analysis for any CSV file that you upload")
    data_file = st.file_uploader("Upload Your CSV", type=['CSV'])
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.dataframe(df.head())
        profile = ProfileReport(df)
        if st.button("Generate Report"):
            st_profile_report(profile)

if __name__=='__main__':
    main()
