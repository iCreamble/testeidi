import pandas as pd
import streamlit as st
import time
from datetime import datetime
from seatable_api import Base, context





server_url = 'https://cloud.seatable.io'
api_token = st.secrets["token"]
base = Base(api_token, server_url)
base.auth()







st.title('GERADOR DE MOVE ORDER - EIDI')
st.divider()

tab1, tab2 = st.tabs(['Gerar move order', 'Verificar solicitações'])

with tab1:
    with st.form('form1', clear_on_submit=True):
        input1 = st.text_input('Digite o código da matéria prima:')
        input2 = st.text_input('Digite a quantidade:')
        input3 = st.text_input('Múltiplo da MP desejado:')
        if st.form_submit_button('Solicitar'):

            dict = {}
            dict['Data'] = '{}'.format(datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M'))
            dict['Codigo'] = input1
            dict['Quantidade'] = input2
            dict['Multiplo'] = input3
            dict['Aprovado'] = 0
            dict['Feito'] = 0
            base.append_row('Table1', dict)
            
            
            with st.success('Solicitação enviada com sucesso.'):
                time.sleep(2)
                st.empty()


with tab2:
    if st.button('Verificar solicitações:'):
        with st.container():
            df = pd.DataFrame(base.list_rows("Table1"))
            df = df.iloc[:, 3:]
            st.write(df)
