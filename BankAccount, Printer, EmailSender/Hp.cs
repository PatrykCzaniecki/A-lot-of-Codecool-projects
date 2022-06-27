namespace DesignPatternsInfo;

public class Hp : IPrinter
{
    public void Print(string content)
    {
        Console.WriteLine("Hp printing " + content);
    }
}