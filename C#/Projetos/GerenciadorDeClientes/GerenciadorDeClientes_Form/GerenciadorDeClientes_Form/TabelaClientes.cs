using System;
using MySql.Data.MySqlClient;

namespace MyTable
{
    public class Program
    {
        public static void __Main__(string[] args)
        {
            string connectionString = "server=localhost;user=root;database=PROJETO;port=3306;password=1234";
            MySqlConnection connection = new MySqlConnection(connectionString);

            try
            {
                Console.WriteLine("Conectando ao banco de dados...");
                connection.Open();

                string checkTableSql = "SHOW TABLES LIKE 'clientes'";
                MySqlCommand checkTableCmd = new MySqlCommand(checkTableSql, connection);
                object result = checkTableCmd.ExecuteScalar();

                if (result == null)
                {
                    Console.WriteLine("Tabela clientes não existe. Criando...");
                    string createTableSql = @"
                        CREATE TABLE clientes (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome_razao_social VARCHAR(150) NOT NULL,
                            email VARCHAR(150) NOT NULL,
                            telefone VARCHAR(11) NOT NULL,
                            data_cadastro DATE NOT NULL,
                            tipo_pessoa ENUM('Física', 'Jurídica') NOT NULL,
                            cpf_cnpj VARCHAR(14) NOT NULL,
                            inscricao_estadual VARCHAR(12),
                            isento BOOLEAN,
                            genero ENUM('Feminino', 'Masculino', 'Outro'),
                            data_nascimento DATE,
                            bloqueado BOOLEAN
                        )";
                    MySqlCommand createTableCmd = new MySqlCommand(createTableSql, connection);
                    createTableCmd.ExecuteNonQuery();
                    Console.WriteLine("Tabela clientes criada com sucesso.");
                }
                else
                {
                    Console.WriteLine("Tabela clientes já existe.");
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            connection.Close();
            Console.WriteLine("Conexão encerrada.");
        }
    }
}
