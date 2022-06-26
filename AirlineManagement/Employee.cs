namespace AirlineManagement;

public abstract class Employee
{
    protected Employee(string name, DateOnly birthDate)
    {
        Name = name;
        BirthDate = birthDate;
    }

    protected string Name { get; set; }
    protected DateOnly BirthDate { get; set; }

    public override string ToString()
    {
        return $"{Name}";
    }
}