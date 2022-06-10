using System;
using System.Collections.Generic;
using System.IO;

namespace Codecool.LifeOfAnts.Img
{
    public class View
    {
        /// <summary>
        /// Static method for image printing
        /// </summary>
        /// <param name="fileName"> String with the filename</param>
        public static void PrintFile(string fileName)
        {
            Console.ForegroundColor = ConsoleColor.Cyan;
            IEnumerable<string> fileContent;

            var filesFolderName = Directory.GetParent(System.Reflection.Assembly.GetEntryAssembly().Location).Parent.Parent.Parent + "\\Image\\";
            fileContent = File.ReadLines(filesFolderName + fileName);
            string gameTitle = string.Empty;

            foreach (string line in fileContent)
            {
                Console.WriteLine(gameTitle + line);
            }
            Console.ResetColor();
        }
    }
}
