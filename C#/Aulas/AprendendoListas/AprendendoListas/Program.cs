using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AprendendoListas
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> clientes = new List<string>();
            clientes.Add("Renan");
            clientes.Add("Fonseca");
            clientes.Add("Pedro");
            clientes.Add("Silva");
            clientes.Add("Claudio");
            clientes.Add("Melo");
            clientes.Add("Grazi");
            clientes.Add("Rosina");

            string pessoa = "João";
            clientes.Add(pessoa);
            Console.WriteLine(clientes.Count());
            Console.WriteLine("=========");

            foreach (string s in clientes)
            {
                Console.WriteLine(s);
            }

            clientes.RemoveAt(1);

            Console.WriteLine("=========");

            foreach (string s in clientes)
            {
                Console.WriteLine(s);
            }

            clientes.RemoveAll(cliente => cliente == "Silva");

            Console.WriteLine("=========");

            foreach (string s in clientes)
            {
                Console.WriteLine(s);
            }

            Console.WriteLine("=========");

            string busca = clientes.Find(cliente => cliente.Length > 5);
            Console.WriteLine(busca);

            Console.WriteLine("=========");

            List<string> busca_todos = clientes.FindAll(cliente => cliente.Length > 5);
            foreach (string s in busca_todos)
            {
                Console.WriteLine(s);
            }
        }

    }
}