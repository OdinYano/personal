namespace GerenciadorDeClientes_Form
{
    partial class ListagemCompradores
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            label7 = new Label();
            label8 = new Label();
            label9 = new Label();
            label10 = new Label();
            label11 = new Label();
            label12 = new Label();
            label13 = new Label();
            label14 = new Label();
            label15 = new Label();
            label16 = new Label();
            label17 = new Label();
            label25 = new Label();
            b_AdicionarCliente = new Button();
            b_PesquisarCliente = new Button();
            b_RemoverCliente = new Button();
            b_ListarClienteSelecionado = new Button();
            b_EditarCliente = new Button();
            b_Voltar = new Button();
            b_Voltar_Pesquisa = new Button();
            b_Listar = new Button();
            b_LimparFiltro = new Button();
            b_NovoCliente = new Button();
            b_VoltarEdit = new Button();
            checkBox1 = new CheckBox();
            checkBox2 = new CheckBox();
            comboBox1 = new ComboBox();
            comboBox2 = new ComboBox();
            dateTimePicker1 = new DateTimePicker();
            dateTimePicker2 = new DateTimePicker();
            dateTimePicker3 = new DateTimePicker();
            textBox1 = new TextBox();
            textBox2 = new TextBox();
            textBox3 = new TextBox();
            textBox4 = new TextBox();
            textBox5 = new TextBox();
            textBox6 = new TextBox();
            textBox10 = new TextBox();
            textBox11 = new TextBox();
            textBox12 = new TextBox();
            Lista_Clientes = new ListView();
            g_Adicionar = new GroupBox();
            g_Lista = new GroupBox();
            g_Pesquisar = new GroupBox();
            g_Adicionar.SuspendLayout();
            g_Lista.SuspendLayout();
            g_Pesquisar.SuspendLayout();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(23, 9);
            label1.Name = "label1";
            label1.Size = new Size(470, 15);
            label1.TabIndex = 0;
            label1.Text = "Consulte os seus Clientes cadastrados na sua Loja ou realize o cadastro de novos Cliente";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(30, 64);
            label2.Name = "label2";
            label2.Size = new Size(131, 15);
            label2.TabIndex = 3;
            label2.Text = "Nome ou  Razao Social:";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(30, 94);
            label3.Name = "label3";
            label3.Size = new Size(39, 15);
            label3.TabIndex = 4;
            label3.Text = "Email:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(30, 124);
            label4.Name = "label4";
            label4.Size = new Size(54, 15);
            label4.TabIndex = 5;
            label4.Text = "Telefone:";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(30, 184);
            label5.Name = "label5";
            label5.Size = new Size(72, 15);
            label5.TabIndex = 6;
            label5.Text = "Tipo Pessoa:";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(661, 34);
            label6.Name = "label6";
            label6.Size = new Size(74, 15);
            label6.TabIndex = 7;
            label6.Text = "Cpf ou Cnpj:";
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(661, 64);
            label7.Name = "label7";
            label7.Size = new Size(104, 15);
            label7.TabIndex = 8;
            label7.Text = "Inscricao Estadual:";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(661, 94);
            label8.Name = "label8";
            label8.Size = new Size(42, 15);
            label8.TabIndex = 9;
            label8.Text = "Isento:";
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Location = new Point(661, 124);
            label9.Name = "label9";
            label9.Size = new Size(48, 15);
            label9.TabIndex = 10;
            label9.Text = "Gênero:";
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Location = new Point(661, 154);
            label10.Name = "label10";
            label10.Size = new Size(117, 15);
            label10.TabIndex = 11;
            label10.Text = "Data de Nascimento:";
            // 
            // label11
            // 
            label11.AutoSize = true;
            label11.Location = new Point(661, 184);
            label11.Name = "label11";
            label11.Size = new Size(67, 15);
            label11.TabIndex = 12;
            label11.Text = "Bloqueado:";
            // 
            // label12
            // 
            label12.AutoSize = true;
            label12.Location = new Point(30, 154);
            label12.Name = "label12";
            label12.Size = new Size(101, 15);
            label12.TabIndex = 13;
            label12.Text = "Data do Cadastro:";
            // 
            // label13
            // 
            label13.AutoSize = true;
            label13.Location = new Point(30, 34);
            label13.Name = "label13";
            label13.Size = new Size(21, 15);
            label13.TabIndex = 25;
            label13.Text = "ID:";
            // 
            // label14
            // 
            label14.AutoSize = true;
            label14.Location = new Point(30, 25);
            label14.Name = "label14";
            label14.Size = new Size(131, 15);
            label14.TabIndex = 3;
            label14.Text = "Nome ou  Razao Social:";
            // 
            // label15
            // 
            label15.AutoSize = true;
            label15.Location = new Point(30, 55);
            label15.Name = "label15";
            label15.Size = new Size(39, 15);
            label15.TabIndex = 4;
            label15.Text = "Email:";
            // 
            // label16
            // 
            label16.AutoSize = true;
            label16.Location = new Point(30, 85);
            label16.Name = "label16";
            label16.Size = new Size(54, 15);
            label16.TabIndex = 5;
            label16.Text = "Telefone:";
            // 
            // label17
            // 
            label17.AutoSize = true;
            label17.Location = new Point(15, 16);
            label17.Name = "label17";
            label17.Size = new Size(220, 15);
            label17.TabIndex = 28;
            label17.Text = "Você pode selecionar um cliente na lista:";
            // 
            // label25
            // 
            label25.AutoSize = true;
            label25.Location = new Point(30, 115);
            label25.Name = "label25";
            label25.Size = new Size(101, 15);
            label25.TabIndex = 13;
            label25.Text = "Data do Cadastro:";
            // 
            // b_AdicionarCliente
            // 
            b_AdicionarCliente.AutoSize = true;
            b_AdicionarCliente.Location = new Point(906, 204);
            b_AdicionarCliente.Name = "b_AdicionarCliente";
            b_AdicionarCliente.Size = new Size(110, 25);
            b_AdicionarCliente.TabIndex = 1;
            b_AdicionarCliente.Text = "Adicionar Cliente";
            b_AdicionarCliente.UseVisualStyleBackColor = true;
            b_AdicionarCliente.Click += b_AdicionarCliente_Click;
            // 
            // b_PesquisarCliente
            // 
            b_PesquisarCliente.Location = new Point(511, 9);
            b_PesquisarCliente.Name = "b_PesquisarCliente";
            b_PesquisarCliente.Size = new Size(110, 25);
            b_PesquisarCliente.TabIndex = 2;
            b_PesquisarCliente.Text = "Filtrar";
            b_PesquisarCliente.UseVisualStyleBackColor = true;
            b_PesquisarCliente.Click += b_PesquisarCliente_Click;
            // 
            // b_RemoverCliente
            // 
            b_RemoverCliente.Location = new Point(1106, 389);
            b_RemoverCliente.Name = "b_RemoverCliente";
            b_RemoverCliente.Size = new Size(110, 25);
            b_RemoverCliente.TabIndex = 28;
            b_RemoverCliente.Text = "Remover Cliente";
            b_RemoverCliente.UseVisualStyleBackColor = true;
            b_RemoverCliente.Click += b_RemoverCliente_Click;
            // 
            // b_ListarClienteSelecionado
            // 
            b_ListarClienteSelecionado.Location = new Point(990, 389);
            b_ListarClienteSelecionado.Name = "b_ListarClienteSelecionado";
            b_ListarClienteSelecionado.Size = new Size(110, 25);
            b_ListarClienteSelecionado.TabIndex = 30;
            b_ListarClienteSelecionado.Text = "Selecionar Cliente";
            b_ListarClienteSelecionado.UseVisualStyleBackColor = true;
            b_ListarClienteSelecionado.Click += b_ListarClienteSelecionado_Click;
            // 
            // b_EditarCliente
            // 
            b_EditarCliente.Location = new Point(906, 204);
            b_EditarCliente.Name = "b_EditarCliente";
            b_EditarCliente.Size = new Size(110, 25);
            b_EditarCliente.TabIndex = 33;
            b_EditarCliente.Text = "Editar Cliente";
            b_EditarCliente.UseVisualStyleBackColor = true;
            b_EditarCliente.Click += b_EditarCliente_Click;
            // 
            // b_Voltar
            // 
            b_Voltar.Location = new Point(1222, 389);
            b_Voltar.Name = "b_Voltar";
            b_Voltar.Size = new Size(110, 25);
            b_Voltar.TabIndex = 31;
            b_Voltar.Text = "Voltar";
            b_Voltar.UseVisualStyleBackColor = true;
            b_Voltar.Click += b_Voltar_Click;
            // 
            // b_Voltar_Pesquisa
            // 
            b_Voltar_Pesquisa.Location = new Point(731, 110);
            b_Voltar_Pesquisa.Name = "b_Voltar_Pesquisa";
            b_Voltar_Pesquisa.Size = new Size(110, 25);
            b_Voltar_Pesquisa.TabIndex = 33;
            b_Voltar_Pesquisa.Text = "Voltar";
            b_Voltar_Pesquisa.UseVisualStyleBackColor = true;
            b_Voltar_Pesquisa.Click += b_Voltar_Click;
            // 
            // b_Listar
            // 
            b_Listar.Location = new Point(499, 110);
            b_Listar.Name = "b_Listar";
            b_Listar.Size = new Size(110, 25);
            b_Listar.TabIndex = 32;
            b_Listar.Text = "Listar";
            b_Listar.UseVisualStyleBackColor = true;
            b_Listar.Click += b_Listar_Click;
            // 
            // b_LimparFiltro
            // 
            b_LimparFiltro.Location = new Point(615, 110);
            b_LimparFiltro.Name = "b_LimparFiltro";
            b_LimparFiltro.Size = new Size(110, 25);
            b_LimparFiltro.TabIndex = 31;
            b_LimparFiltro.Text = "Limpar Filtro";
            b_LimparFiltro.UseVisualStyleBackColor = true;
            b_LimparFiltro.Click += b_LimparFiltro_Click;
            // 
            // b_NovoCliente
            // 
            b_NovoCliente.AutoSize = true;
            b_NovoCliente.Location = new Point(630, 9);
            b_NovoCliente.Name = "b_NovoCliente";
            b_NovoCliente.Size = new Size(110, 25);
            b_NovoCliente.TabIndex = 35;
            b_NovoCliente.Text = "Adicionar Cliente";
            b_NovoCliente.UseVisualStyleBackColor = true;
            b_NovoCliente.Click += b_NovoCliente_Click;
            // 
            // b_VoltarEdit
            // 
            b_VoltarEdit.Location = new Point(1022, 204);
            b_VoltarEdit.Name = "b_VoltarEdit";
            b_VoltarEdit.Size = new Size(110, 25);
            b_VoltarEdit.TabIndex = 34;
            b_VoltarEdit.Text = "Voltar";
            b_VoltarEdit.UseVisualStyleBackColor = true;
            b_VoltarEdit.Click += b_Voltar_Click;
            // 
            // checkBox1
            // 
            checkBox1.AutoSize = true;
            checkBox1.Location = new Point(798, 93);
            checkBox1.Name = "checkBox1";
            checkBox1.Size = new Size(15, 14);
            checkBox1.TabIndex = 20;
            checkBox1.UseVisualStyleBackColor = true;
            // 
            // checkBox2
            // 
            checkBox2.AutoSize = true;
            checkBox2.Location = new Point(798, 183);
            checkBox2.Name = "checkBox2";
            checkBox2.Size = new Size(15, 14);
            checkBox2.TabIndex = 23;
            checkBox2.UseVisualStyleBackColor = true;
            // 
            // comboBox1
            // 
            comboBox1.AutoCompleteSource = AutoCompleteSource.ListItems;
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { "Física", "Jurídica" });
            comboBox1.Location = new Point(167, 181);
            comboBox1.Name = "comboBox1";
            comboBox1.Size = new Size(186, 23);
            comboBox1.TabIndex = 17;
            comboBox1.Text = "Selecione o tipo de Pessoa";
            // 
            // comboBox2
            // 
            comboBox2.FormattingEnabled = true;
            comboBox2.Items.AddRange(new object[] { "Feminino", "Masculino", "Outro" });
            comboBox2.Location = new Point(798, 121);
            comboBox2.Name = "comboBox2";
            comboBox2.Size = new Size(186, 23);
            comboBox2.TabIndex = 21;
            // 
            // dateTimePicker1
            // 
            dateTimePicker1.Location = new Point(798, 154);
            dateTimePicker1.Name = "dateTimePicker1";
            dateTimePicker1.Size = new Size(249, 23);
            dateTimePicker1.TabIndex = 22;
            // 
            // dateTimePicker2
            // 
            dateTimePicker2.Enabled = false;
            dateTimePicker2.Location = new Point(167, 150);
            dateTimePicker2.Name = "dateTimePicker2";
            dateTimePicker2.Size = new Size(249, 23);
            dateTimePicker2.TabIndex = 24;
            // 
            // dateTimePicker3
            // 
            dateTimePicker3.Enabled = false;
            dateTimePicker3.Location = new Point(167, 111);
            dateTimePicker3.Name = "dateTimePicker3";
            dateTimePicker3.Size = new Size(249, 23);
            dateTimePicker3.TabIndex = 24;
            // 
            // textBox1
            // 
            textBox1.Location = new Point(167, 61);
            textBox1.Name = "textBox1";
            textBox1.PlaceholderText = "Nome ou Razão Social do Cliente";
            textBox1.Size = new Size(463, 23);
            textBox1.TabIndex = 14;
            // 
            // textBox2
            // 
            textBox2.Location = new Point(167, 91);
            textBox2.Name = "textBox2";
            textBox2.PlaceholderText = "E-mail do Cliente";
            textBox2.Size = new Size(463, 23);
            textBox2.TabIndex = 15;
            // 
            // textBox3
            // 
            textBox3.Location = new Point(167, 121);
            textBox3.Name = "textBox3";
            textBox3.PlaceholderText = "Telefone do Cliente";
            textBox3.Size = new Size(463, 23);
            textBox3.TabIndex = 16;
            // Cria um novo MaskedTextBox
            MaskedTextBox txtTelefone = new MaskedTextBox();
            txtTelefone.Mask = "(00) 00000-0000";
            this.Controls.Add(txtTelefone);
            // 
            // textBox4
            // 
            textBox4.Location = new Point(798, 31);
            textBox4.Name = "textBox4";
            textBox4.Size = new Size(335, 23);
            textBox4.TabIndex = 18;
            // Cria um novo MaskedTextBox
            MaskedTextBox txtCpfCnpj = new MaskedTextBox();
            txtCpfCnpj.TextChanged += TxtCpfCnpj_TextChanged;
            this.Controls.Add(txtCpfCnpj);
            // 
            // textBox5
            // 
            textBox5.Location = new Point(798, 61);
            textBox5.Name = "textBox5";
            textBox5.Size = new Size(335, 23);
            textBox5.TabIndex = 19;
            // Cria um novo MaskedTextBox
            MaskedTextBox txtInscricaoEstadual = new MaskedTextBox();
            txtInscricaoEstadual.Mask = "000.000.000-000";
            this.Controls.Add(txtInscricaoEstadual);
            // 
            // textBox6
            // 
            textBox6.Enabled = false;
            textBox6.Location = new Point(167, 31);
            textBox6.Name = "textBox6";
            textBox6.PlaceholderText = "ID do Cliente";
            textBox6.Size = new Size(186, 23);
            textBox6.TabIndex = 26;
            // 
            // textBox10
            // 
            textBox10.Location = new Point(167, 22);
            textBox10.Name = "textBox10";
            textBox10.PlaceholderText = "Nome ou Razão Social do Cliente";
            textBox10.Size = new Size(463, 23);
            textBox10.TabIndex = 14;
            // 
            // textBox11
            // 
            textBox11.Location = new Point(167, 52);
            textBox11.Name = "textBox11";
            textBox11.PlaceholderText = "E-mail do Cliente";
            textBox11.Size = new Size(463, 23);
            textBox11.TabIndex = 15;
            // 
            // textBox12
            // 
            textBox12.Location = new Point(167, 82);
            textBox12.Name = "textBox12";
            textBox12.PlaceholderText = "Telefone do Cliente";
            textBox12.Size = new Size(463, 23);
            textBox12.TabIndex = 16;
            // 
            // Lista_Clientes
            // 
            Lista_Clientes.Location = new Point(11, 34);
            Lista_Clientes.Name = "Lista_Clientes";
            Lista_Clientes.Size = new Size(1337, 349);
            Lista_Clientes.TabIndex = 27;
            Lista_Clientes.UseCompatibleStateImageBehavior = false;
            // 
            // g_Adicionar
            // 
            g_Adicionar.Controls.Add(b_VoltarEdit);
            g_Adicionar.Controls.Add(b_EditarCliente);
            g_Adicionar.Controls.Add(label2);
            g_Adicionar.Controls.Add(label3);
            g_Adicionar.Controls.Add(label4);
            g_Adicionar.Controls.Add(textBox6);
            g_Adicionar.Controls.Add(b_AdicionarCliente);
            g_Adicionar.Controls.Add(label5);
            g_Adicionar.Controls.Add(label13);
            g_Adicionar.Controls.Add(label6);
            g_Adicionar.Controls.Add(dateTimePicker2);
            g_Adicionar.Controls.Add(label7);
            g_Adicionar.Controls.Add(checkBox2);
            g_Adicionar.Controls.Add(label8);
            g_Adicionar.Controls.Add(dateTimePicker1);
            g_Adicionar.Controls.Add(label9);
            g_Adicionar.Controls.Add(comboBox2);
            g_Adicionar.Controls.Add(label10);
            g_Adicionar.Controls.Add(checkBox1);
            g_Adicionar.Controls.Add(label11);
            g_Adicionar.Controls.Add(textBox5);
            g_Adicionar.Controls.Add(label12);
            g_Adicionar.Controls.Add(textBox4);
            g_Adicionar.Controls.Add(textBox1);
            g_Adicionar.Controls.Add(comboBox1);
            g_Adicionar.Controls.Add(textBox2);
            g_Adicionar.Controls.Add(textBox3);
            g_Adicionar.Location = new Point(12, 40);
            g_Adicionar.Name = "g_Adicionar";
            g_Adicionar.Size = new Size(1158, 245);
            g_Adicionar.TabIndex = 32;
            g_Adicionar.TabStop = false;
            // 
            // g_Lista
            // 
            g_Lista.Controls.Add(b_Voltar);
            g_Lista.Controls.Add(label17);
            g_Lista.Controls.Add(Lista_Clientes);
            g_Lista.Controls.Add(b_ListarClienteSelecionado);
            g_Lista.Controls.Add(b_RemoverCliente);
            g_Lista.Location = new Point(12, 390);
            g_Lista.Name = "g_Lista";
            g_Lista.Size = new Size(1354, 72);
            g_Lista.TabIndex = 34;
            g_Lista.TabStop = false;
            // 
            // g_Pesquisar
            // 
            g_Pesquisar.Controls.Add(b_Voltar_Pesquisa);
            g_Pesquisar.Controls.Add(b_Listar);
            g_Pesquisar.Controls.Add(b_LimparFiltro);
            g_Pesquisar.Controls.Add(label14);
            g_Pesquisar.Controls.Add(label15);
            g_Pesquisar.Controls.Add(label16);
            g_Pesquisar.Controls.Add(dateTimePicker3);
            g_Pesquisar.Controls.Add(label25);
            g_Pesquisar.Controls.Add(textBox10);
            g_Pesquisar.Controls.Add(textBox11);
            g_Pesquisar.Controls.Add(textBox12);
            g_Pesquisar.Location = new Point(12, 332);
            g_Pesquisar.Name = "g_Pesquisar";
            g_Pesquisar.Size = new Size(1158, 35);
            g_Pesquisar.TabIndex = 33;
            g_Pesquisar.TabStop = false;
            // 
            // ListagemCompradores
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1423, 907);
            Controls.Add(b_NovoCliente);
            Controls.Add(g_Lista);
            Controls.Add(g_Pesquisar);
            Controls.Add(label1);
            Controls.Add(g_Adicionar);
            Controls.Add(b_PesquisarCliente);
            Name = "ListagemCompradores";
            Text = "Gerenciador de Clientes";
            g_Adicionar.ResumeLayout(false);
            g_Adicionar.PerformLayout();
            g_Lista.ResumeLayout(false);
            g_Lista.PerformLayout();
            g_Pesquisar.ResumeLayout(false);
            g_Pesquisar.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        private void TxtCpfCnpj_TextChanged(object sender, EventArgs e)
        {
            // Obtém o MaskedTextBox que disparou o evento
            MaskedTextBox txtCpfCnpj = (MaskedTextBox)sender;

            // Remove a máscara atual
            txtCpfCnpj.Mask = string.Empty;

            // Obtém o texto sem formatação
            string texto = txtCpfCnpj.Text.Replace(".", string.Empty).Replace("-", string.Empty).Replace("/", string.Empty);

            // Define a máscara de acordo com o número de caracteres digitados
            if (texto.Length <= 11)
            {
                txtCpfCnpj.Mask = "000.000.000-00";
            }
            else
            {
                txtCpfCnpj.Mask = "00.000.000/0000-00";
            }
        }

        #endregion

        private Label label1;
        private Button b_AdicionarCliente;
        private Button b_PesquisarCliente;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
        private Label label7;
        private Label label8;
        private Label label9;
        private Label label10;
        private Label label11;
        private Label label12;
        private TextBox textBox1;
        private TextBox textBox2;
        private TextBox textBox3;
        private ComboBox comboBox1;
        private TextBox textBox4;
        private TextBox textBox5;
        private CheckBox checkBox1;
        private ComboBox comboBox2;
        private DateTimePicker dateTimePicker1;
        private CheckBox checkBox2;
        private DateTimePicker dateTimePicker2;
        private Label label13;
        private ListView Lista_Clientes;
        private Button b_RemoverCliente;
        private Button b_ListarClienteSelecionado;
        private Button b_Voltar_Pesquisa;
        private GroupBox g_Adicionar;
        private GroupBox g_Pesquisar;
        private Button b_LimparFiltro;
        private Label label14;
        private Label label15;
        private Label label16;
        private DateTimePicker dateTimePicker3;
        private Label label25;
        private TextBox textBox10;
        private TextBox textBox11;
        private TextBox textBox12;
        private GroupBox g_Lista;
        private Label label17;
        private Button b_Listar;
        private Button b_Voltar;
        private Button button2;
        private Button b_NovoCliente;
        private Button b_EditarCliente;
        private Button b_VoltarEdit;
        private TextBox textBox6;
    }
}