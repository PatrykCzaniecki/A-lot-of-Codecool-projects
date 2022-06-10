using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Items;
using UnityEngine;

public class Armor : Item
{
    public override bool OnCollision(Actor anotherActor)
    {
        return true;
    }
    public override int DefaultSpriteId => 181;
    public override string DefaultName => "Armor";
    public override bool Detectable => true;
    public override bool Pickable => true;
    public int Shield => 10;
}
