import streamlit as st
import pandas as pd
import numpy as np
import super_requests as r

import micro_db as db

#como rodar - streamlit run app.py

st.set_page_config(page_title="Dogs")


col1, col2, col3 = st.columns([2,4,2])

with col1:
    st.write("")

with col2:
    st.image("https://images.pexels.com/photos/3478875/pexels-photo-3478875.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=400")

with col3:
    st.write("")

st.title('Descubra sua idade pelo seu cachorro!')

raca = st.selectbox('selecione a raça', db.rasse_dogs)

tipo_raca = st.selectbox('selecione o tipo de raça', db.rassentyp)
age = st.text_input('digite o ano de nascimento (integer)')

gender = st.radio('genero do dog', ['female','male'])

if gender == 'female':
    gender = 'w'
else:
    gender = 'm'

cor = st.selectbox('selecione a cor do dog', db.cor_dogs)

submit_button = st.button('send')

if submit_button:

    st.text(f'{raca}, {tipo_raca}, {age}, {gender}, {cor}')

