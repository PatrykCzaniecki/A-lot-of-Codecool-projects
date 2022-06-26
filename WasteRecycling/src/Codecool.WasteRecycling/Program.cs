using System;

namespace Codecool.WasteRecycling;

public class Program
{
    public static void Main(string[] args)
    {
        var dustbin = new Dustbin("Orange");
        var regularGarbage1 = new Garbage("Chewed Apple");
        var regularGarbage2 = new Garbage("Something weird and moldy");
        var paperGarbage1 = new PaperGarbage("Unfinished Essay");
        var paperGarbage2 = new PaperGarbage("Unpayed Bills");
        var paperGarbage3 = new PaperGarbage("House Mortgage");
        var plasticGarbage1 = new PlasticGarbage("Mineral Water Bottle");
        var plasticGarbage2 = new PlasticGarbage("McDonalds Fork");
        var plasticGarbage3 = new PlasticGarbage("Wrapper");
        try
        {
            paperGarbage1.Squeeze();
            paperGarbage2.Squeeze();
            paperGarbage3.Squeeze();
            plasticGarbage1.Clean();
            plasticGarbage2.Clean();
            dustbin.ThrowOutGarbage(regularGarbage1);
            dustbin.ThrowOutGarbage(regularGarbage2);
            dustbin.ThrowOutGarbage(paperGarbage1);
            dustbin.ThrowOutGarbage(paperGarbage2);
            dustbin.ThrowOutGarbage(paperGarbage3);
            dustbin.ThrowOutGarbage(plasticGarbage1);
            dustbin.ThrowOutGarbage(plasticGarbage2);
            dustbin.ThrowOutGarbage(plasticGarbage3);
        }
        catch (DustbinContentException)
        {
            Console.WriteLine("Please prepare your garbage properly, before throwing it out!");
        }
        finally
        {
            dustbin.DisplayContents();
            dustbin.EmptyContents();
            dustbin.DisplayContents();
        }
    }
}
