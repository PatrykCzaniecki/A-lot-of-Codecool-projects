namespace Codecool.Wardrobe;

public class DoubleHanger : Hanger
{
    private Clothing? _bottomClothing;
    private Clothing? _topClothing;

    public override bool IsNotFull => _topClothing is null || _bottomClothing is null;

    public override bool HangOn(Clothing clothing)
    {
        if (!IsNotFull) return false;

        if (_topClothing is null && clothing.IsTop)
        {
            _topClothing = clothing;
            return true;
        }

        if (_bottomClothing is null && clothing.IsBottom)
        {
            _bottomClothing = clothing;
            return true;
        }

        return false;
    }

    public override Clothing? TakeOff(string id)
    {
        if (_topClothing is not null && _topClothing.Id == id)
        {
            var clothing = _topClothing;
            _topClothing = null;
            return clothing;
        }

        if (_bottomClothing is not null && _bottomClothing.Id == id)
        {
            var clothing = _bottomClothing;
            _bottomClothing = null;
            return clothing;
        }

        return null;
    }

    public override bool HasClothing(string id)
    {
        return _topClothing?.Id == id || _bottomClothing?.Id == id;
    }

    public override bool CanHangOnClothingType(ClothingType type)
    {
        return IsNotFull &&
               ((_topClothing == null && type.IsTop()) ||
                (_bottomClothing == null && type.IsBottom()));
    }

    public override string ToString()
    {
        return
            $"Hanger (is not full = {IsNotFull}):\nTop: {_topClothing?.ToString() ?? "empty"}\nBottom: {_bottomClothing?.ToString() ?? "empty"}";
    }
}