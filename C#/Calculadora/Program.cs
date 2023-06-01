﻿using System;
using System.Collections;
using System.Linq;
using System.Text;

namespace Calculadora
{
    class Program
    {

        enum Menu { Soma = 1, Subtracao = 2, Divisao = 3, Multiplicacao = 4, Potencia = 5, Raiz = 6, Sair = 7 }

        static void Main(string[] args)
        {

            bool escolheuSair = false;
            while (!escolheuSair)
            {
                Console.WriteLine("Seja Bem Vindo ao Calc, selecione uma opção:");
                Console.WriteLine("1- Soma\n2- Subtracao\n3- Divisao\n4- Multiplicacao\n5- Potencia\n6- Raiz\n7- Sair");

                Menu opcao = (Menu)int.Parse(Console.ReadLine());
                Console.WriteLine(opcao);
                switch (opcao)
                {
                    case Menu.Soma:
                        Soma();
                        break;

                    case Menu.Subtracao:
                        Subtracao();
                        break;

                    case Menu.Divisao:
                        Divisao();
                        break;

                    case Menu.Multiplicacao:
                        Multiplicacao();
                        break;

                    case Menu.Potencia:
                        Potencia();
                        break;

                    case Menu.Raiz:
                        Raiz();
                        break;

                    case Menu.Sair:
                        escolheuSair = true;
                        break;
                }
                Console.Clear();
            }
        }

        static void Soma()
        {
            Console.WriteLine("Soma dois numeros: ");
            Console.WriteLine("Digite o primeiro numero: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o segundo numero: ");
            int b = int.Parse(Console.ReadLine());
            int resultado = a + b;
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }

        static void Subtracao()
        {
            Console.WriteLine("Subtrai dois numeros: ");
            Console.WriteLine("Digite o primeiro numero: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o segundo numero: ");
            int b = int.Parse(Console.ReadLine());
            int resultado = a - b;
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }

        static void Divisao()
        {
            Console.WriteLine("Divisao dois numeros: ");
            Console.WriteLine("Digite o primeiro numero: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o segundo numero: ");
            int b = int.Parse(Console.ReadLine());
            float resultado = (float)a / (float)b;
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }

        static void Multiplicacao()
        {
            Console.WriteLine("Multiplica dois numeros: ");
            Console.WriteLine("Digite o primeiro numero: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o segundo numero: ");
            int b = int.Parse(Console.ReadLine());
            int resultado = a * b;
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }

        static void Potencia()
        {
            Console.WriteLine("Potência de um numero: ");
            Console.WriteLine("Digite a base: ");
            int a = int.Parse(Console.ReadLine());
            Console.WriteLine("Digite o expoente: ");
            int b = int.Parse(Console.ReadLine());
            double resultado = Math.Pow(a, b);
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }

        static void Raiz()
        {
            Console.WriteLine("Raiz de um numero: ");
            Console.WriteLine("Digite o primeiro numero: ");
            int a = int.Parse(Console.ReadLine());
            double resultado = Math.Sqrt(a);
            Console.WriteLine($"O resultado é: {resultado}");
            Console.WriteLine("Aperte enter para voltar ao menu.");
            Console.ReadLine();
        }
    }
}