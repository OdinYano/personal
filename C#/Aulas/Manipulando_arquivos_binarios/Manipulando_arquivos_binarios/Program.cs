using System.Runtime.InteropServices;
using System.Runtime.Serialization.Formatters.Binary;

internal class Program
{
    [System.Serializable]
    struct Produto
    {
        public string nome;
        public float preco;
    }
    private static void Main(string[] args)
    {
        List<string> linguagens = new List<string>();
        linguagens.Add("python");
        linguagens.Add("genero");
        linguagens.Add("c#");
        linguagens.Add("java");

        Produto banana = new Produto();
        {
            banana.nome = "banana";
            banana.preco = 1f;
        }

        FileStream stream = new("meuarquivo.renan", FileMode.OpenOrCreate);
        BinaryFormatter encoder = new BinaryFormatter();

        /*
        encoder.Serialize(stream, 120);
        encoder.Serialize(stream, "renan fonseca");
        encoder.Serialize(stream, true);
        

        encoder.Serialize(stream, linguagens);
        encoder.Serialize(stream, banana);
        */
        
        List<string> listadoDoArquivo = (List<string>)encoder.Deserialize(stream);
        Produto prod = (Produto)encoder.Deserialize(stream);

        Console.WriteLine(listadoDoArquivo[0]);
        Console.WriteLine(prod.nome);
        
        stream.Close();
    }
}