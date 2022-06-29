namespace CallCenter;

public abstract class Employee
{
    protected Employee(int id, string name)
    {
        Id = id;
        Name = name;
    }

    protected int Id { get; set; }

    protected string Name { get; set; }

    public override string ToString()
    {
        return $"Employee: {Id}, Name: {Name}";
    }
}