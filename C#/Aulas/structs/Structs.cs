using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AprendendoStructs
{
    class Program
    {
        struct Produto
        {
            public string nome;
            public float preco;
            public float peso;
            public string marca;

            public Produto(string nome, float preco, float peso, string marca)
            {
                this.nome = nome;
                this.preco = preco;
                this.peso = peso;
                this.marca = marca;
            }

            public void ExibirInfo()
            {
                Console.WriteLine($"Nome: {this.nome}");
                Console.WriteLine($"Preço: R$ {this.preco}");
                Console.WriteLine($"Peso: {this.peso}");
                Console.WriteLine($"Marca: {this.marca}");
            }

            public string AdicionarCupom(float porcentagem)
            {
                float desconto = this.preco * porcentagem / 100f;
                string retorno = $"Preço com cupom de {porcentagem}%: R$ {this.preco - desconto}";
                return retorno;
            }
        }
        static void Main(string[] args)
        {
            Produto bola = new Produto("Bola Amarela", 15f, 14f, "nike");
            Produto balde = new Produto("balde", 12f, 2f, "pp");

            bola.ExibirInfo();
            Console.WriteLine("===========");
            balde.ExibirInfo() ;

            float cupom = 50f;

            string valor_final = bola.AdicionarCupom(cupom);
            Console.WriteLine(valor_final);


            Console.ReadLine();
        }
    }
}