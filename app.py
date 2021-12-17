import streamlit as st
import pandas as pd
import numpy as np


st.title('Descubra sua idade por seu cachorro!')

input0 = st.selectbox('selecione a raça', ['raça1','raça2'])

input1 = st.text_input('input 1')

subtmit_button = st.button('send')

if subtmit_button:
    st.text(f'{input1} {input0}')

