using System.IO;

namespace Codecool.LeagueStatistics.Facotry
{
    /// <summary>
    ///     Provides random names for Players and Teams
    /// </summary>
    public static class NamesGenerator
    {
        public static string pathPlayerNames = @"C:\Users\Patryk\Codecool\OOP - C#\Week Pair 4\league-statistics-csharp-PatrykCzaniecki\data\PlayerNames.txt";
        public static string pathCityNames = @"C:\Users\Patryk\Codecool\OOP - C#\Week Pair 4\league-statistics-csharp-PatrykCzaniecki\data\CityNames.txt";
        public static string pathTeamNames = @"C:\Users\Patryk\Codecool\OOP - C#\Week Pair 4\league-statistics-csharp-PatrykCzaniecki\data\TeamNames.txt";
        public static string GetPlayerName()
        {
            return File.ReadAllLines(pathPlayerNames).GetRandomValue();
        }

        public static string GetTeamName()
        {
            var cities = File.ReadAllLines(pathCityNames);
            var names = File.ReadAllLines(pathTeamNames);

            return cities.GetRandomValue() + " " + names.GetRandomValue();
        }
    }
}
