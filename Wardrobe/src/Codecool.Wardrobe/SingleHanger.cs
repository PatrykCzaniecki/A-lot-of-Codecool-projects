namespace Codecool.Wardrobe;

public class SingleHanger : Hanger
{
    private Clothing? _clothing;

    public override bool IsNotFull => _clothing is null;

    public override bool HangOn(Clothing clothing)
    {
        if (!IsNotFull) return false;

        if (!clothing.IsTop) return false;

        _clothing = clothing;

        return true;
    }

    public override Clothing? TakeOff(string id)
    {
        if (HasClothing(id))
        {
            var clothing = _clothing;
            _clothing = null;
            return clothing;
        }

        return null;
    }

    public override bool HasClothing(string id)
    {
        return _clothing?.Id == id;
    }

    public override bool CanHangOnClothingType(ClothingType type)
    {
        return IsNotFull && type.IsTop();
    }

    public override string ToString()
    {
        return $"Hanger (is not full = {IsNotFull}):\nTop: {_clothing?.ToString() ?? "empty"}";
    }
}