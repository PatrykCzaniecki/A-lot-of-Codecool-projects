namespace Codecool.WasteRecycling
{
    public class Garbage
    {
        //Garbage instances can only be instantiated by supplying a garbage name.
        public Garbage(string name)
        {
            Name = name;
        }
        //Garbage instances allow access to the name with which they are created, using the get-only Name property.
        public string Name { get; private set; }
    }
}
