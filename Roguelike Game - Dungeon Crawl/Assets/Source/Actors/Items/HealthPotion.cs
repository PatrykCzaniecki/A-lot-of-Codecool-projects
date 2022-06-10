namespace DungeonCrawl.Actors.Items
{
    public class HealthPotion : Item
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 528;
        public override string DefaultName => "Potion of greater healing";
        public override bool Detectable => true;
        public override bool Pickable => true;

        public int Health => 200;
    }
}
