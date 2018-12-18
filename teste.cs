using System;

namespace Teste
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Testes");

            string[] testes = new string[3] {"teste", "teste2", "teste3"};
            foreach (string i in testes)
                Console.WriteLine(i);
        }
    }
}