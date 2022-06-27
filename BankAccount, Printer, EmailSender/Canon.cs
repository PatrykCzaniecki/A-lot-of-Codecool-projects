namespace DesignPatternsInfo;

public class Canon : IPrinter
{
    public void Print(string content)
    {
        Console.WriteLine("Canon printing " + content);
    }
}