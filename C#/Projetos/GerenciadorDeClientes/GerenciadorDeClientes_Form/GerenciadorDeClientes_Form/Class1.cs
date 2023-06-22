using System;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;

namespace ClasseCliente
{
    public class Cliente
    {
        public int Id { get; set; }
        public string NomeRazaoSocial { get; set; }
        public string Email { get; set; }
        public string Telefone { get; set; }
        public DateTime DataCadastro { get; set; }
        public string TipoPessoa { get; set; }
        public string CpfCnpj { get; set; }
        public string InscricaoEstadual { get; set; }
        public bool Isento { get; set; }
        public string Genero { get; set; }
        public DateTime? DataNascimento { get; set; }
        public bool Bloqueado { get; set; }
    }

    public class ClienteDAO
    {
        private string connectionString;

        public ClienteDAO(string server, string database, string user, string password)
        {
            this.connectionString = $"server={server};database={database};user={user};password={password}";
        }

        public void Inserir(Cliente cliente)
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                if (EmailJaCadastrado(cliente.Email, null, connection))
                {
                    throw new Exception("O e-mail informado já está cadastrado para outro cliente.");
                }

                if (CpfCnpjJaCadastrado(cliente.CpfCnpj, null, connection))
                {
                    throw new Exception("O CPF/CNPJ informado já está cadastrado para outro cliente.");
                }

