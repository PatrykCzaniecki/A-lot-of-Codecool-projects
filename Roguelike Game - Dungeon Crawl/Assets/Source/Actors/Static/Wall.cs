namespace DungeonCrawl.Actors.Static
{
    public class Wall : Actor
    {
        public override int DefaultSpriteId => 825;
        public override string DefaultName => "Wall";
        public override bool OnCollision(Actor anotherActor)
        {
            return false;
        }
    }
}
