using System;

namespace Codecool.Wardrobe;

public class Program
{
    public static void Main(string[] args)
    {
        var wardrobeSize = 5;

        var wardrobe = new Wardrobe(wardrobeSize);

        var shirt = new Clothing("Shirt #1", ClothingType.Shirt);
        var shirtId = shirt.Id;
        Hanger singleHanger = new SingleHanger();
        singleHanger.HangOn(shirt);
        wardrobe.PutOnHanger(1, singleHanger);

        var blouse = new Clothing("Blouse #1", ClothingType.Blouse);
        var blouseId = blouse.Id;
        var trousers = new Clothing("Trousers #1", ClothingType.Trousers);
        Hanger doubleHanger = new DoubleHanger();

        doubleHanger.HangOn(blouse);
        doubleHanger.HangOn(trousers);
        wardrobe.PutOnHanger(2, doubleHanger);
        Console.WriteLine(wardrobe);
        var shirt2 = new Clothing("Shirt #2", ClothingType.Shirt);

        if (singleHanger.HangOn(shirt2))
            Console.WriteLine("Clothing hang on!");
        else
            Console.WriteLine("Unable to hang on clothing!");

        if (wardrobe.PutOnHanger(1, doubleHanger))
            Console.WriteLine("Hanger put on!");
        else
            Console.WriteLine("Unable to put on hanger!");

        Console.WriteLine(wardrobe.TakeOffClothing(shirtId));
        Console.WriteLine(wardrobe);
        Console.WriteLine(wardrobe.TakeOffClothing(blouseId));
        Console.WriteLine(wardrobe);
        Console.WriteLine(wardrobe.TakeOffHanger(2));
        Console.WriteLine(wardrobe);
        wardrobe.PutOnClothing(1, shirt);
        Console.WriteLine(wardrobe);
        Console.WriteLine(wardrobe.TakeOffClothing(shirtId));
        var freeHanger = wardrobe.GetFreeHangerForClothingType(ClothingType.Shirt);
        Console.WriteLine(freeHanger);
    }
}