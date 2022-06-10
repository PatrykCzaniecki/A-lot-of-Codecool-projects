using System.Collections.Generic;
using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Repository;
using UnityEngine;

namespace DungeonCrawl.Core
{
    /// <summary>
    ///     Loads the initial map and can be used for keeping some important game variables
    /// </summary>
    public class GameManager : MonoBehaviour
    {
        
        private void Start()
        {
            MapLoader.LoadMap();
        }
        public static void SaveGame (string name, int hp, int damage, int shield, int x, int y, int map)
        {
            PlayerDao.SaveGame( name,  hp,  damage,  shield,  x,  y,  map);
        }

        public static object LoadGame()
        {
            var loadData = PlayerDao.LoadGame();
            return loadData;
        }
        
        public static Dictionary<string, int> LoadGameInventory()
        {
            var loadData = PlayerDao.LoadGameInventory();
            return loadData;
        }
    }
}
