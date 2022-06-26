namespace Library;

public class CD : Item
{
    public CD(int id, string name, int numberOfTrucks) : base(id, name)
    {
        NumberOfTrucks = numberOfTrucks;
    }

    private int NumberOfTrucks { get; }

    public override string ToString()
    {
        return base.ToString() + $", NumberOfTrucks: {NumberOfTrucks}";
    }
}