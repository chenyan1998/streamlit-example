from collections import namedtuple
import math
import streamlit as st
import streamlit.components.v1 as stc

# File Processing Pkgs
import altair as alt
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber
import numpy as np
import os 
import matplotlib.pyplot as plt
import plotly.express as px

#start
"""
# Welcome to SIA Data Analysis and Visualization !

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

def save_uploadedfile(uploadedfile):
     with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

# df = pd.DataFrame(np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
# st.dataframe(df)  # Same as st.write(df)

st.subheader("Dataset")
data_file = st.file_uploader("Upload CSV",type=['csv'])
if st.button("Process"):
    if data_file is not None:
        file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
        df_colx = df.iloc[:,14]
        # #st.dataframe(df_colx)
        df_coly1 = df.iloc[:,15]
        df_coly2 = df.iloc[:,13]
        df_coly3 = df.iloc[:,12]
        
        #st.dataframe(df_coly)
        save_uploadedfile(data_file)
        chart_data = pd.DataFrame(df_colx,df_coly1)
        st.line_chart(chart_data)
        # st.altair_chart(df_colx,df_coly, use_container_width=True)

        #mul lines in one graph
        chart_data = pd.DataFrame(df_colx, columns=['FEL', 'frends_zTransformation'])
        st.line_chart(chart_data)
        st.area_chart(chart_data)
        st.bar_chart(chart_data)

        #line chart
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.line_chart(chart_data)
        #area chart
        chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
        st.area_chart(chart_data)
        #bar chart
        chart_data = pd.DataFrame(np.random.randn(50, 3),columns=["a", "b", "c"])
        st.bar_chart(chart_data)



with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))



