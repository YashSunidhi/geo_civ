import streamlit as st
import pandas as pd
import datetime as datetime
import os
import ast
from sentence_transformers import SentenceTransformer
from bertopic.representation import KeyBERTInspired, MaximalMarginalRelevance, TextGeneration
import plotly.express as px

from umap import UMAP
from hdbscan import HDBSCAN
from bertopic import BERTopic

from sklearn.feature_extraction.text import CountVectorizer
from bertopic.representation import PartOfSpeech, KeyBERTInspired, MaximalMarginalRelevance, OpenAI
import streamlit as st
from trubrics.integrations.streamlit import FeedbackCollector
from streamlit_feedback import streamlit_feedback
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'> CivTech Data Analysis </h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'> Data Understansing </h5>", unsafe_allow_html=True)
