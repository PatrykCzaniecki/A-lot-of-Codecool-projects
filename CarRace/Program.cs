namespace CarRace;

public class Program
{
    public static void Main(string[] args)
    {
        var race = new Race();
        SetUpRace(race);

        race.SimulateRace();
        race.PrintRaceResult();
    }

    private static void SetUpRace(Race race)
    {
        for (var i = 0; i < 10; i++)
        {
            race.RegisterRacer(new Car());
            race.RegisterRacer(new Motorcycle());
            race.RegisterRacer(new Truck());
        }
    }
}