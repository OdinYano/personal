using aulasElemar_01;
using System.Runtime.CompilerServices;
/*
Console.WriteLine("Hello, World!");

int j = 0;

while (j < 10)
{
    System.Console.WriteLine(j);
    j++;
}

for (var i = 0; i < 10; i++)
{
    System.Console.WriteLine(i);

    if (i % 2 == 0)
    { 
        System.Console.WriteLine("Par"); 
    }
    else
    {
            System.Console.WriteLine("Impar");
    }
}
Console.Clear();
*/
Produto p1 = new Produto();

p1.Nome = "Panela";
p1.Codigo = "12345";
p1.Preco = 10.9M;

System.Console.WriteLine(p1.Nome);
System.Console.WriteLine(p1.Codigo);
System.Console.WriteLine(p1.Preco);

Funcionario f1 = new Funcionario();

f1.Nome = "Renan";
f1.endereco.Cidade = "Farroupilha";

namespace aulasElemar_01
{
    public class Produto
    {
        public string Nome;
        public string Codigo;
        public decimal Preco;
    }

    public class Funcionario
    {
        public string id;
        public string Nome;
        public Endereco endereco;
    }

    public class Endereco
    {
        public string Cidade;
        public string Bairro;
    }
}


