using System;
using System.Collections.Generic;
using Codecool.LeagueStatistics.Factory;
using Codecool.LeagueStatistics.Model;
using Codecool.LeagueStatistics.View;

namespace Codecool.LeagueStatistics.Controllers
{
    /// <summary>
    ///     Provides all necessary methods for season simulation
    /// </summary>
    public class Season
    {
        public List<Team> League { get; set; }

        public Season()
        {
            League = new List<Team>();
        }

        /// <summary>
        ///     Fills league with new teams and simulates all games in season.
        /// After all games played calls table to be displayed.
        /// </summary>
        public void Run()
        {
            var league = LeagueFactory.CreateLeague(6);
            foreach (var team in league)
            {
                League.Add(team);
            }
            PlayAllGames();

            Display.DisplayLeagueResults(League);
        }
        /// <summary>
        ///     Playing one round. Everyone with everyone one time. 
        /// </summary>
        public void PlayAllGames()
        {
            foreach (var team in League)
            {
                foreach (var opponent in League)
                {
                    if (team != opponent)
                    {
                        PlayMatch(team, opponent);
                    }
                }
            }
        }
        /// <summary>
        ///     Plays single game between two teams and displays result after.
        /// </summary>
        public void PlayMatch(Team team1, Team team2)
        {
            int teamOneGoals = ScoredGoals(team1);
            int teamTwoGoals = ScoredGoals(team2);

            if (teamOneGoals > teamTwoGoals)
            {
                team1.Wins++;
                team2.Losts++;
            }else if (teamTwoGoals > teamOneGoals)
            {
                team2.Wins++;
                team1.Losts++;
            }else if (teamOneGoals == teamTwoGoals)
            {
                team1.Draws++;
                team2.Draws++;
            }
        }

        /// <summary>
        ///     Checks for each player of given team chanse to score based on skillrate.
        ///     Adds scored golas to player's and team's statistics.
        /// </summary>
        /// <param name="team">team</param>
        /// <returns>All goals scored by the team in current game</returns>
        public int ScoredGoals(Team team)
        {
            int goalsScoredInCurrentGame = 0;

            foreach (var player in team.Players)
            {
                if (player.SkillRate > Utils.Random.Next(player.SkillRate + 1))
                {
                    player.Goals++;
                    goalsScoredInCurrentGame++;
                }
            }
            return goalsScoredInCurrentGame;
        }
    }
}
