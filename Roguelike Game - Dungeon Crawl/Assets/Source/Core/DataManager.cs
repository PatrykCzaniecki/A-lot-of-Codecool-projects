using UnityEngine;
using System.Data.SqlClient;

namespace DungeonCrawl.Core
{
    public class DataManager : MonoBehaviour
    {
        public static DataManager Singleton { get; private set; }

        private void Awake()
        {
            if (Singleton != null)
            {
                Destroy(this);
                return;
            }

            Singleton = this;
        }

        public SqlConnection ConnectionBuilder()
        {
            SqlConnection connection =
                new SqlConnection(@"Server=DESKTOP-L87LOKJ;Database=Dungeon;User Id=user;Password=codecool;");
                /*new SqlConnection(@"Server=localhost;Database=Dungeon;User Id=user2;Password=codecool;");*/
            return connection;
        }
    }
}
