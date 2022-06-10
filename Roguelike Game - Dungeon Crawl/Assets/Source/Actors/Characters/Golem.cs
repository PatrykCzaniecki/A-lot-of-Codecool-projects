using DungeonCrawl.Core;
using UnityEngine;
using Random = System.Random;

namespace DungeonCrawl.Actors.Characters
{
    public class Golem : Character
    {
        public int MapId = 1;
        private int moveCount = 0;
        Random random = new Random();
        
        public Golem()
        {
            Health = 50;
            Damage = 15;
            Shield = 5;
        }
        
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        
        public override bool FightMode => true;
        protected override void OnDeath()
        {
            Debug.Log("Well, I was already dead anyway...");
            var player = ActorManager.Singleton.FindPlayer();
            player.Position = (65, -21);
            Debug.Log(player.DefaultName);
            MapLoader.MapId = 2;
            MapLoader.LoadMap();
            ActorManager.Singleton._allActors.Add(player);
        }
        
        public void GolemTryMove(Direction direction)
        {
            var vector = direction.ToVector();
            (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
            var actorAtTargetPosition = ActorManager.Singleton.GetActorAt(targetPosition);
            if (actorAtTargetPosition == null)
            {
                // No obstacle found, just move
                Position = targetPosition;
            }
            else if (actorAtTargetPosition.FightMode)
            {
                if (actorAtTargetPosition is Player player){Fight(player);}
            }
        }

        protected override void OnUpdate(float deltaTime)
        {
            var player = ActorManager.Singleton.FindPlayer();
            int golemX = Position.x;
            int golemY = Position.y;
            int playerX = player.Position.x;
            int playerY = player.Position.y;
            Direction direction = Direction.Up;
            moveCount++;
            if (moveCount == 240 && playerX > 15) 
            {
                if (golemY > playerY)
                {
                    var vector = direction.ToVector();
                    (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
                    direction = Direction.Down;
                    if (targetPosition.x <= 19 && playerY < golemY)
                    {
                        direction = Direction.Left;
                    }
                    if (targetPosition.x <= 19  && playerY < golemY)
                    {
                        direction = Direction.Right;
                    }
                }
                else if (golemY < playerY)
                {
                    var vector = direction.ToVector();
                    (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
                    direction = Direction.Up;
                    if (targetPosition.x > 21)
                    {
                        direction = Direction.Left;
                    }
                    if (targetPosition.x < 21)
                    {
                        direction = Direction.Right;
                    }
                }
                else if (golemX > playerX)
                {
                    direction = Direction.Left;
                }
                else if (golemX < playerX)
                {
                    direction = Direction.Right;
                }
                moveCount = 0;
                GolemTryMove(direction);
            }
            else if (moveCount == 240)
            {
                moveCount = 0;
            }
        }
        
        public override int DefaultSpriteId => 317;
        public override string DefaultName => "Golem";
    }
}
