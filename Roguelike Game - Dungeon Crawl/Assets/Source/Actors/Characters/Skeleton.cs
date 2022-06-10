using DungeonCrawl.Core;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public class Skeleton : Character
    {
        public Skeleton()
            {
                Health = 10;
                Damage = 5;
                Shield = 0;
            }
        private int _move = 0;

        protected override void OnUpdate(float deltaTime)
        {
            var goDownY = Position.y - 1;
            _move++;
            if (_move == 1500)
            {
                _move = 0;
                MapLoader.SpawnBone((Position.x, goDownY));
            }
        }

        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        
        public override bool FightMode => true;
        public override int DefaultSpriteId => 316;
        public override string DefaultName => "Skeleton";
        protected override void OnDeath()
        {
            Debug.Log("Well, I was already dead anyway...");
        }
    }
}
