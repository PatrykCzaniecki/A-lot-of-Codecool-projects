namespace DentalClinic;

public class Hygienist : DentalStuff
{
    public Hygienist(string name, string specialization) : base(name, specialization)
    {
    }

    public override string ToString()
    {
        return $"I am Name: {Name}, Specialization: {Specialization}";
    }
}