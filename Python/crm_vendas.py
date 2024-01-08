import streamlit as st
import pandas as pd
import os
from openpyxl import load_workbook
import sys

def verificar_planilhas():
    if not os.path.exists('vendas.xlsx'):
        data = {'Valor': [], 'Cliente': [], 'Observação': []}
        df = pd.DataFrame(data)
        df.to_excel('vendas.xlsx', index=False)
        st.write("Planilha 'vendas.xlsx' criada.")

    if not os.path.exists('clientes.xlsx'):
        data = {'Nome': [], 'CPF': [], 'Telefone': []}
        df = pd.DataFrame(data)
        df.to_excel('clientes.xlsx', index=False)
        st.write("Planilha 'clientes.xlsx' criada.")

def cadastro_vendas():
    st.title("Cadastro de Vendas")
    verificar_planilhas()

    valor = st.text_input("Valor:")
    cliente = st.text_input("Cliente:")
    observacao = st.text_input("Observação:")

    data = {'Valor': [valor], 'Cliente': [cliente], 'Observação': [observacao]}
    df = pd.DataFrame(data)

    path = 'vendas.xlsx'
    sheet_name = 'Sheet1'
    if os.path.exists(path):
        with pd.ExcelFile(path) as xls:
            if sheet_name in xls.sheet_names:
                # Carrega a planilha existente
                df_existing = xls.parse(sheet_name)
                # Adiciona os novos dados
                df_existing = pd.concat([df_existing, df], ignore_index=True)
                # Salva a planilha atualizada
                df_existing.to_excel(path, index=False)
                st.session_state.vendas_saved = True
            else:
                # Se a planilha não existir, cria uma nova
                df.to_excel(path, index=False)
                st.session_state.vendas_saved = True
    else:
        # Se o arquivo Excel não existir, cria um novo
        df.to_excel(path, index=False)
        st.session_state.vendas_saved = True

def cadastrar_cliente():
    st.title("Cadastro de Cliente")
    verificar_planilhas()

    nome = st.text_input("Nome:")
    cpf = st.text_input("CPF:")
    telefone = st.text_input("Telefone:")

    data = {'Nome': [nome], 'CPF': [cpf], 'Telefone': [telefone]}
    df = pd.DataFrame(data)

    # Adiciona dados à planilha Excel local
    path = 'clientes.xlsx'
    sheet_name = 'Sheet1'
    if os.path.exists(path):
        with pd.ExcelFile(path) as xls:
            if sheet_name in xls.sheet_names:
                # Carrega a planilha existente
                df_existing = xls.parse(sheet_name)
                # Adiciona os novos dados
                df_existing = pd.concat([df_existing, df], ignore_index=True)
                # Salva a planilha atualizada
                df_existing.to_excel(path, index=False)
                st.session_state.clientes_saved = True
            else:
                # Se a planilha não existir, cria uma nova
                df.to_excel(path, index=False)
                st.session_state.clientes_saved = True
    else:
        # Se o arquivo Excel não existir, cria um novo
        df.to_excel(path, index=False)
        st.session_state.clientes_saved = True


def listar_vendas():
    st.title("Listar Vendas")
    verificar_planilhas()

    df_vendas = pd.read_excel('vendas.xlsx')
    st.dataframe(df_vendas)

def listar_clientes():
    st.title("Listar Clientes")
    verificar_planilhas()

    df_clientes = pd.read_excel('clientes.xlsx')
    st.dataframe(df_clientes)

def emitir_nfe():
    st.title("Emitir NFe")
    st.write("Clique no link abaixo para emitir a NFe:")
    st.markdown(r"[Emissão de NFe - Sebrae](https://amei.sebrae.com.br/auth/realms/externo/protocol/openid-connect/auth?client_id=emissor-nfe-frontend&redirect_uri=https%3A%2F%2Femissornfe.sebrae.com.br%2F&state=af6ad833-473d-4609-93a2-8c1cc709b0b2&response_mode=fragment&response_type=code&scope=openid&nonce=8ff8f929-e829-461f-b6dc-5a5e2f32c5cb)")

# Layout
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Escolha uma opção:", ("Cadastro de Vendas", "Cadastrar Cliente", "Listar Vendas", "Listar Clientes", "Emitir NFe"))

if opcao == "Cadastro de Vendas":
    cadastro_vendas()
elif opcao == "Cadastrar Cliente":
    cadastrar_cliente()
elif opcao == "Listar Vendas":
    listar_vendas()
elif opcao == "Listar Clientes":
    listar_clientes()
elif opcao == "Emitir NFe":
    emitir_nfe()

import subprocess
subprocess.run(['streamlit', 'run', 'seu_script.py'], check=True)
