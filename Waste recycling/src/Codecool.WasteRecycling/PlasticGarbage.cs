namespace Codecool.WasteRecycling
{
    public class PlasticGarbage : Garbage
    {
        //PlasticGarbage instances can only be instantiated by supplying a garbage name and a flag that signals whether they are clean, in this order.
        //PlasticGarbage instances allow access to the name with which they are created, just like Garbage instances do.
        public PlasticGarbage(string name) : base(name)
        {
        }
        //PlasticGarbage instances allow checking whether they are clean, using the Cleaned property. The property has a private setter.
        public bool Cleaned { get; private set; }

        //PlasticGarbage instances provide a way to clean them, using the Clean() method. If a piece of plastic garbage is already clean, using this method has no effect.
        public void Clean()
        {
            Cleaned = true;
        }
    }
}
