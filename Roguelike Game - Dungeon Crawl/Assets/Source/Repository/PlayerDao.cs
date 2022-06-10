using Assets.Source.Core;
using DungeonCrawl.Core;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Threading.Tasks;
using UnityEngine;

namespace DungeonCrawl.Repository
{
    public class PlayerDao : MonoBehaviour
    {
        public static void SaveGame(string name, int hp, int damage, int shield, int x, int y, int map)
        {
            ClearPlayerTable();
            
            const string insertPlayerSql = @"
            INSERT INTO player (player_name,hp,damage,shield,x,y,map)
            VALUES (@player_name,@hp,@damage,@shield,@x,@y,@map);";

            try
            {
                using var connection = DataManager.Singleton.ConnectionBuilder();
                connection.Open();
                using var command = connection.CreateCommand();
                command.CommandType = CommandType.Text;
                command.CommandText = insertPlayerSql;
                command.Parameters.AddWithValue("@player_name", name);
                command.Parameters.AddWithValue("@hp", hp);
                command.Parameters.AddWithValue("@damage", damage);
                command.Parameters.AddWithValue("@shield", shield);
                command.Parameters.AddWithValue("@x", x);
                command.Parameters.AddWithValue("@y", y);
                command.Parameters.AddWithValue("@map", map);
                command.ExecuteNonQuery();
                connection.Close();
            }
            catch (SqlException)
            {
                Debug.Log("Saved Failed");
            }
            displayTextGameSave();
        }
        
        private async static void displayTextGameSave()
        {
            string message = "Game Saved!";
            UserInterface.Singleton.SetText($"{message}", UserInterface.TextPosition.TopCenter);
            await Task.Delay(5000);
            string message1 = "";
            UserInterface.Singleton.SetText($"{message1}", UserInterface.TextPosition.TopCenter);
        }
        
        private async static void displayTextGameLoad()
        {
            string message = "Game Loaded";
            UserInterface.Singleton.SetText($"{message}", UserInterface.TextPosition.TopCenter);
            await Task.Delay(5000);
            string message1 = "";
            UserInterface.Singleton.SetText($"{message1}", UserInterface.TextPosition.TopCenter);
        }

        private static  void ClearPlayerTable()
        {
            const string deleteAllRowsSql = @"DELETE FROM player";
            var connection = DataManager.Singleton.ConnectionBuilder();
            connection.Open();
            using var command = connection.CreateCommand();
            command.CommandType = CommandType.Text;
            command.CommandText = deleteAllRowsSql;
            command.ExecuteNonQuery();
            connection.Close();
        }

        private static void ClearInventoryTable()
        {
            const string deleteAllRowsSql = @"DELETE FROM inventory";
            var connection = DataManager.Singleton.ConnectionBuilder();
            connection.Open();
            using var command = connection.CreateCommand();
            command.CommandType = CommandType.Text;
            command.CommandText = deleteAllRowsSql;
            command.ExecuteNonQuery();
            connection.Close();
        }

        public static void SaveGameInventory(IDictionary<string, int> Inventory)
        {
            ClearInventoryTable();

            const string insertInvenorySql = @"
            INSERT INTO inventory (item_name,amount)
            VALUES (@item_name,@amount);";

            foreach (var key in Inventory)
            {
                var item_name = key.Key;
                var amount = key.Value;
                try
                {
                    var connection = DataManager.Singleton.ConnectionBuilder();
                    connection.Open();
                    using var command = connection.CreateCommand();
                    command.CommandType = CommandType.Text;
                    command.CommandText = insertInvenorySql;
                    command.Parameters.AddWithValue("@item_name", item_name);
                    command.Parameters.AddWithValue("@amount", amount);
                    command.ExecuteNonQuery();
                    connection.Close();
                }
                catch (SqlException )
                {
                    Debug.Log("Saved Failed");
                }
            }
        }
        
        public static object LoadGame()
        {
            displayTextGameLoad();
            const string selectPlayerSql = @"SELECT * FROM player ORDER BY id DESC;";
            
            var connection = DataManager.Singleton.ConnectionBuilder();
            connection.Open();
            using var command = connection.CreateCommand();
            command.CommandType = CommandType.Text;
            command.CommandText = selectPlayerSql;
            using var dataReader = command.ExecuteReader();
            if (dataReader.Read())
            {
                var name = (string)dataReader["player_name"];
                var hp = (int)dataReader["hp"];
                var damage = (int)dataReader["damage"];
                var shield = (int)dataReader["shield"];
                var x = (int)dataReader["x"];
                var y = (int)dataReader["y"];
                var map = (int)dataReader["map"];

                var loadData = new
                { Name = name, Hp = hp, Damage = damage, Shield = shield, X = x, Y = y, Map = map };
                return loadData;
            }
            else
            {
                throw new InvalidOperationException();
            }
        }
        
        public static Dictionary<string, int> LoadGameInventory()
        {
            displayTextGameLoad();

            const string selectInventorySql = @"SELECT * FROM inventory ORDER BY id DESC;";

            var connection = DataManager.Singleton.ConnectionBuilder();
            connection.Open();
            using var command = connection.CreateCommand();
            command.CommandType = CommandType.Text;
            command.CommandText = selectInventorySql;
            using var dataReader = command.ExecuteReader();
            var loadDataInventory = new Dictionary<string, int>();
            
            while (dataReader.Read())
            {
                var item = (string)dataReader["item_name"];
                var amount = (int) dataReader["amount"];
                
                loadDataInventory.Add(item, amount);
            }
            return loadDataInventory;
        }
    }
}
