namespace DungeonCrawl.Repository
{
    public class PlayerToTransfer
    {
        public string Name { get; set; }
        public int Health { get; set; }
        public int Damage { get; set; }
        public int Shield { get; set; }
        public int X { get; set; }
        public int Y { get; set; }

        public PlayerToTransfer(string name, int health, int damage, int shield, (int x, int y) position)
        {
            Name = name;
            Health = health;
            Damage = damage;
            Shield = shield;
            X = position.x;
            Y = position.y;
        }
    }
}
