namespace CarRace;

public class RandomHelper
{
    private static readonly Random _random = new();

    private RandomHelper()
    {
    }

    public static int NextInt(int upper)
    {
        return _random.Next(upper);
    }

    public static string ChooseOne(string[] possibilities)
    {
        if (possibilities != null && possibilities.Length >= 1)
            return possibilities[_random.Next(possibilities.Length)];

        throw new ArgumentException("Possibilities should be a non-empty array of strings.");
    }

    public static int NextInt(int lower, int upper)
    {
        return _random.Next(lower, upper);
    }

    public static bool EventWithChance(int chance)
    {
        return _random.Next(100) < chance;
    }
}