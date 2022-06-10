using Codecool.LeagueStatistics.Facotry;

namespace Codecool.LeagueStatistics.Model
{
    /// <summary>
    ///     Represents player
    /// </summary>
    public class Player
    {
        /// <summary>
        ///     Player's name
        /// </summary>
        public string Name { get; set; }

        /// <summary>
        ///     SkillRate is a percentage chance to score a goal
        /// </summary>
        public int SkillRate { get; set; }

        /// <summary>
        ///     Amount of scored goals
        /// </summary>
        public int Goals { get; set; }

        public Player(int skillrate)
        {
            Name = NamesGenerator.GetPlayerName();
            SkillRate = skillrate;
        }

        public Player()
        {
        }
    }
}
