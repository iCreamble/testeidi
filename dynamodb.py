import boto3
# import os
# import requests
# import json
import pandas as pd
import streamlit as st
import time
from datetime import datetime





dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'sa-east-1',
              aws_access_key_id = 'AKIA2UC3DAIFU6PNFGJR',
              aws_secret_access_key = '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')
mytable = dynamo_client.Table('moeidi')




###  WRITE
# mydict = {}
# mydict['chaveint'] = 4
# mydict['data'] = '30/04/2024'
# mydict['codigo'] = '2300000C'
# mydict['quantidade'] = '1500'
# mydict['multiplopref'] = '750'
# mydict['done'] = '1'



# mytable.put_item(Item = mydict)




### READ

# for item in mytable.scan()['Items']:
#     print(item)

# df = pd.DataFrame(mytable.scan()['Items'])
# print(df)
# print(df['chaveint'].max())




### UPDATE
# mytable.update_item(Key = {'chaveint':3},
#                          UpdateExpression = 'set done =:S',
#                          ExpressionAttributeValues = {":S":1})


# df = pd.DataFrame(mytable.scan()['Items'])
# print(df)






st.title('GERADOR DE MOVE ORDER - EIDI')
st.divider()

tab1, tab2 = st.tabs(['Gerar move order', 'Verificar solicitações'])

with tab1:
    with st.form('form1', clear_on_submit=True):
        input1 = st.text_input('Digite o código da matéria prima:')
        input2 = st.text_input('Digite a quantidade:')
        input3 = st.text_input('Múltiplo da MP desejado:')
        if st.form_submit_button('Solicitar'):

            df = pd.DataFrame(mytable.scan()['Items'])
            lastchave = df['chaveint'].max()

            mydict = {}
            mydict['chaveint'] = lastchave+1
            mydict['data'] = '{}'.format(datetime.strftime(datetime.now(), '%d/%m/%Y'))
            mydict['codigo'] = input1
            mydict['quantidade'] = input2
            mydict['multiplopref'] = input3
            mydict['done'] = '0'
            mytable.put_item(Item = mydict)
            # st.write(mydict)
            
            with st.success('Solicitação enviada com sucesso.'):
                time.sleep(2)
                st.empty()


with tab2:
    if st.button('Verificar solicitações:'):
        df = pd.DataFrame(mytable.scan()['Items'])
        df = df.sort_values(['chaveint'])
        st.write(df)