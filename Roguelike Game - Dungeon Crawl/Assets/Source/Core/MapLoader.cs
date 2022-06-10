using DungeonCrawl.Actors.Characters;
using DungeonCrawl.Actors.Static;
using System;
using System.Text.RegularExpressions;
using DungeonCrawl.Actors.Items;
using UnityEngine;

namespace DungeonCrawl.Core
{
    /// <summary>
    ///     MapLoader is used for constructing maps from txt files
    /// </summary>
    public static class MapLoader
    {
        /// <summary>
        ///     Constructs map from txt file and spawns actors at appropriate positions
        /// </summary>
        /// <param name="id"></param>
        ///
        public static int MapId { get; set; } = 1;

        public static void LoadMap()
        {
            if (MapId == 2)
            {
                CameraController.Singleton._camera.backgroundColor = Color.black;
            }

            ActorManager.Singleton.DestroyAllActors();
            var lines = Regex.Split(Resources.Load<TextAsset>($"map_{MapId}").text, "\r\n|\r|\n");

            // Read map size from the first line
            var split = lines[0].Split(' ');
            var width = int.Parse(split[0]);
            var height = int.Parse(split[1]);

            // Create actors
            for (var y = 0; y < height; y++)
            {
                var line = lines[y + 1];
                for (var x = 0; x < width; x++)
                {
                    var character = line[x];
                    SpawnActor(character, (x, -y));
                }
            }

            // Set default camera size and position
            CameraController.Singleton.Size = 10;
            CameraController.Singleton.Position = (width / 2, -height / 2);
        }

        public static void SpawnBone((int x, int y) position)
        {
            ActorManager.Singleton.Spawn<Bone>(position);
        }

        private static void SpawnActor(char c, (int x, int y) position)
        {
            if (MapId == 1)
            {
                switch (c)
                {
                    case '#':
                        ActorManager.Singleton.Spawn<Wall>(position);
                        break;
                    case '.':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        break;
                    case 'p':
                        ActorManager.Singleton.Spawn<Player>(position);
                        ActorManager.Singleton.Spawn<Floor>(position);
                        break;
                    case 's':
                        ActorManager.Singleton.Spawn<Skeleton>(position);
                        ActorManager.Singleton.Spawn<Floor>(position);
                        break;
                    case ' ':
                        break;
                    case 'S':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Sword>(position);
                        break;
                    case 't':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Armor>(position);
                        break;
                    case 'k':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Key>(position);
                        break;
                    case 'd':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Door>(position);
                        break;
                    case 'H':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Ghost>(position);
                        break;
                    case 'G':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Golem>(position);
                        break;
                    case 'B':
                        ActorManager.Singleton.Spawn<Floor>(position);
                        ActorManager.Singleton.Spawn<Bone>(position);
                        break;
                    default:
                        throw new ArgumentOutOfRangeException();
                }
            }

            if (MapId == 2)
            {
                switch (c)
                {
                    case '@':
                        ActorManager.Singleton.Spawn<River>(position);
                        break;

                    case '#':
                        ActorManager.Singleton.Spawn<Trees>(position);
                        break;
                    case '!':
                        ActorManager.Singleton.Spawn<Bridge>(position);
                        break;
                    case '.':
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 's':
                        ActorManager.Singleton.Spawn<Skeleton>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'S':
                        ActorManager.Singleton.Spawn<Trident>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'q':
                        ActorManager.Singleton.Spawn<Shovel>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'z':
                        ActorManager.Singleton.Spawn<Shaman>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'd':
                        ActorManager.Singleton.Spawn<Door>(position);
                        break;
                    case 'k':
                        ActorManager.Singleton.Spawn<SilverKey>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'r':
                        ActorManager.Singleton.Spawn<Ring>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'm':
                        ActorManager.Singleton.Spawn<Necklace>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case 'g':
                        ActorManager.Singleton.Spawn<Ghost>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                    case'H' :
                        ActorManager.Singleton.Spawn<HealthPotion>(position);
                        ActorManager.Singleton.Spawn<Grass>(position);
                        break;
                }
            }
        }
    }
}
