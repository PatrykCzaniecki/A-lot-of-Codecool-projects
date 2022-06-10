namespace DungeonCrawl.Actors.Items
{
    public class Ring : Item
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 332;
        public override string DefaultName => "Ring of Life";
        public override bool Detectable => true;
        public override bool Pickable => true;
        public int Health => 30;
    }
}
