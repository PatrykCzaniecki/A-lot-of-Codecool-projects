public delegate int MathematicalOperation(int a, int b);

public class Program
{
    public static int Add(int a, int b) => a + b;
    public static int Subtract(int a, int b) => a - b;
    public static int Multiply(int a, int b) => a * b;
    public static int Divide(int a, int b) => a / b;
    public static int Modulo(int a, int b) => a % b;

    public static MathematicalOperation MathematicalOperationFactory(string operationType) => operationType switch
    {
        "+" => Add,
        "-" => Subtract,
        "*" => Multiply,
        "/" => Divide,
        "%" => Modulo,
        _ => throw new NotImplementedException()
    };

    public static void WorkingWithDelegates()
    {
        Console.Write("Provide mathematical operator: ");
        string operationType = Console.ReadLine();
        MathematicalOperation mathematicalOperation = MathematicalOperationFactory(operationType);
        Console.Write("Provide first number: ");
        int a = Convert.ToInt32(Console.ReadLine());
        Console.Write("Provide second number: ");
        int b = Convert.ToInt32(Console.ReadLine());
        int result = mathematicalOperation(a, b);
        Console.WriteLine($"{a} {operationType} {b} = {result}");
    }

    public static void Main(string[] args)
    {
        WorkingWithDelegates();
    }
}
