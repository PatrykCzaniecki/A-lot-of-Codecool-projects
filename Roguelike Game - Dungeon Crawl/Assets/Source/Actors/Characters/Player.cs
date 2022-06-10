using Assets.Source.Core;
using DungeonCrawl.Actors.Items;
using DungeonCrawl.Core;
using System.Collections.Generic;
using DungeonCrawl.Repository;
using Unity.Plastic.Newtonsoft.Json.Linq;
using UnityEngine;

namespace DungeonCrawl.Actors.Characters
{
    public class Player : Character
    {
        private bool isInventoryVisible = false;
        public Dictionary<string, int> Inventory { get; set; }
        public Player()
        {
            Health = 100;
            Damage = 5;
            Shield = 0;
            Inventory = new Dictionary<string, int>();
        }

        public void AddToInventory(Item item)
        {
            if (item is Key key)
            {
                Inventory.Add("key", 1);
                Destroy(key.gameObject);
            }
            else if (item is Sword sword)
            {
                Damage += sword.damage;
                Inventory.Add("sword", 1);
                Destroy(sword.gameObject);
            }
            else if (item is Armor armor)
            {
                Shield += armor.Shield;
                Inventory.Add("shield", 1);
                Destroy(armor.gameObject);
            }
            else if (item is Necklace necklace)
            {
                Shield += necklace.Shield;
                Inventory.Add("Magic Necklace", 1);
                Destroy(necklace.gameObject);
            }
            else if (item is Ring ring)
            {
                Health += ring.Health;
                Inventory.Add("Ring of Life", 1);
                Destroy(ring.gameObject);
            }
            else if (item is Shovel shovel)
            {
                Damage += shovel.damage;
                Inventory.Add("Shovel of The Gods", 1);
                Destroy(shovel.gameObject);
            }
            else if (item is SilverKey silverKey)
            {
                Inventory.Add("Silver Key", 1);
                Destroy(silverKey.gameObject);
            }
            else if (item is Trident trident)
            {
                Damage += trident.damage;
                Inventory.Add("The Trident of Death", 1);
                Destroy(trident.gameObject);
            }
            else if (item is HealthPotion potion)
            {
                Health += potion.Health;
                Inventory.Add("HealthPotion", 1);
                Destroy(potion.gameObject);
            }
        }

        protected override void OnUpdate(float deltaTime)
        {
            if (Input.GetKeyDown(KeyCode.F5))
            {
                //Save game
                PlayerDao.SaveGame(DefaultName, Health, Damage, Shield, Position.x, Position.y,MapLoader.MapId);
                PlayerDao.SaveGameInventory(Inventory);
            }
            if (Input.GetKeyDown(KeyCode.F9))
            {
                //Load game
                LoadPlayer();
                Inventory.Clear();
                LoadPlayerInventory();
            }
            if (Input.GetKeyDown(KeyCode.F10))
            {
                JsonManager.Singleton.SavePlayer(this);
                //JsonManager.Singleton.SaveInventory(this);
            }
            if (Input.GetKeyDown(KeyCode.F11))
            {
                LoadPlayerFromJson(JsonManager.Singleton.LoadPlayer());
                //LoadInventoryFromJson(JsonManager.Singleton.LoadInventory());
            }

            if (Input.GetKeyDown(KeyCode.W))
            {
                // Move down
                PlayerTryMove(Direction.Up);
            }
            
            if (Input.GetKeyDown(KeyCode.S))
            {
                // Move down
                PlayerTryMove(Direction.Down);
            }

            if (Input.GetKeyDown(KeyCode.A))
            {
                // Move left
                PlayerTryMove(Direction.Left);
            }

            if (Input.GetKeyDown(KeyCode.D))
            {
                // Move right
                PlayerTryMove(Direction.Right);
            }
            if (Input.GetKeyDown(KeyCode.I))
            {
                string text = "Inventory:\n";
                if (!isInventoryVisible)
                {
                    foreach (var item in Inventory)
                    {
                        text += $"{item.Key}\n";
                    }
                }
                isInventoryVisible = !isInventoryVisible;
                UserInterface.Singleton.SetText($"{text}", UserInterface.TextPosition.BottomLeft);
                UserInterface.Singleton.SetText($"My health: {Health}\n" + $"My damage: {Damage}\n" + $"My shield: {Shield}\n", UserInterface.TextPosition.TopLeft);
            }
            CameraController.Singleton.Position = Position;
        }

        public void DestroyDoor()
        {
            ActorManager.Singleton.DestroyActor(this);
        }

        protected override void OnDeath()
        {
            Debug.Log("Oh no, I'm dead!");
        }

        public void LoadPlayer()
        {
            var loadedData = GameManager.LoadGame() as dynamic;
            if (loadedData != null)
            {
                Health = loadedData.Hp;
                Damage = loadedData.Damage;
                Shield = loadedData.Shield;
                Position = ((int) loadedData.X, (int) loadedData.Y);
                if (loadedData.Map != MapLoader.MapId)
                {
                    MapLoader.MapId = loadedData.Map;
                    MapLoader.LoadMap();
                }
            }
        }
        
        public void LoadPlayerInventory()
        {
            var loadedData = GameManager.LoadGameInventory();
            if (loadedData != null)
            {
                Inventory = loadedData;
            }
        }

        public void LoadPlayerFromJson(JObject loadedPlayer)
        {
            Health = (int)loadedPlayer["Health"];
            Position = (((int)(loadedPlayer["X"])), ((int)(loadedPlayer["Y"])));
            Damage = (int) loadedPlayer["Damage"];
            Shield = (int) loadedPlayer["Shield"];
        }

        public void LoadInventoryFromJson(JObject loadedInventory)
        {
            //Inventory = Dictionary<string, int> loadedInventory;
        }

        public override int DefaultSpriteId => 24;
        public override string DefaultName => "Player";
        public override bool FightMode => true;
    }
}
