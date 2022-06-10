using System;

namespace DungeonCrawl.Actors.Static
{
    public class Grass : Actor
    {
        private Random _random = new Random();
        public override int DefaultSpriteId => 101;
        public override string DefaultName => "Grass";
        public override bool Detectable => false;
    }
}
