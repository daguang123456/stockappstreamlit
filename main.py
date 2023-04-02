import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page


page = st.sidebar.selectbox("探索或预测", ("探讨","预测"))

if page == "预测":
    show_predict_page()
else:
    show_explore_page()