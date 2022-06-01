using Codecool.LeagueStatistics.Facotry;
using System;
using System.Collections.Generic;

namespace Codecool.LeagueStatistics.Model
{
    /// <summary>
    ///     Represents a team.
    /// </summary>
    public class Team
    {
        public string Name { get; set; }

        /// <summary>
        ///     Division is a geografic representation of team.
        /// </summary>
        public Division Division { get; set; }

        public int Wins { get; set; }
        public int Draws { get; set; }
        public int Losts { get; set; }

        public IEnumerable<Player> Players { get; set; }

        /// <summary>
        /// CurrentPoints is a sum of wins and draws points. For each win 3 points, for draw 1 point.
        /// </summary>
        public int CurrentPoints => (Wins * 3) + Draws;

        public Team(Division division, IEnumerable<Player> players)
        {
            Name = NamesGenerator.GetTeamName();
            Division = division;
            Players = players;
        }

        public Team()
        {
        }
    }
}
