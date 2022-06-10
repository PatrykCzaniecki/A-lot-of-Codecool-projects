using System;
using System.IO;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Repository;
using Unity.Plastic.Newtonsoft.Json;
using Unity.Plastic.Newtonsoft.Json.Linq;
using UnityEngine;

namespace DungeonCrawl.Core
{
    public class JsonManager : MonoBehaviour
    {
        public static JsonManager Singleton { get; private set; }
        
        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }
            Singleton = this;
        }

        string saveFile = Environment.CurrentDirectory + "/exported_saves/gamedata.json";
        
        public void SavePlayer(Player player)
        {
            var objectToSave = new PlayerToTransfer(player.DefaultName, player.Health, player.Damage, player.Shield,
                player.Position);
            string stringjson = JsonConvert.SerializeObject(objectToSave);
            File.WriteAllText(saveFile, stringjson);
        }
        
        /*public void SaveInventory(Dictionary<string, int> inventory)
        {
            var objectToSave = new InventoryToTransfer(inventory);
            string stringjson = JsonConvert.SerializeObject(objectToSave);
            File.WriteAllText(saveFile, stringjson);
        }*/

        public JObject LoadPlayer()
        {
            // Does the file exist?
            if (File.Exists(saveFile))
            {
                using (StreamReader file = File.OpenText(saveFile))
                using (JsonTextReader reader = new JsonTextReader(file))
                {
                    JObject playerJsonData = (JObject) JToken.ReadFrom(reader);
                    // Read the entire file and save its contents.

                    return playerJsonData;
                }
            }
            throw new FileNotFoundException();
        }
        
        /*public JObject LoadInventory()
        {
            // Does the file exist?
            if (File.Exists(saveFile))
            {
                using (StreamReader file = File.OpenText(saveFile))
                using (JsonTextReader reader = new JsonTextReader(file))
                {
                    JObject inventoryJsonData = (JObject) JToken.ReadFrom(reader);
                    // Read the entire file and save its contents.

                    return inventoryJsonData;
                }
            }
            throw new FileNotFoundException();
        }*/
    }
}
