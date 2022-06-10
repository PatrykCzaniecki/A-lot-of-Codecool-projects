using DungeonCrawl.Actors;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Core;
using UnityEngine;

public class Door : Actor
{
    public override bool OnCollision(Actor anotherActor)
    {
        if (anotherActor is Player player)
        {
            if (player.Inventory.ContainsKey("key") && MapLoader.MapId==1)
            {
                SetSprite(341);
                return true;
            }
            if (player.Inventory.ContainsKey("Silver Key") && MapLoader.MapId==2)
            {
                SetSprite(341);
                return true;
            }
        }
        return false;
    }

    public override int DefaultSpriteId => 340;
    public override string DefaultName => "Door";
    public override bool Detectable => true;
}
