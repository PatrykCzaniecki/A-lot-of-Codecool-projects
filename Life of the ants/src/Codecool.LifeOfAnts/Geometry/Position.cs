using System;

namespace Codecool.LifeOfAnts
{
    public struct Position
    {
        public Position(int x, int y)
        {
            X = x;
            Y = y;
        }

        public int X { get; set; }
        
        public int Y { get; set; }

        public int DistanceToCoordinate(Position other)
        {
            return Math.Abs(other.X - X) + Math.Abs(other.Y - Y);
        }

        public Position NextCoordinatesInDirection(Direction direction)
        {
            Position nextCoordinate = new Position(X, Y);
            switch (direction)
            {
                case Direction.North:
                    nextCoordinate = new Position(X, Y + 1);
                    break;
                case Direction.South:
                    nextCoordinate = new Position(X, Y - 1);
                    break;
                case Direction.East:
                    nextCoordinate = new Position(X + 1, Y);
                    break;
                case Direction.West:
                    nextCoordinate = new Position(X - 1, Y);
                    break;
            }
            return nextCoordinate;
        }
    }
}
