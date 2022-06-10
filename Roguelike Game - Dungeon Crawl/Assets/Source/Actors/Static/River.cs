using System;

namespace DungeonCrawl.Actors.Static
{
    public class River : Actor
    {
        private Random random = new Random();
        public override int DefaultSpriteId => 203;
        public override string DefaultName => "River";
        public override bool OnCollision(Actor anotherActor)
        {
            return false;
        }
    }
}
