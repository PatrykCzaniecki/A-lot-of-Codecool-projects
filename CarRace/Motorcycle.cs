namespace CarRace;

public class Motorcycle : Vehicle
{
    private const int NormalSpeed = 100;

    private int NumberOfMotorcycle = 1;

    public Motorcycle() : base(NormalSpeed)
    {
    }

    private static int SpeedInRain()
    {
        return RandomHelper.NextInt(5, 50 + 1);
    }

    public override void PrepareForLap(Race race)
    {
        if (race.IsRaining)
            ActualSpeed = NormalSpeed - SpeedInRain();
        else
            ActualSpeed = NormalSpeed;
    }

    protected override string GenerateName()
    {
        return "Motorcycle " + NumberOfMotorcycle++;
    }
}