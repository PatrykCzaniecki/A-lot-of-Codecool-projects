namespace DentalClinic;

public abstract class DentalStuff
{
    protected DentalStuff(string name, string specialization)
    {
        Name = name;
        Specialization = specialization;
    }

    protected string Name { get; set; }

    protected string Specialization { get; set; }

    public override string ToString()
    {
        return $"Dental Stuff {Name} and {Specialization}";
    }
}