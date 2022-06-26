using System;

namespace Codecool.Wardrobe;

public class Clothing
{
    public Clothing(string name, ClothingType type)
    {
        Id = Guid.NewGuid().ToString();
        Name = name;
        Type = type;
    }

    public string Id { get; }
    public string Name { get; }
    public ClothingType Type { get; }

    public bool IsTop => Type.IsTop();
    public bool IsBottom => Type.IsBottom();

    public override string ToString()
    {
        return $"Clothing: {{{Id}, {Name}, {Type}}}";
    }
}