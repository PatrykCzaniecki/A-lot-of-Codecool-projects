using System;
using System.ComponentModel.Design;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Runtime.CompilerServices;
using System.Windows;

namespace Draughts
{
    public class Game
    {
        public static void Main(string[] args)
        {
            Menu();
        }

        public static void Menu()
        {
            Console.WriteLine("Welcome Player");
            Console.WriteLine("What size of board u choose(10-20):");
            var size = Console.ReadLine();
            Round(Int32.Parse(size));
        }

        public static void Round(int size)
        {
            Board board = new Board(size);
            board.DisplayBoard();
            board.Move();
            board.DisplayBoard();
        }
    }
}