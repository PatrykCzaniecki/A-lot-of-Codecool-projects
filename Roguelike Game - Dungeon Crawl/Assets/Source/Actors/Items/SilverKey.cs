namespace DungeonCrawl.Actors.Items
{
    public class SilverKey : Item
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 560;
        public override string DefaultName => "Silver Key";
        public override bool Detectable => true;
        public override bool Pickable => true;
    }
}
