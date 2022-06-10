using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Items;
using UnityEngine;

public class Sword : Item 
{ 
    public override bool OnCollision(Actor anotherActor)
    {
        return true;
    }
    public override int DefaultSpriteId => 369;
    public override string DefaultName => "Sword";
    public override bool Detectable => true;
    public override bool Pickable => true;
    public int damage = 5;
}
