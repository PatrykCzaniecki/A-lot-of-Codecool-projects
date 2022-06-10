using System;

namespace DungeonCrawl.Actors.Static
{
    public class Trees : Actor
    {
        private Random random = new Random();
        public override int DefaultSpriteId => random.Next(47,54);
        public override string DefaultName => "River";
        public override bool OnCollision(Actor anotherActor)
        {
            return false;
        }
    }
}
