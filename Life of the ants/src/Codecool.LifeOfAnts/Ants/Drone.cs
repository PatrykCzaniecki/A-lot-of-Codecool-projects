using System;
using System.Collections.Generic;
using Codecool.LifeOfAnts.Geometry;

namespace Codecool.LifeOfAnts.Ants
{
    public class Drone : Ant
    {
        public Drone(Position position)
        {
            Symbol = 'D';
            Coordinates = position;
            _matingCountdown = 0;
            _isMating = false;
        }
        
        private int _matingCountdown;
        private bool _isMating;
        private int _timeSteps = 11;
        
        public override Position GetPosition()
        {
            return Coordinates;
        }

        public override char GetSymbol()
        {
            return Symbol;
        }

        public override string ToString()
        {
            return Symbol.ToString();
        }

        public Position MoveTowardsQueen()
        {
            var nextPosition = Coordinates.NextCoordinatesInDirection(DirectionExtensions.GetRandomDirection());
            var queenPosition = AntColony.GetTheQueen().GetPosition();

            while (nextPosition.DistanceToCoordinate(queenPosition) > Coordinates.DistanceToCoordinate(queenPosition))
            {
                nextPosition = Coordinates.NextCoordinatesInDirection(DirectionExtensions.GetRandomDirection());
            }
            Coordinates = nextPosition;
            return Coordinates;
        }

        public bool ReachedQueen()
        {
            var queenPosition = AntColony.GetTheQueen().GetPosition();
            if (Coordinates.DistanceToCoordinate(queenPosition) == 0)
            {
                return true;
            }
            return false;
        }

        public void TryMating()
        {
            if (AntColony.GetTheQueen().IsInGoodMood())
            {
                Console.WriteLine("Drone says: HALLELUJAH");
                _isMating = true;
            }
            else if (!AntColony.GetTheQueen().IsInGoodMood() && !_isMating)
            {
                Console.WriteLine("Drone says: :(\n");
                Coordinates = GetPositionAfterKickout();
            }
        }

        public Position GetPositionAfterKickout()
        {
            var kickOutPositions = new List<Position>();

            for (int x = 0; x < AntColony.GetWidth(); x++)
            {
                kickOutPositions.Add(new Position(x, 0));
                kickOutPositions.Add(new Position(x, AntColony.GetWidth() - 1));
                kickOutPositions.Add(new Position(0, x));
                kickOutPositions.Add(new Position(AntColony.GetWidth() - 1, x));
            }
            return kickOutPositions[new Random().Next(kickOutPositions.Count)];
        }

        public bool GetIsMating()
        {
            return _isMating;
        }

        public int GetMatingCountdown()
        {
            return _matingCountdown;
        }

        public void ContinueMating()
        {
            _matingCountdown += 1;
        }

        public void ResetPosition()
        {
            Coordinates = GetPositionAfterKickout();
            _matingCountdown = 0;
        }

        public override void MakeMove()
        {
            if (ReachedQueen())
            {
                TryMating();
                if (_isMating)
                {
                    ContinueMating();

                    if (_matingCountdown <= 10)
                    {
                        _timeSteps -= 1;
                        Console.WriteLine("Drone is mating with the Queen for another " + _timeSteps + " time steps\n");
                    }
                    else if (_matingCountdown > 10)
                    {
                        _isMating = false;
                        ResetPosition();
                        _timeSteps = 11;
                    }
                }
                else if (!_isMating)
                {
                    ResetPosition();
                }
            }
            else
            {
                MoveTowardsQueen();
            }
        }
    }
}
