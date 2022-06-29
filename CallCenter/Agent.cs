namespace CallCenter;

public class Agent : Employee
{
    public Agent(int id, string name, Seniority seniority) : base(id, name)
    {
        Seniority = seniority;
    }

    public Seniority Seniority { get; }

    public override string ToString()
    {
        return base.ToString() + $", Seniority {Seniority}";
    }
}