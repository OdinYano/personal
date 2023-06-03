using System.ComponentModel.Design;
using System.Runtime.Serialization.Formatters.Binary;

namespace AprendendoStructs
{
    class CMD
    {
        [System.Serializable]
        struct Cliente
        {
            public string nome;
            public string email;
            public string cpf_cnpj;
        }

        static List<Cliente> clientes = new List<Cliente>();
        enum Menu { Listagem = 1, Adicionar = 2, Remover = 3, Sair = 4}

        static void Main(string[] args)
        {
            Carregar();
            bool escolheuSair = false;

            while (!escolheuSair)
            {
                Console.WriteLine("Sistema de clientes - Bem Vindo!");
                Console.WriteLine("1-Listagem\n2-Adicionar\n3-Remover\n4-Sair");
                int intOp = int.Parse(Console.ReadLine());
                Menu opcao = (Menu)intOp;

                switch (opcao)
                {
                    case Menu.Listagem:
                        Listagem();
                        break;
                    case Menu.Adicionar:
                        Adicionar();
                        break;
                    case Menu.Remover:
                        Remover();
                        break;
                    case Menu.Sair:
                        escolheuSair = true;
                        break;
                }
                Console.Clear();
            }

        }

        static void Adicionar()
        {
            Cliente cliente = new Cliente();
            Console.WriteLine("Casdastro cliente: ");
            Console.WriteLine("Nome do Cliente: ");
            cliente.nome = Console.ReadLine();
            Console.WriteLine("Email do Cliente: ");
            cliente.email = Console.ReadLine();
            Console.WriteLine("CPF/CNPJ do Cliente: ");
            cliente.cpf_cnpj = Console.ReadLine();

            clientes.Add(cliente);
            Salvar();
            Console.WriteLine("Cadastro concluido aperte enter para sair.");
            Console.ReadLine();
        }

        static void Remover()
        {
            Listagem();
            Console.WriteLine("Digite o ID do cliente que deseja remover: ");
            int id = int.Parse(Console.ReadLine());
            if(id >= 0 && id <= clientes.Count)
            {
                clientes.RemoveAt(id);
                Salvar();
            }
            else
            {
                Console.WriteLine("ID digitado não é valido!");
                Console.ReadLine();
            }
        }

        static void Listagem()
        {
            if(clientes.Count > 0)
            {
                Console.WriteLine("Lista de clientes: ");
                int i = 0;
                foreach (Cliente cliente in clientes)
                {
                    Console.WriteLine($"ID: {i}");
                    Console.WriteLine($"Nome: {cliente.nome}");
                    Console.WriteLine($"Email: {cliente.email}");
                    Console.WriteLine($"CPF/CNPJ: {cliente.cpf_cnpj}");
                    i++;
                }
                Console.WriteLine("Cadastro concluido aperte enter para sair.");
                Console.ReadLine();

            }
            else
            { 
                Console.WriteLine("Nenhum cliente cadastrado!"); 
            }
        }

        static void Salvar()
        {
            FileStream stream = new FileStream("clientes.dat", FileMode.OpenOrCreate);
            BinaryFormatter encoder = new BinaryFormatter();

            encoder.Serialize(stream, clientes);
            stream.Close();
        }

        static void Carregar()
        {
            FileStream stream = new FileStream("clientes.dat", FileMode.OpenOrCreate);
            try
            {              
                BinaryFormatter encoder = new BinaryFormatter();

                clientes = (List<Cliente>)encoder.Deserialize(stream);
                
                if(clientes == null)
                {
                    clientes = new List<Cliente>();
                }
            }
            catch (Exception ex)
            {
                clientes = new List<Cliente>();
            }
            stream.Close();
        }
    }
}