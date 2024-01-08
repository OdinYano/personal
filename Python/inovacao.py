import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import plotly.express as px

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard Interativo")

        self.frame_selecao = tk.Frame(root)
        self.frame_selecao.pack(padx=10, pady=10)

        self.df = pd.DataFrame()
        self.tipos_graficos = ["Dispersão", "Linha", "Barra", "Pizza", "Caixa", "Área", "Histograma", "Matrix de Dispersão"]
        self.opcoes_graficos = tk.StringVar(value="Selecione o tipo de gráfico:")

        # Variáveis de controle para caixas de seleção
        self.var_dimensao = tk.StringVar()
        self.var_dimensao.set("Selecione a dimensão:")

        self.var_valor = tk.StringVar()
        self.var_valor.set("Selecione o valor:")

        self.var_legenda = tk.StringVar()
        self.var_legenda.set("Selecione a legenda:")

        self.var_ordenacao = tk.StringVar()
        self.var_ordenacao.set("Selecione a ordenação:")

        self.btn_exibir_grafico = tk.Button(self.frame_selecao, text="Exibir Gráfico", command=self.exibir_grafico)

        # Inicializa os botões e caixas de seleção
        self.criar_caixas_selecao()

    def escolher_coluna(self, titulo, variavel):
        colunas = self.df.columns
        coluna_selecionada = simpledialog.askstring(titulo, f"Selecione a coluna de {titulo}:", initialvalue=variavel.get(), parent=self.root)

        if coluna_selecionada and coluna_selecionada in colunas:
            variavel.set(coluna_selecionada)
        elif coluna_selecionada:
            messagebox.showwarning("Aviso", f"Coluna de {titulo.lower()} inválida.")

    def criar_caixas_selecao(self):
        opcoes_tipo_grafico = tk.OptionMenu(self.frame_selecao, self.opcoes_graficos, *self.tipos_graficos)
        opcoes_tipo_grafico.pack()

        # Adiciona as caixas de seleção no frame
        tk.OptionMenu(self.frame_selecao, self.var_dimensao, *self.df.columns).pack()

        tk.OptionMenu(self.frame_selecao, self.var_valor, *self.df.columns).pack()

        tk.OptionMenu(self.frame_selecao, self.var_legenda, *self.df.columns).pack()

        tk.OptionMenu(self.frame_selecao, self.var_ordenacao, *self.df.columns).pack()

        # Adiciona o botão de exibir gráfico
        self.btn_exibir_grafico.pack()

    def exibir_grafico(self):
        tipo_grafico = self.opcoes_graficos.get()
        dimensao = self.var_dimensao.get()
        valor = self.var_valor.get()
        legenda = self.var_legenda.get()
        ordenacao = self.var_ordenacao.get()

        if tipo_grafico == "Dispersão":
            self.mostrar_grafico_dispersao(dimensao, valor)
        elif tipo_grafico == "Linha":
            self.mostrar_grafico_linha(dimensao, valor)
        elif tipo_grafico == "Barra":
            self.mostrar_grafico_barra(dimensao, valor, legenda, ordenacao)
        elif tipo_grafico == "Pizza":
            self.mostrar_grafico_pizza(dimensao, valor)
        elif tipo_grafico == "Caixa":
            self.mostrar_grafico_caixa(dimensao, valor)
        elif tipo_grafico == "Área":
            self.mostrar_grafico_area(dimensao, valor)
        elif tipo_grafico == "Histograma":
            self.mostrar_grafico_histograma(dimensao, valor)
        elif tipo_grafico == "Matrix de Dispersão":
            self.mostrar_matrix_dispersao([dimensao, valor])

    def mostrar_grafico_dispersao(self, dimensao, valor):
        fig = px.scatter(self.df, x=dimensao, y=valor, title=f'Gráfico de Dispersão: {dimensao} vs {valor}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_linha(self, dimensao, valor):
        fig = px.line(self.df, x=dimensao, y=valor, title=f'Gráfico de Linha: {dimensao} vs {valor}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_area(self, dimensao, valor):
        fig = px.area(self.df, x=dimensao, y=valor, title=f'Gráfico de Área: {dimensao} vs {valor}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_histograma(self, dimensao, valor):
        fig = px.histogram(self.df, x=dimensao, y=valor, title=f'Histograma: {dimensao} vs {valor}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_matrix_dispersao(self, colunas):
        fig = px.scatter_matrix(self.df, dimensions=colunas, title=f'Matrix de Dispersão: {", ".join(colunas)}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_barra(self, dimensao, valor, legenda, ordenacao):
        if legenda != "Selecione a legenda:" and ordenacao != "Selecione a ordenação:":
            if ordenacao != "Selecione a ordenação:":
                fig = px.bar(self.df, x=dimensao, y=valor, color=legenda, title=f'Gráfico de Barras: {dimensao} vs {valor}', category_orders={ordenacao: self.df[ordenacao].unique()})
            else:
                fig = px.bar(self.df, x=dimensao, y=valor, color=legenda, title=f'Gráfico de Barras: {dimensao} vs {valor}')

        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_pizza(self, dimensao, valor):
        fig = px.pie(self.df, names=dimensao, title=f'Gráfico de Pizza: {dimensao}')
        self.salvar_e_exibir_figura_grafico(fig)

    def mostrar_grafico_caixa(self, dimensao, valor):
        fig = px.box(self.df, x=dimensao, y=valor, title=f'Gráfico de Caixa: {dimensao} vs {valor}')
        self.salvar_e_exibir_figura_grafico(fig)

    def salvar_e_exibir_figura_grafico(self, figura):
        figura.write_html("grafico.html")
        figura.write_image("grafico.png")

        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Novo Gráfico")

        img_label = tk.Label(nova_janela)
        img_label.pack()

        img = tk.PhotoImage(file="grafico.png")
        img_label.configure(image=img)
        img_label.image = img

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
