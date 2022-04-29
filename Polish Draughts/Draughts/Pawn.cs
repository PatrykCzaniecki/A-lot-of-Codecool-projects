namespace Draughts
{
    public class Pawn
    {
        public char Color { get; set; }
        public  (int x, int y) Coordinates { get; set; }
        public bool IsCrowned { get; set; }

        public Pawn(char color, int x, int y)
        {
            Color = color;
            Coordinates = (x, y);
            IsCrowned = false;
        }

        public void CoordinatesPawn(int row, int col)
        {
            Coordinates = (row, col);
        }

        public char GetColor()
        {
            return Color;
        }
        public void Crowned(bool crown)
        {
            IsCrowned = crown;
        }
    }
}