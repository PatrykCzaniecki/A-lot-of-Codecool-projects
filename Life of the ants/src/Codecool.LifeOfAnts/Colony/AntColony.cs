using System;
using System.Collections.Generic;
using System.Linq;
using Codecool.LifeOfAnts.Ants;

namespace Codecool.LifeOfAnts.Colony
{
    public class AntColony
    {
        public AntColony(int width)
        {
            _width = width;
            _height = _width;
            _allAnts = new List<Ant>();
            _theQueen = new Queen(new Position(_width / 2, _width / 2));
        }

        public List<Drone> DronesList { get; set; }

        private Random _randomNumber = new Random();
        private Dictionary<Position, List<Ant>> _colonyMap;
        private int _width;
        private int _height;
        private List<Ant> _allAnts;
        private Queen _theQueen;

        public void CreateEmptyColony()
        {
            _colonyMap = new Dictionary<Position, List<Ant>>();

            for (int x = 0; x < _width; x++)
            {
                for (int y = 0; y < _height; y++)
                {
                    _colonyMap[new Position(x, y)] = new List<Ant>();
                }
            }
        }
        
        public void UpdateColony()
        {
            foreach (var ant in _allAnts)
            {
                ant.MakeMove();
                _colonyMap[ant.GetPosition()].Add(ant);
            }
        }

        public void PrintColony()
        {
            string verticalEdge = String.Concat(Enumerable.Repeat("~", 2 * _width));
            string antColonyBoard = "+" + verticalEdge + "+\n";

            for (int x = 0; x < _width; x++)
            {
                string printedRow = string.Empty;

                for (int y = 0; y < _height; y++)
                {
                    Position position = new Position(x, y);

                    if (_colonyMap[position].Count() != 0)
                    {
                        printedRow += _colonyMap[position][0].ToString() + " ";
                    }
                    else
                    {
                        printedRow += "  ";
                    }
                }
                antColonyBoard += "|" + printedRow + "|" + "\n";
            }
            antColonyBoard += "+" + verticalEdge + "+\n";
            Console.WriteLine(antColonyBoard);
        }

        public void UpdateAndPrintColony()
        {
            CreateEmptyColony();
            UpdateColony();
            PrintColony();
        }

        public Position ValidStartingDroneAntCoordinates()
        {
            var startingDronePosition = RandomPointInColony();

            while (startingDronePosition.DistanceToCoordinate(_theQueen.GetPosition()) < _width / 2)
            {
                startingDronePosition = RandomPointInColony();
            }
            return startingDronePosition;
        }

        public Position RandomPointInColony()
        {
            int xcoordinate = Math.Abs(_randomNumber.Next(0, _width - 1));
            int ycoordinate = Math.Abs(_randomNumber.Next(0, _width - 1));

            return new Position(xcoordinate, ycoordinate);
        }

        public int GetWidth()
        {
            return _width;
        }

        public Queen GetTheQueen()
        {
            return _theQueen;
        }

        public void GenerateAnts(int workers, int soldiers, int drones)
        {
            for (int w = 0; w < workers; w++)
            {
                _allAnts.Add(new Worker(RandomPointInColony()));
            }

            for (int s = 0; s < soldiers; s++)
            {
                _allAnts.Add(new Soldier(RandomPointInColony()));
            }

            for (int d = 0; d < drones; d++)
            {
                _allAnts.Add(new Drone(ValidStartingDroneAntCoordinates()));
            }

            _allAnts.Add(_theQueen);

            foreach (var ant in _allAnts)
            {
                _colonyMap[ant.GetPosition()].Add(ant);
                ant.AntColony = this;
            }
        }
    }
}
