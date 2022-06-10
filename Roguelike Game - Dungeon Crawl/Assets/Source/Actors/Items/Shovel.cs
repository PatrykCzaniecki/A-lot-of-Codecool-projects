namespace DungeonCrawl.Actors.Items
{
    public class Shovel : Item 
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 281;
        public override string DefaultName => "Shovel of The Gods ";
        public override bool Detectable => true;
        public override bool Pickable => true;
        public int damage = 20; 
    }
}
