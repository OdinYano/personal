namespace AprendendoPOO
{
    class Jogo
    {
        public string titulo;
        public string genero;
        public string desenvolvedora;
        public float preco;

        public void Abrir()
        {
            Console.WriteLine("Abrindo...");
        }

        public void Carregar()
        {
            Console.WriteLine("Carregando...");
        }

        public void Fechar()
        {
            Console.WriteLine("Aperte ESC para sair!");
        }
    }
}