namespace DesignPatternsInfo; 

internal class Person
{
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }

    public string Name { get; set; }

    public int Age { get; set; }

    public void SayHi()
    {
        Console.WriteLine($"Hello, my name is {Name}");
    }
}