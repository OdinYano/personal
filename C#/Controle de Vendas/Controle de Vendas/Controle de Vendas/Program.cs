using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using OfficeOpenXml;

class Program
{
    static List<Cliente> clientes = new List<Cliente>();
    static List<Venda> vendas = new List<Venda>();
    static string filePath = "dados.xlsx";

    static void Main()
    {
        CarregarDados();

        while (true)
        {
            Console.WriteLine("1. Cadastrar Cliente");
            Console.WriteLine("2. Registrar Venda");
            Console.WriteLine("3. Mostrar Clientes");
            Console.WriteLine("4. Mostrar Vendas");
            Console.WriteLine("5. Sair");

            Console.Write("Escolha uma opção: ");
            string opcao = Console.ReadLine();

            switch (opcao)
            {
                case "1":
                    CadastrarCliente();
                    break;
                case "2":
                    RegistrarVenda();
                    break;
                case "3":
                    MostrarClientes();
                    break;
                case "4":
                    MostrarVendas();
                    break;
                case "5":
                    SalvarDados();
                    return;
                default:
                    Console.WriteLine("Opção inválida. Tente novamente.");
                    break;
            }
        }
    }

    static void CadastrarCliente()
    {
        Console.Write("Nome do Cliente: ");
        string nome = Console.ReadLine();
        Console.Write("E-mail do Cliente: ");
        string email = Console.ReadLine();

        Cliente cliente = new Cliente(nome, email);
        clientes.Add(cliente);
        Console.WriteLine("Cliente cadastrado com sucesso!");
    }

    static void RegistrarVenda()
    {
        Console.Write("Nome do Cliente: ");
        string nomeCliente = Console.ReadLine();
        Cliente cliente = clientes.Find(c => c.Nome == nomeCliente);

        if (cliente == null)
        {
            Console.WriteLine("Cliente não encontrado.");
            return;
        }

        Console.Write("Valor da Venda: ");
        decimal valor = Convert.ToDecimal(Console.ReadLine());

        Venda venda = new Venda(cliente, valor);
        vendas.Add(venda);
        Console.WriteLine("Venda registrada com sucesso!");
    }

    static void MostrarClientes()
    {
        Console.WriteLine("Lista de Clientes:");
        foreach (var cliente in clientes)
        {
            Console.WriteLine($"{cliente.Nome} - {cliente.Email}");
        }
    }

    static void MostrarVendas()
    {
        Console.WriteLine("Lista de Vendas:");
        foreach (var venda in vendas)
        {
            Console.WriteLine($"{venda.Cliente.Nome} - Valor: {venda.Valor:C}");
        }
    }

    static void SalvarDados()
    {
        FileInfo file = new FileInfo(filePath);
        ExcelPackage.LicenseContext = LicenseContext.NonCommercial; 

        using (ExcelPackage package = new ExcelPackage(file))
        {
            ExcelWorksheet worksheetClientes = package.Workbook.Worksheets.Add("Clientes");
            worksheetClientes.Cells.LoadFromCollection(clientes.Select(c => new { c.Nome, c.Email }), true);

            ExcelWorksheet worksheetVendas = package.Workbook.Worksheets.Add("Vendas");
            worksheetVendas.Cells.LoadFromCollection(vendas.Select(v => new { ClienteNome = v.Cliente.Nome, v.Valor }), true);

            package.Save();
        }
    }

    static void CarregarDados()
    {
        FileInfo file = new FileInfo(filePath);
        if (file.Exists)
        {
            using (ExcelPackage package = new ExcelPackage(file))
            {
                ExcelWorksheet worksheetClientes = package.Workbook.Worksheets["Clientes"];
                clientes = new List<Cliente>();
                int rowCount = worksheetClientes.Dimension.Rows;

                for (int row = 2; row <= rowCount; row++) // Começando da segunda linha, pois a primeira geralmente contém cabeçalhos
                {
                    string nome = worksheetClientes.Cells[row, 1].Text;
                    string email = worksheetClientes.Cells[row, 2].Text;

                    Cliente cliente = new Cliente(nome, email);
                    clientes.Add(cliente);
                }

                ExcelWorksheet worksheetVendas = package.Workbook.Worksheets["Vendas"];
                vendas = new List<Venda>();
                rowCount = worksheetVendas.Dimension.Rows;

                for (int row = 2; row <= rowCount; row++)
                {
                    string nomeCliente = worksheetVendas.Cells[row, 1].Text;
                    Cliente cliente = clientes.Find(c => c.Nome == nomeCliente);

                    if (cliente == null)
                    {
                        Console.WriteLine($"Cliente '{nomeCliente}' não encontrado. Ignorando venda.");
                        continue;
                    }

                    decimal valor = decimal.Parse(worksheetVendas.Cells[row, 2].Text);
                    Venda venda = new Venda(cliente, valor);
                    vendas.Add(venda);
                }
            }
        }
    }
}

    class Cliente
{
    public string Nome { get; set; }
    public string Email { get; set; }

    public Cliente(string nome, string email)
    {
        Nome = nome;
        Email = email;
    }
}

class Venda
{
    public Cliente Cliente { get; set; }
    public decimal Valor { get; set; }

    public Venda(Cliente cliente, decimal valor)
    {
        Cliente = cliente;
        Valor = valor;
    }
}
