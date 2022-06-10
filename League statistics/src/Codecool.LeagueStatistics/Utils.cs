using System;
using System.Collections.Generic;
using System.Linq;

namespace Codecool.LeagueStatistics
{
    public enum Division
    {
        East,
        Central,
        West
    }

    /// <summary>
    /// Provides repetetive methods or data.
    /// </summary>
    public static class Utils
    {
        public static readonly Random Random = new Random();

        public const int TeamSize = 11;

        /// <summary>
        ///     Gets a random item from any IEnumerable
        /// </summary>
        public static T GetRandomValue<T>(this IEnumerable<T> enumerable)
        {
            var array = enumerable as T[] ?? enumerable.ToArray();
            var index = Random.Next(0, array.Length);

            return array[index];
        }
    }
}
