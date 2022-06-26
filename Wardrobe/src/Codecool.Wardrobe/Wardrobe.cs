using System.Linq;
using System.Text;

namespace Codecool.Wardrobe;

public class Wardrobe
{
    private readonly Hanger?[] _hangers;
    private readonly int _size;

    public Wardrobe(int size)
    {
        _size = size;
        _hangers = new Hanger[_size];
    }

    private bool IsFree(int position)
    {
        return !InvalidPosition(position) && _hangers[GetIndex(position)] == null;
    }

    private bool HasFreeHanger(int position)
    {
        return !InvalidPosition(position) && (_hangers[GetIndex(position)]?.IsNotFull ?? false);
    }

    public bool PutOnClothing(int position, Clothing clothing)
    {
        if (HasFreeHanger(position)) return _hangers[GetIndex(position)].HangOn(clothing);

        return false;
    }

    public bool PutOnHanger(int position, Hanger hanger)
    {
        if (IsFree(position))
        {
            _hangers[GetIndex(position)] = hanger;
            return true;
        }

        return false;
    }

    public Hanger? TakeOffHanger(int position)
    {
        if (!IsFree(position))
        {
            var hanger = _hangers[GetIndex(position)];
            _hangers[GetIndex(position)] = null;

            return hanger;
        }

        return null;
    }

    private bool InvalidPosition(int position)
    {
        return position < 1 || position > _size;
    }

    private int GetIndex(int position)
    {
        return position - 1;
    }

    private int GetPosition(int index)
    {
        return index + 1;
    }

    private Hanger? FindHangerForClothing(string id)
    {
        return _hangers.FirstOrDefault(hanger => hanger.HasClothing(id));
    }

    public Clothing? TakeOffClothing(string id)
    {
        return FindHangerForClothing(id)?.TakeOff(id);
    }

    public override string ToString()
    {
        var stringBuilder = new StringBuilder();
        stringBuilder.Append("Wardrobe:\n");
        for (var i = 0; i < _hangers.Length; i++)
            stringBuilder.Append($"#{GetPosition(i)}: {_hangers[i]?.ToString() ?? "empty"}\n");
        return stringBuilder.ToString();
    }

    public Hanger? GetFreeHangerForClothingType(ClothingType type)
    {
        return _hangers.FirstOrDefault(hanger => hanger?.CanHangOnClothingType(type) ?? false);
    }
}