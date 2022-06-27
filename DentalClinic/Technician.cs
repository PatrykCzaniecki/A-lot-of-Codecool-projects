namespace DentalClinic;

public class Technician : DentalStuff
{
    public Technician(string name, string specialization) : base(name, specialization)
    {
    }

    public override string ToString()
    {
        return $"I am Name: {Name}, Specialization: {Specialization}";
    }
}