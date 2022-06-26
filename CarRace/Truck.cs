namespace CarRace;

public class Truck : Vehicle
{
    private const int NormalSpeed = 100;

    private const int SpeedWhenBrokeDown = 0;

    private const int ChanceToBrokeDown = 5;

    private const int TurnsToRepair = 2;

    private int LeftTurnsToRepair;
    private State state = State.not_broken;

    public Truck() : base(NormalSpeed)
    {
    }

    public bool TruckIsBroken => state != State.not_broken;

    public override void PrepareForLap(Race race)
    {
        if (TruckIsBroken)
            ActualSpeed = SpeedWhenBrokeDown;
        else
            ActualSpeed = NormalSpeed;

        state = NextState();
    }

    private State NextState()
    {
        switch (state)
        {
            case State.not_broken:
                if (RandomHelper.EventWithChance(ChanceToBrokeDown))
                {
                    LeftTurnsToRepair = TurnsToRepair;
                    return State.broken;
                }

                break;
            case State.broken:
                if (LeftTurnsToRepair-- > 0) return State.broken;
                break;
        }

        return State.not_broken;
    }

    protected override string GenerateName()
    {
        return RandomHelper.NextInt(0, 1000 + 1).ToString();
    }

    private enum State
    {
        not_broken,
        broken
    }
}