using System.Collections.Generic;

namespace DungeonCrawl.Repository
{
    public class InventoryToTransfer
    {
        public Dictionary<string, int> Inventory { get; set; }

        public InventoryToTransfer(Dictionary<string, int> inventory)
        {
            Inventory = inventory;
        }
    }
}