                string sql = @"
                    INSERT INTO clientes (
                        nome_razao_social,
                        email,
                        telefone,
                        data_cadastro,
                        tipo_pessoa,
                        cpf_cnpj,
                        inscricao_estadual,
                        isento,
                        genero,
                        data_nascimento,
                        bloqueado
                    ) VALUES (
                        @nome_razao_social,
                        @email,
                        @telefone,
                        @data_cadastro,
                        @tipo_pessoa,
                        @cpf_cnpj,
                        @inscricao_estadual,
                        @isento,
                        @genero,
                        @data_nascimento,
                        @bloqueado
                    )";
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                cmd.Parameters.AddWithValue("@nome_razao_social", cliente.NomeRazaoSocial);
                cmd.Parameters.AddWithValue("@email", cliente.Email);
                cmd.Parameters.AddWithValue("@telefone", cliente.Telefone);
                cmd.Parameters.AddWithValue("@data_cadastro", cliente.DataCadastro);
                cmd.Parameters.AddWithValue("@tipo_pessoa", cliente.TipoPessoa);
                cmd.Parameters.AddWithValue("@cpf_cnpj", cliente.CpfCnpj);
                cmd.Parameters.AddWithValue("@inscricao_estadual", cliente.InscricaoEstadual);
                cmd.Parameters.AddWithValue("@isento", cliente.Isento);
                cmd.Parameters.AddWithValue("@genero", cliente.Genero);
                cmd.Parameters.AddWithValue("@data_nascimento", cliente.DataNascimento);
                cmd.Parameters.AddWithValue("@bloqueado", cliente.Bloqueado);
                cmd.ExecuteNonQuery();
            }
        }

        public void Atualizar(Cliente cliente)
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                if (EmailJaCadastrado(cliente.Email, cliente.Id, connection))
                {
                    throw new Exception("O e-mail informado já está cadastrado para outro cliente.");
                }

                if (CpfCnpjJaCadastrado(cliente.CpfCnpj, cliente.Id, connection))
                {
                    throw new Exception("O CPF/CNPJ informado já está cadastrado para outro cliente.");
                }

                string sql = @"
                    UPDATE clientes SET
                        nome_razao_social = @nome_razao_social,
                        email = @email,
                        telefone = @telefone,
                        data_cadastro = @data_cadastro,
                        tipo_pessoa = @tipo_pessoa,
                        cpf_cnpj = @cpf_cnpj,
                        inscricao_estadual = @inscricao_estadual,
                        isento = @isento,
                        genero = @genero,
                        data_nascimento = @data_nascimento,
                        bloqueado = @bloqueado
                    WHERE id = @id";
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                cmd.Parameters.AddWithValue("@id", cliente.Id);
                cmd.Parameters.AddWithValue("@nome_razao_social", cliente.NomeRazaoSocial);
                cmd.Parameters.AddWithValue("@email", cliente.Email);
                cmd.Parameters.AddWithValue("@telefone", cliente.Telefone);
                cmd.Parameters.AddWithValue("@data_cadastro", cliente.DataCadastro);
                cmd.Parameters.AddWithValue("@tipo_pessoa", cliente.TipoPessoa);
                cmd.Parameters.AddWithValue("@cpf_cnpj", cliente.CpfCnpj);
                cmd.Parameters.AddWithValue("@inscricao_estadual", cliente.InscricaoEstadual);
                cmd.Parameters.AddWithValue("@isento", cliente.Isento);
                cmd.Parameters.AddWithValue("@genero", cliente.Genero);
                cmd.Parameters.AddWithValue("@data_nascimento", cliente.DataNascimento);
                cmd.Parameters.AddWithValue("@bloqueado", cliente.Bloqueado);
                cmd.ExecuteNonQuery();
            }
        }

        public void Excluir(int id)
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                string sql = "DELETE FROM clientes WHERE id = @id";
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                cmd.Parameters.AddWithValue("@id", id);
                cmd.ExecuteNonQuery();
            }
        }

        public List<Cliente> Listar()
        {
            List<Cliente> clientes = new List<Cliente>();

            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                string sql = "SELECT * FROM clientes";
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                MySqlDataReader reader = cmd.ExecuteReader();

                while (reader.Read())
                {
                    Cliente cliente = new Cliente();
                    cliente.Id = reader.GetInt32("id");
                    cliente.NomeRazaoSocial = reader.GetString("nome_razao_social");
                    cliente.Email = reader.GetString("email");
                    cliente.Telefone = reader.GetString("telefone");
                    cliente.DataCadastro = reader.GetDateTime("data_cadastro");
                    cliente.TipoPessoa = reader.GetString("tipo_pessoa");
                    cliente.CpfCnpj = reader.GetString("cpf_cnpj");
                    if (!reader.IsDBNull(reader.GetOrdinal("inscricao_estadual")))
                    {
                        cliente.InscricaoEstadual = reader.GetString("inscricao_estadual");
                    }
                    else
                    {
                        cliente.InscricaoEstadual = " ";
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("isento")))
                    {
                        cliente.Isento = reader.GetBoolean("isento");
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("genero")))
                    {
                        cliente.Genero = reader.GetString("genero");
                    }
                    else
                    {
                        cliente.Genero = " ";
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("data_nascimento")))
                    {
                        cliente.DataNascimento = reader.GetDateTime("data_nascimento");
                    }
                    else
                    {
                        cliente.DataNascimento = DateTime.Today;
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("bloqueado")))
                    {
                        cliente.Bloqueado = reader.GetBoolean("bloqueado");
                    }
                    else
                    {
                        cliente.Bloqueado = false;
                    }
                    clientes.Add(cliente);
                }
                reader.Close();
            }
            return clientes;
        }
        public List<Cliente> Pesquisar(string filtro)
        {
            List<Cliente> clientes = new List<Cliente>();

            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                string sql = "SELECT * FROM clientes WHERE " + filtro;
                MySqlCommand cmd = new MySqlCommand(sql, connection);
                MySqlDataReader reader = cmd.ExecuteReader();

                while (reader.Read())
                {
                    Cliente cliente = new Cliente();
                    cliente.Id = reader.GetInt32("id");
                    cliente.NomeRazaoSocial = reader.GetString("nome_razao_social");
                    cliente.Email = reader.GetString("email");
                    cliente.Telefone = reader.GetString("telefone");
                    cliente.DataCadastro = reader.GetDateTime("data_cadastro");
                    cliente.TipoPessoa = reader.GetString("tipo_pessoa");
                    cliente.CpfCnpj = reader.GetString("cpf_cnpj");
                    if (!reader.IsDBNull(reader.GetOrdinal("inscricao_estadual")))
                    {
                        cliente.InscricaoEstadual = reader.GetString("inscricao_estadual");
                    }
                    else
                    {
                        cliente.InscricaoEstadual = " ";
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("isento")))
                    {
                        cliente.Isento = reader.GetBoolean("isento");
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("genero")))
                    {
                        cliente.Genero = reader.GetString("genero");
                    }
                    else
                    {
                        cliente.Genero = " ";
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("data_nascimento")))
                    {
                        cliente.DataNascimento = reader.GetDateTime("data_nascimento");
                    }
                    else
                    {
                        cliente.DataNascimento = DateTime.Today;
                    }
                    if (!reader.IsDBNull(reader.GetOrdinal("bloqueado")))
                    {
                        cliente.Bloqueado = reader.GetBoolean("bloqueado");
                    }
                    else
                    {
                        cliente.Bloqueado = false;
                    }
                    clientes.Add(cliente);
                }
                reader.Close();
            }
            return clientes;
        }


        private bool EmailJaCadastrado(string email, int? id, MySqlConnection connection)
        {
            string sql = "SELECT COUNT(*) FROM clientes WHERE email = @email";
            if (id.HasValue)
            {
                sql += " AND id <> @id";
            }
            MySqlCommand cmd = new MySqlCommand(sql, connection);
            cmd.Parameters.AddWithValue("@email", email);
            if (id.HasValue)
            {
                cmd.Parameters.AddWithValue("@id", id.Value);
            }
            long count = (long)cmd.ExecuteScalar();
            return count > 0;
        }

        private bool CpfCnpjJaCadastrado(string cpfCnpj, int? id, MySqlConnection connection)
        {
            string sql = "SELECT COUNT(*) FROM clientes WHERE cpf_cnpj = @cpf_cnpj";
            if (id.HasValue)
            {
                sql += " AND id <> @id";
            }
            MySqlCommand cmd = new MySqlCommand(sql, connection);
            cmd.Parameters.AddWithValue("@cpf_cnpj", cpfCnpj);
            if (id.HasValue)
            {
                cmd.Parameters.AddWithValue("@id", id.Value);
            }
            long count = (long)cmd.ExecuteScalar();
            return count > 0;
        }
    }
}
