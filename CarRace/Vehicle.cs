using System.Text;

namespace CarRace;

public abstract class Vehicle
{
    protected Vehicle(int normalSpeed)
    {
        Name = GenerateName();
        NormalSpeed = normalSpeed;
    }

    protected string Name { get; }

    protected int NormalSpeed { get; }

    protected int ActualSpeed { get; set; }

    public int DistanceTraveled { get; set; }

    public abstract void PrepareForLap(Race race);

    protected abstract string GenerateName();

    public void MoveForAnHour()
    {
        DistanceTraveled += ActualSpeed * 1;
    }

    public override string ToString()
    {
        var sb = new StringBuilder()
            .Append("{type: ")
            .Append(GetType().Name)
            .Append(", ")
            .Append("name: ")
            .Append(Name)
            .Append(", ")
            .Append("distance travelled: ")
            .Append(DistanceTraveled)
            .Append("}");
        return sb.ToString();
    }
}