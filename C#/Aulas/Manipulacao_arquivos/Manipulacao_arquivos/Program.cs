

using System.Xml;

namespace ManipulandoArquivos
{
    class Program
    {
        static void Main(string[] args)
        {
            
            StreamWriter escritor = new StreamWriter("teste.txt");
            escritor.WriteLine("namespace Projeto_novo");
            escritor.Close();
            Console.WriteLine("Arquivo gerado");

            StreamWriter editor = File.AppendText("teste.txt");
            editor.WriteLine("\r\n{\r\n    class Program\r\n    {\r\n        static void Main(string[] args) \r\n        {\r\n        }\r\n    }\r\n}");
            editor.Close();
            

            StreamReader leitor = new StreamReader("teste.txt");

            List<string> linhas = new List<string>();
            string linha = "";

            while(linha != null)
            {
                linha = leitor.ReadLine();
                if (linha != null)
                {
                    linhas.Add(linha);
                    Console.WriteLine(linha);
                }
                
            }
            Console.WriteLine("=========");
            Console.WriteLine(linhas[0]);
            leitor.Close();

            StreamWriter modificador = new StreamWriter("teste.txt");
            linhas[0] = "namespace Novo_projeto";

            linha = "";
            foreach (string nova_linha in linhas)
            {
                linha = linha + nova_linha;
                linha = linha + "\n";
                modificador.WriteLine(nova_linha);
            }
            Console.WriteLine("=========");
            Console.WriteLine(linha);
            

            modificador.Close();
        }

    }
}