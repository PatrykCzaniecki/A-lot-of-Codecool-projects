using System;

namespace Codecool.LifeOfAnts.Geometry
{
    public static class DirectionExtensions
    {
        public static Direction GetRandomDirection()
        {
            Array values = Enum.GetValues(typeof(Direction));
            Direction randomDirection = (Direction)values.GetValue(new Random().Next(values.Length));

            return randomDirection;
        }
    }
}
