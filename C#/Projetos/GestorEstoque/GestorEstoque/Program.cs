using GestorEstoque;
using System.Runtime.Serialization.Formatters.Binary;

namespace gestorEstoque
{
    [System.Serializable]
    class Program
    {
        static List<IEstoque> produtos = new List<IEstoque>();
        enum Menu { Listar = 1, Adicionar = 2, Remover = 3, Entrada = 4, Saida = 5, Sair = 6 }
        static void Main(string[] args)
        {
            bool escolheuSair = false;
            Carregar();
            while (!escolheuSair)
            {
                Console.WriteLine("Sistema de estoque");
                Console.WriteLine("1-Listar\n2-Adicionar\n3-Remover\n4-Entrada\n5-Saida\n6-Sair");
                string opStr = Console.ReadLine();
                int opInt = int.Parse(opStr);

                if (opInt > 0 && opInt < 7)
                {
                    Menu opcao = (Menu)opInt;
                    Console.Clear();

                    switch (opcao)
                    {
                        case Menu.Listar:
                            Listagem();
                            Console.ReadLine();
                            break;
                        case Menu.Adicionar:
                            Cadastro();
                            break;
                        case Menu.Remover:
                            Remover();
                            break;
                        case Menu.Entrada:
                            Entrada();
                            break;
                        case Menu.Saida:
                            Saida();
                            break;
                        case Menu.Sair:
                            escolheuSair = true;
                            break;
                    }
                }
                else
                {
                    escolheuSair = true;
                }
                Console.Clear();
            }
        }

        static void Listagem()
        {
            Console.WriteLine("Lista de produtos");
            int i = 1;
            foreach (IEstoque produto in produtos)
            {
                Console.WriteLine("ID: " + i);
                produto.Exibir();
                i++;
            }
        }

        static void Remover()
        {
            Listagem();
            Console.WriteLine("Digite o ID do produto que deseja remover ou 0 para voltar: ");
            int id = int.Parse(Console.ReadLine());

            if (id != 0)
            {
                if (id > 0 && id <= produtos.Count)
                {
                    produtos.RemoveAt(id - 1);
                    Console.WriteLine("Produto removido com sucesso.");
                }
            }
        }

        static void Entrada()
        {
            Listagem();
            Console.WriteLine("Digite o ID do produto que deseja dar entrada 0 para voltar: ");
            int id = int.Parse(Console.ReadLine());

            if (id != 0)
            {
                if (id > 0 && id <= produtos.Count)
                {
                    produtos[id - 1].AdicionarEntrada();
                    Salvar();
                }
            }
        }

        static void Saida()
        {
            Listagem();
            Console.WriteLine("Digite o ID do produto que deseja dar saida 0 para voltar: ");
            int id = int.Parse(Console.ReadLine());

            if (id != 0)
            {
                if (id > 0 && id <= produtos.Count)
                {
                    produtos[id - 1].AdicionarSaida();
                    Salvar();
                }
            }
        }

        enum MenuCadastro { Produto_Fisico = 1, Ebook = 2, Curso = 3, Voltar = 4}
        static void Cadastro()
        {
            bool escolheuVoltar = false;
            while (!escolheuVoltar)
            {
                Console.WriteLine("Cadastro de Produto");
                Console.WriteLine("1-Produto Fisico\n2-Ebook\n3-Curso\n4-Voltar");
                string opStr = Console.ReadLine();
                int opInt = int.Parse(opStr);

                if (opInt > 0 && opInt < 5)
                {
                    MenuCadastro opcao = (MenuCadastro)opInt;

                    switch (opcao)
                    {
                        case MenuCadastro.Produto_Fisico:
                            CadastroProdutoFisico();
                            break;
                        case MenuCadastro.Ebook:
                            CadastroEbook();
                            break;
                        case MenuCadastro.Curso:
                            CadastroCurso();
                            break;
                        case MenuCadastro.Voltar:
                            escolheuVoltar = true;
                            break;
                    }
                    Console.Clear();
                }
            }
        }

        static void CadastroProdutoFisico()
        {
            Console.WriteLine("Cadastro de Produto Fisico: ");
            Console.WriteLine("Nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine("Preço: ");
            float preco = float.Parse(Console.ReadLine());
            Console.WriteLine("Frete: ");
            float frete = float.Parse(Console.ReadLine());

            ProdutoFisico pf = new ProdutoFisico(nome, preco, frete);
            produtos.Add(pf);
            Salvar();
        }

        static void CadastroEbook()
        {
            Console.WriteLine("Cadastro de Ebook: ");
            Console.WriteLine("Nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine("Preço: ");
            float preco = float.Parse(Console.ReadLine());
            Console.WriteLine("Autor: ");
            string autor = Console.ReadLine();

            Ebook eb = new Ebook(nome, preco, autor);
            produtos.Add(eb);
            Salvar();
        }

        static void CadastroCurso()
        {
            Console.WriteLine("Cadastro de Curso: ");
            Console.WriteLine("Nome: ");
            string nome = Console.ReadLine();
            Console.WriteLine("Preço: ");
            float preco = float.Parse(Console.ReadLine());
            Console.WriteLine("Autor: ");
            string autor = Console.ReadLine();

            Curso cs = new Curso(nome, preco, autor);
            produtos.Add(cs);
            Salvar();
        }

        static void Salvar()
        {
            FileStream stream = new FileStream("produtos.dat", FileMode.OpenOrCreate);
            BinaryFormatter encoder = new BinaryFormatter();

            encoder.Serialize(stream, produtos);

            stream.Close();
        }

        static void Carregar()
        {
            FileStream stream = new FileStream("produtos.dat", FileMode.OpenOrCreate);
            BinaryFormatter encoder = new BinaryFormatter();

            try
            {
                produtos = (List<IEstoque>)encoder.Deserialize(stream);

                if (produtos == null)
                {
                    produtos = new List<IEstoque>();
                }
            }
            catch (Exception e)
            {
                produtos = new List<IEstoque>();
            }
            

            stream.Close();
        }
    }
}