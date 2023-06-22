using ClasseCliente;
using MySql.Data.MySqlClient;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.Button;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using MySqlX.XDevAPI;
using System.Reflection.PortableExecutable;
using System.Collections.Generic;
using System.Globalization;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolBar;
using System.Reflection;

namespace GerenciadorDeClientes_Form
{
    public partial class ListagemCompradores : Form
    {
        private ClienteDAO clienteDAO;
        public ListagemCompradores()
        {
            InitializeComponent();

            string server = "localhost";
            string database = "PROJETO";
            string user = "root";
            string password = "1234";
            clienteDAO = new ClienteDAO(server, database, user, password);

            Lista_Clientes.View = View.Details;
            Lista_Clientes.LabelEdit = true;
            Lista_Clientes.AllowColumnReorder = true;
            Lista_Clientes.FullRowSelect = true;
            Lista_Clientes.GridLines = true;

            Lista_Clientes.Columns.Add("ID", 50, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Nome", 300, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Email", 250, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Telefone", 120, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("DataCadastro", 80, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("TipoPessoa", 50, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Cpf/Cnpj", 100, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("InscricaoEstadual", 100, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Isento", 50, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Genero", 100, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("DataNascimento", 80, HorizontalAlignment.Center);
            Lista_Clientes.Columns.Add("Bloqueado", 50, HorizontalAlignment.Center);

            MostrarGrupo(0);
        }

        private void b_AdicionarCliente_Click(object sender, EventArgs e)
        {
            Cliente novoCliente = new Cliente();
            novoCliente.NomeRazaoSocial = textBox1.Text;
            novoCliente.Email = textBox2.Text;
            novoCliente.Telefone = textBox3.Text;
            novoCliente.DataCadastro = DateTime.Now;
            novoCliente.TipoPessoa = comboBox1.SelectedItem.ToString();
            novoCliente.CpfCnpj = textBox4.Text;
            novoCliente.InscricaoEstadual = textBox5.Text;
            novoCliente.Isento = checkBox1.Checked;
            novoCliente.Genero = comboBox2.SelectedItem.ToString();
            novoCliente.DataNascimento = dateTimePicker1.Value;
            novoCliente.Bloqueado = checkBox2.Checked;

            try
            {
                clienteDAO.Inserir(novoCliente);
                MessageBox.Show("Cliente inserido com sucesso!");
                LimparCampos();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void b_EditarCliente_Click(object sender, EventArgs e)
        {
            Cliente ClienteSelecionado = new Cliente();
            ClienteSelecionado.Id = int.Parse(textBox6.Text);
            ClienteSelecionado.NomeRazaoSocial = textBox1.Text;
            ClienteSelecionado.Email = textBox2.Text;
            ClienteSelecionado.Telefone = textBox3.Text;
            ClienteSelecionado.DataCadastro = DateTime.Now;
            ClienteSelecionado.TipoPessoa = comboBox1.SelectedItem.ToString();
            ClienteSelecionado.CpfCnpj = textBox4.Text;
            ClienteSelecionado.InscricaoEstadual = textBox5.Text;
            ClienteSelecionado.Isento = checkBox1.Checked;
            ClienteSelecionado.Genero = comboBox2.SelectedItem.ToString();
            ClienteSelecionado.DataNascimento = dateTimePicker1.Value;
            ClienteSelecionado.Bloqueado = checkBox2.Checked;

            try
            {
                clienteDAO.Atualizar(ClienteSelecionado);
                MessageBox.Show("Cliente atualizado com sucesso!");
                LimparCampos();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void b_RemoverCliente_Click(object sender, EventArgs e)
        {
            Cliente ClienteSelecionado = new Cliente();
            ListViewItem item = Lista_Clientes.SelectedItems[0];
            ClienteSelecionado.Id = int.Parse(item.SubItems[0].Text);

            try
            {
                clienteDAO.Excluir(ClienteSelecionado.Id);
                MessageBox.Show("Cliente removido com sucesso!");
                Lista_Clientes.Items.Clear();
                LimparCampos();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void b_PesquisarCliente_Click(object sender, EventArgs e)
        {
            MostrarGrupo(2);
        }

        private void b_Voltar_Click(object sender, EventArgs e)
        {
            MostrarGrupo(0);
        }

        private void b_Listar_Click(object sender, EventArgs e)
        {
            List<Cliente> lista_clientes = new List<Cliente>();

            string filtro = " 1 = 1 ";
            if (!string.IsNullOrEmpty(textBox10.Text))
            {
                filtro = " nome_razao_social LIKE '%" + textBox10.Text + "%' AND " + filtro;
            }
            if (!string.IsNullOrEmpty(textBox11.Text))
            {
                filtro = " email LIKE '%" + textBox11.Text + "%' AND " + filtro;
            }
            if (!string.IsNullOrEmpty(textBox12.Text))
            {
                filtro = " telefone LIKE '%" + textBox12.Text + "%' AND " + filtro;
            }
            if (dateTimePicker2.Value.ToString("yyyy-MM-dd") != dateTimePicker3.Value.ToString("yyyy-MM-dd"))
            {
                filtro = " data_cadastro LIKE '%" + dateTimePicker3.Value.ToString("yyyy-MM-dd") + "%' AND " + filtro;
            }

            lista_clientes = clienteDAO.Pesquisar(filtro);
            exibir_clientes(lista_clientes);
        }

        private void exibir_clientes(List<Cliente> lista_clientes)
        {
            MostrarGrupo(3);
            for (int i = 0; i < lista_clientes.Count; i++)
            {
                string dataNascimento = "";
                if (lista_clientes[i].DataNascimento.HasValue)
                {
                    dataNascimento = lista_clientes[i].DataNascimento.Value.ToString("dd/MM/yyyy");
                }

                string[] row =
                {
                    lista_clientes[i].Id.ToString(),
                    lista_clientes[i].NomeRazaoSocial.ToString(),
                    lista_clientes[i].Email.ToString(),
                    lista_clientes[i].Telefone.ToString(),
                    lista_clientes[i].DataCadastro.ToString("dd/MM/yyyy"),
                    lista_clientes[i].TipoPessoa.ToString(),
                    lista_clientes[i].CpfCnpj.ToString(),
                    lista_clientes[i].InscricaoEstadual.ToString(),
                    lista_clientes[i].Isento ? "Sim" : "Não",
                    lista_clientes[i].Genero.ToString(),
                    dataNascimento,
                    lista_clientes[i].Bloqueado ? "Sim" : "Não"
                };

                var linha_listview = new ListViewItem(row);

                Lista_Clientes.Items.Add(linha_listview);
            }
        }

        private void b_ListarClienteSelecionado_Click(object sender, EventArgs e)
        {

            if (Lista_Clientes.SelectedItems.Count > 0)
            {
                ListViewItem item = Lista_Clientes.SelectedItems[0];
                textBox6.Text = item.SubItems[0].Text;
                textBox1.Text = item.SubItems[1].Text;
                textBox2.Text = item.SubItems[2].Text;
                textBox3.Text = item.SubItems[3].Text;
                dateTimePicker2.Value = DateTime.ParseExact(item.SubItems[4].Text, "dd/MM/yyyy", CultureInfo.InvariantCulture);
                comboBox1.SelectedItem = item.SubItems[5].Text;
                textBox4.Text = item.SubItems[6].Text;
                textBox5.Text = item.SubItems[7].Text;
                checkBox1.Checked = (item.SubItems[8].Text == "Sim");
                comboBox2.SelectedItem = item.SubItems[9].Text;
                dateTimePicker1.Value = DateTime.ParseExact(item.SubItems[10].Text, "dd/MM/yyyy", CultureInfo.InvariantCulture);
                checkBox2.Checked = (item.SubItems[11].Text == "Sim");
            }

            MostrarGrupo(1);
            b_AdicionarCliente.Visible = false;
            b_EditarCliente.Visible = true;
        }

        private void b_LimparFiltro_Click(object sender, EventArgs e)
        {
            LimparCampos();
        }

        private void b_NovoCliente_Click(object sender, EventArgs e)
        {
            MostrarGrupo(1);
            b_AdicionarCliente.Visible = true;
            b_EditarCliente.Visible = false;
        }

        private void LimparCampos()
        {
            Lista_Clientes.Items.Clear();

            foreach (Control c in this.Controls)
            {
                if (c is System.Windows.Forms.TextBox)
                {
                    ((System.Windows.Forms.TextBox)c).Clear();
                }
                else if (c is System.Windows.Forms.CheckBox)
                {
                    ((System.Windows.Forms.CheckBox)c).Checked = false;
                }
                else if (c is DateTimePicker)
                {
                    ((DateTimePicker)c).Value = DateTime.Now;
                }
                else if (c is System.Windows.Forms.ComboBox)
                {
                    ((System.Windows.Forms.ComboBox)c).SelectedIndex = -1;
                }
            }
        }

        private void MostrarGrupo(int grupo)
        {
            // Oculta todos os grupos
            g_Adicionar.Visible = false;
            g_Pesquisar.Visible = false;
            g_Lista.Visible = false;

            // Exibe o grupo especificado pelo parâmetro
            switch (grupo)
            {
                case 1:
                    g_Adicionar.Visible = true;
                    break;
                case 2:
                    g_Pesquisar.Visible = true;
                    break;
                case 3:
                    g_Lista.Visible = true;
                    break;
            }

            LimparCampos();
        }
    }
}
