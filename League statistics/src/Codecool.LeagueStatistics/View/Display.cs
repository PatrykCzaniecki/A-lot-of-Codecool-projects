using Codecool.LeagueStatistics.Model;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Codecool.LeagueStatistics.View
{
    /// <summary>
    /// Provides console view for league table, results and all League statistics
    /// </summary>
    public static class Display
    {
        public static void DisplayLeagueResults(List<Team> league)
        {
            Console.WriteLine(String.Format("|{0,5}|{1,5}|{2,5}|{3,5}|{4,5}|{5,5}", "Team Name", "Points", "Goals", "Wins", "Draws", "Losses"));
            foreach (var team in league)
            {
                Console.WriteLine(String.Format("|{0,5}|{1,5}|{2,5}|{3,5}|{4,5}|{5,5}", team.Name,
                    team.CurrentPoints, team.Players.Sum(player => player.Goals), team.Wins, team.Draws, team.Losts));
            }
        }
    }
}
