namespace CarRace;

public class Weather
{
    private const int ChanceToRain = 30;

    public Weather()
    {
        RandomWeather();
    }

    public bool IsRaining { get; private set; }

    public void RandomWeather()
    {
        IsRaining = RandomHelper.EventWithChance(ChanceToRain);
    }
}