using UnityEngine;
using Random = System.Random;

namespace DungeonCrawl.Actors.Characters
{
    public class Ghost : Character
    {
        private int moveCount = 0;
        Random random = new Random();

        public Ghost()
        {
            Health = 5;
            Damage = 10;
            Shield = 0;
        }

        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }

        public override bool FightMode => true;

        protected override void OnDeath()
        {
            Debug.Log("Well, I was already dead anyway...");
        }

        public override int DefaultSpriteId => 314;
        public override string DefaultName => "Ghost";

        protected override void OnUpdate(float deltaTime)
        {
            moveCount++;
            if (moveCount == 240)
            {
                int randomNum = random.Next(1, 5);
                Direction direction = Direction.Down;
                if (randomNum == 2)
                {
                    direction = Direction.Left;
                }
                else if (randomNum == 3)
                {
                    direction = Direction.Right;
                }
                else if (randomNum == 4)
                {
                    direction = Direction.Up;
                }
                GhostTryMove(direction);
                moveCount = 0;
            }
        }
    }
}
