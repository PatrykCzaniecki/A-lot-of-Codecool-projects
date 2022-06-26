namespace CarRace;

public class Race
{
    private const int NumberOfLaps = 50;

    private readonly Weather _weather = new();

    public List<Vehicle> listOfRacers = new();

    public bool IsRaining => _weather.IsRaining;

    public bool IsThereABrokenTruck { get; private set; }

    public void SimulateRace()
    {
        for (var i = 0; i < NumberOfLaps; i++)
        {
            foreach (var racer in listOfRacers)
            {
                racer.PrepareForLap(this);
                racer.MoveForAnHour();
            }

            _weather.RandomWeather();
            IsThereABrokenTruck = GetBrokenTruckStatus();
        }
    }

    public void RegisterRacer(Vehicle racer)
    {
        listOfRacers.Add(racer);
    }

    private bool GetBrokenTruckStatus()
    {
        foreach (var racer in listOfRacers)
            if (racer is Truck)
            {
                var truck = (Truck) racer;
                if (truck.TruckIsBroken) return true;
            }

        return false;
    }

    public void PrintRaceResult()
    {
        Console.WriteLine("Race results");
        foreach (var racer in listOfRacers.OrderByDescending(racer => racer.DistanceTraveled)) Console.WriteLine(racer);
    }
}