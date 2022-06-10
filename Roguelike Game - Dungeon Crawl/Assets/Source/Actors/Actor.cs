using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using UnityEngine;

namespace DungeonCrawl.Actors
{
    public abstract class Actor : MonoBehaviour
    {
        public (int x, int y) Position
        {
            get => _position;
            set
            {
                _position = value;
                transform.position = new Vector3(value.x, value.y, Z);
            }
        }

        private (int x, int y) _position;
        private SpriteRenderer _spriteRenderer;

        private void Awake()
        {
            _spriteRenderer = GetComponent<SpriteRenderer>();

            SetSprite(DefaultSpriteId);
        }

        private void Update()
        {
            OnUpdate(Time.deltaTime);
        }

        public void SetSprite(int id)
        {
            _spriteRenderer.sprite = ActorManager.Singleton.GetSprite(id);
        }
        
        public void PlayerTryMove(Direction direction)
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
                if (actorAtTargetPosition is Character character && this is Player OurPlayer){OurPlayer.Fight(character);}
            }
            else if (actorAtTargetPosition.Pickable)
            {
                if (actorAtTargetPosition is Item item && this is Player OurPlayer){OurPlayer.AddToInventory(item);}
                Position = targetPosition;
            }
            else
            {
                if (actorAtTargetPosition.OnCollision(this))
                {
                    // Allowed to move
                    Position = targetPosition;
                }
            }
        }

        public void GhostTryMove(Direction direction)
        {
            var vector = direction.ToVector();
            (int x, int y) targetPosition = (Position.x + vector.x, Position.y + vector.y);
            var actorAtTargetPosition = ActorManager.Singleton.GetActorAt(targetPosition);
            if (actorAtTargetPosition == null)
            {
                // No obstacle found, just move
                Position = targetPosition;
            }
        }

        public void BoneTryMove(Direction direction)
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
                if (actorAtTargetPosition is Player player && this is Golem golem){golem.Fight(player);}
            }
            else ActorManager.Singleton.DestroyActor(this);
        }

        /// <summary>
        ///     Invoked whenever another actor attempts to walk on the same position
        ///     this actor is placed.
        /// </summary>
        /// <param name="anotherActor"></param>
        /// <returns>true if actor can walk on this position, false if not</returns>
        public virtual bool OnCollision(Actor anotherActor)
        {
            // All actors are passable by default
            return true;
        }

        /// <summary>
        ///     Invoked every animation frame, can be used for movement, character logic, etc
        /// </summary>
        /// <param name="deltaTime">Time (in seconds) since the last animation frame</param>
        protected virtual void OnUpdate(float deltaTime)
        {

        }

        /// <summary>
        ///     Can this actor be detected with ActorManager.GetActorAt()? Should be false for purely cosmetic actors
        /// </summary>
        public virtual bool Detectable => true;

        /// <summary>
        ///     Z position of this Actor (0 by default)
        /// </summary>
        public virtual bool FightMode => false;

        public virtual bool Pickable => false;
        
        public virtual int Z => 0;

        /// <summary>
        ///     Id of the default sprite of this actor type
        /// </summary>
        public abstract int DefaultSpriteId { get; }

        /// <summary>
        ///     Default name assigned to this actor type
        /// </summary>
        public abstract string DefaultName { get; }
    }
}
