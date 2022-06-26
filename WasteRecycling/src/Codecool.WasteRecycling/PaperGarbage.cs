namespace Codecool.WasteRecycling;

public class PaperGarbage : Garbage
{
    //PaperGarbage instances can only be instantiated by supplying a garbage name and a flag that signals whether they are squeezed, in this order.
    //PaperGarbage instances allow access to the name they with which they are created, just like Garbage instances do.
    public PaperGarbage(string name) : base(name)
    {
    }

    //PaperGarbage instances allow checking whether they are squeezed, using the Squeezed property. The property has a private setter.
    public bool Squeezed { get; private set; }

    //PaperGarbage instances provide a way to squeeze them, using the Squeeze() method. If a piece of paper garbage is already squeezed, using this method has no effect.
    public void Squeeze()
    {
        Squeezed = true;
    }
}
