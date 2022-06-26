namespace Codecool.Wardrobe;

public abstract class Hanger
{
    public abstract bool IsNotFull { get; }

    public abstract bool HangOn(Clothing clothing);

    public abstract Clothing? TakeOff(string id);

    public abstract bool HasClothing(string id);

    public abstract bool CanHangOnClothingType(ClothingType type);
}