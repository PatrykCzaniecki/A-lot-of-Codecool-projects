using System;
using DungeonCrawl.Core;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public abstract class Character : Actor
    {
        public int Health { get; set; }
        public int Damage { get; set; }
        public int Shield { get; set; }

        public void ApplyDamage(int damage)
        {
            damage -= Shield;
            if (damage > 0)
            {
                Health -= damage;
            }

            if (Health > 0) return;
            // Die
            OnDeath();
            ActorManager.Singleton.DestroyActor(this);
        }

        public void Fight(Character opponent)
        {
            Debug.Log("FIGHT START");
            opponent.ApplyDamage(Damage);
            ApplyDamage(opponent.Damage);
        }
        
        protected abstract void OnDeath();
        /// <summary>
        ///     All characters are drawn "above" floor etc
        /// </summary>
        public override int Z => -1;
    }
}
