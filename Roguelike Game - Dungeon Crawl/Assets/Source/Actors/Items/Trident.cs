using System;
using UnityEngine;

namespace DungeonCrawl.Actors.Items
{
    public class Trident : Item
    {
        public override bool OnCollision(Actor anotherActor)
        {
            return true;
        }
        public override int DefaultSpriteId => 271;
        public override string DefaultName => "The Trident of Death";
        public override bool Detectable => true;
        public override bool Pickable => true;

        protected void OnDestroy()
        {
            Debug.Log("You obtained legendary Triden of Death");
        }

        public int damage = 100;
    }
}
