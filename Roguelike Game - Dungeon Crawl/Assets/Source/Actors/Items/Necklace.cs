namespace DungeonCrawl.Actors.Items
{
    public class Necklace : Item
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 379;
        public override string DefaultName => "Magic Necklace";
        public override bool Detectable => true;
        public override bool Pickable => true;
        public int Shield => 20;
    }
}
