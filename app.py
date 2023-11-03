import streamlit as st
import pandas as pd
import datetime as datetime
import os
import ast
import plotly.express as px
import geopandas as gpd


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'> CivTech Data Analysis </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'> Data Understansing </h5>", unsafe_allow_html=True)

print("Loading Shapefile...")

# If using your files, replace below filename ("Clean_Streets_Index_Grids_2018_Quarter_3.shp") with the 
# shapefile filename you uploaded. 

shapefile = gpd.read_file("/content/ScottishForestry-TreeHealth-SurveySites-Oct23.shp")
