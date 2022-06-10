using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Items;
using UnityEngine;

public class Key : Item
{
    public override bool OnCollision(Actor anotherActor)
    {
        return true;
    }
    public override int DefaultSpriteId => 559;
    public override string DefaultName => "Key";
    public override bool Detectable => true;
    public override bool Pickable => true;
}
