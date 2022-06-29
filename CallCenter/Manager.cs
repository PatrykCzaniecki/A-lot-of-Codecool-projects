namespace CallCenter;

public class Manager : Employee
{
    public Manager(int id, string name) : base(id, name)
    {
    }

    public override string ToString()
    {
        return $"Manager: {Id}, {Name}";
    }
}