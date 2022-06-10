using DungeonCrawl.Core;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public class Bone : Character
    {
        private int _moveCount = 0;

        public Bone()
        {
            Health = 1;
            Damage = 3;
            Shield = 0;
        }
        
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        
        public override bool FightMode => true;

        protected override void OnDeath()
        {
            /*Debug.Log("Well, I was already dead anyway...");*/
        }

        protected override void OnUpdate(float deltaTime)
        {
            _moveCount++;
            var player = ActorManager.Singleton.FindPlayer();
            var boneX = Position.x;
            var boneY = Position.y;
            var playerX = player.Position.x;
            var playerY = player.Position.y;
            var direction = Direction.Up;
            if (_moveCount == 360 && playerX > 15 && Position.x > 15)
            {
                if (boneY > playerY)
                {
                    var vector = direction.ToVector();
                    (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
                    direction = Direction.Down;
                    if (targetPosition.x <= 19 && playerY < boneY) direction = Direction.Left;
                    if (targetPosition.x <= 19 && playerY < boneY) direction = Direction.Right;
                }
                else if (boneY < playerY)
                {
                    var vector = direction.ToVector();
                    (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
                    direction = Direction.Up;
                    if (targetPosition.x > 21) direction = Direction.Left;
                    if (targetPosition.x < 21) direction = Direction.Right;
                }
                else if (boneX > playerX)
                {
                    direction = Direction.Left;
                }
                else if (boneX < playerX)
                {
                    direction = Direction.Right;
                }
                _moveCount = 0;
                BoneTryMove(direction);
            }
            else if (_moveCount == 360)
            {
                direction = Direction.Down;
                _moveCount = 0;
                BoneTryMove(direction);
            }
        }
        public override int DefaultSpriteId => 607;
        public override string DefaultName => "Bone";
    }
}
