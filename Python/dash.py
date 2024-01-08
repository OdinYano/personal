# streamlit run C:\Users\Lenovo IdeaPad\Documents\GitHub\personal\Python\dash.py

import streamlit as st
import pandas as pd
import plotly.express as px

uploaded_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.warning("Por favor, faça o upload de um arquivo CSV.")

if 'df' in locals() and df is not None:
  
    df["Data"] = pd.to_datetime(df["Data"], format="%d-%m-%Y")
    df = df.sort_values("Data")

    df["Month"] = df["Data"].dt.to_period("M")
    month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique())

    df_filtered = df[df["Month"] == month]
    
    todas_opcoes_graficos = ["Faturamento por dia", "Faturamento por tipo de produto", "Faturamento total por Cliente", "Faturamento por tipo de pagamento"]
    selected_graficos = st.sidebar.multiselect("Selecione os gráficos a serem exibidos", todas_opcoes_graficos, default=todas_opcoes_graficos)
    selected_cliente = st.sidebar.multiselect("Selecione Cliente(s)", df_filtered["Cliente"].unique())
    selected_produto = st.sidebar.multiselect("Selecione Produto(s)", df_filtered["Produto"].unique())

    if selected_cliente:
        df_filtered = df_filtered[df_filtered["Cliente"].isin(selected_cliente)]
    if selected_produto:
        df_filtered = df_filtered[df_filtered["Produto"].isin(selected_produto)]

    if not df_filtered.empty and selected_graficos:
        for grafico in selected_graficos:
            if grafico == "Faturamento por dia":
                st.subheader("Faturamento por dia")
                fig_Data = px.bar(df_filtered, x="Data", y="Valor", title="Faturamento por dia")
                st.plotly_chart(fig_Data, use_container_width=True)
            elif grafico == "Faturamento por tipo de produto":
                st.subheader("Faturamento por tipo de produto")
                fig_prod = px.bar(df_filtered, x="Produto", y="Valor", title="Faturamento por tipo de produto")
                fig_prod.update_traces(text=df_filtered["Valor"], textposition='outside')
                st.plotly_chart(fig_prod, use_container_width=True)
            elif grafico == "Faturamento total por Cliente":
                st.subheader("Faturamento total por Cliente")
                fig_city = px.bar(df_filtered, x="Cliente", y="Valor", title="Faturamento total por Cliente")
                st.plotly_chart(fig_city, use_container_width=True)
            elif grafico == "Faturamento por tipo de pagamento":
                st.subheader("Faturamento por tipo de pagamento")
                fig_kind = px.pie(df_filtered, values="Valor", names="Produto", title="Faturamento por tipo de pagamento")
                st.plotly_chart(fig_kind, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para o mês e filtros selecionados.")
