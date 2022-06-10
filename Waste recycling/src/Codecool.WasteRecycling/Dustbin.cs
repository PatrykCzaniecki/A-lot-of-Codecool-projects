using System;

namespace Codecool.WasteRecycling
{
    public class Dustbin
    {
        //Dustbin instances can only be instantiated by supplying a color name.
        public Dustbin(string color)
        {
            Color = color;
            GarbageBin = new DynamicArray();
        }
        //Dustbin instances allow access to the color name with which they are created, using the get-only Color property.
        public string Color { get; private set; }
        public DynamicArray GarbageBin { get; private set; }

        //Dustbin instances allow access to the number of different kinds of garbage stored in them, using the following properties. HouseWasteCount - PaperCount - PlasticCount
        public int HouseWasteCount { get; private set; }
        public int PaperWasteCount { get; private set; }
        public int PlasticWasteCount { get; private set; }

        //Dustbin instances allow Garbage instances to be thrown into them using the ThrowOutGarbage(Garbage) method.
        public void ThrowOutGarbage(Garbage garbage)
        {
            //Dustbin instances only allow the following kinds of garbage to be thrown into them.
            //Cleaned PlasticGarbage -Squeezed PaperGarbage - Any other kind of Garbage(such as house waste), Otherwise, a DustbinContentException occurs.
            if (garbage is PaperGarbage)
            {
                PaperGarbage paperGarbage = (PaperGarbage)garbage;
                if (!paperGarbage.Squeezed)
                {
                    throw new DustbinContentException();
                }
            }

            if (garbage is PlasticGarbage)
            {
                PlasticGarbage plasticGarbage = (PlasticGarbage)garbage;
                if (!plasticGarbage.Cleaned)
                {
                    throw new DustbinContentException();
                }
            }
            GarbageBin.Add(garbage);
        }

        //Dustbin instances provide a way to clear their contents, using the EmptyContents() method.
        public void EmptyContents()
        {
            GarbageBin.Clear();
        }

        //A Dustbin provides a way to get its textual representation, using the ToString() method. The representation is similar to the following example.
        public override string ToString()
        {
            string houseWasteContent = "";
            string paperWasteContent = "";
            string plasticWasteContent = "";
            int houseWasteCount = 0;
            int paperWasteCount = 0;
            int plasticWasteCount = 0;

            foreach (var garbage in GarbageBin._array)
            {
                if (garbage is PaperGarbage && garbage != null)
                {
                    paperWasteCount++;
                    paperWasteContent += $"{garbage.Name} nr.{paperWasteCount}\n";
                }
                else if (garbage is PlasticGarbage && garbage != null)
                {
                    plasticWasteCount++;
                    plasticWasteContent += $"{garbage.Name} nr.{plasticWasteCount}\n";
                }
                else if (garbage != null)
                {
                    houseWasteCount++;
                    houseWasteContent += $"{garbage.Name} nr.{houseWasteCount}\n";
                }
            }
            return $"{Color} Dustbin!\nHouse waste content: {houseWasteCount} item(s)\n{houseWasteContent} \n" +
                   $"Paper content: {paperWasteCount} item(s)\n{paperWasteContent} \n" +
                   $"Plastic content: {plasticWasteCount} item(s)\n{plasticWasteContent}";
        }

        //Dustbin instances provide the possibility to print their textual representation to the console, using the DisplayContents() method.
        public void DisplayContents()
        {
            Console.WriteLine(ToString());
        }
    }
}
