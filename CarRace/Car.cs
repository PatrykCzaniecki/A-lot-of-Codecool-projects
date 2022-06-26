namespace CarRace;

public class Car : Vehicle
{
    private static readonly int YellowFlagSpeed = 75;

    private static readonly string[] PossibleNames =
    {
        "Epiphany",
        "Parallel",
        "Blitz",
        "Eos",
        "Evolution",
        "Wolf",
        "Union",
        "Empyrean",
        "Curiosity",
        "Gallop"
    };

    public Car() : base(NormalSpeed())
    {
    }

    protected override string GenerateName()
    {
        return $"{RandomName()} {RandomName()}";
    }

    private string RandomName()
    {
        return RandomHelper.ChooseOne(PossibleNames);
    }

    private static int NormalSpeed()
    {
        return RandomHelper.NextInt(80, 110 + 1);
    }

    public override void PrepareForLap(Race race)
    {
        if (race.IsThereABrokenTruck)
            ActualSpeed = YellowFlagSpeed;
        else
            ActualSpeed = NormalSpeed();
    }
}