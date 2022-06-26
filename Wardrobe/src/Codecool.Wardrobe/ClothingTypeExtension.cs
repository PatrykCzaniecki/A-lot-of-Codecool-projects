namespace Codecool.Wardrobe;

public static class ClothingTypeExtension
{
    public static bool IsTop(this ClothingType type)
    {
        return type is ClothingType.Blouse or ClothingType.Shirt;
    }

    public static bool IsBottom(this ClothingType type)
    {
        return type is ClothingType.Trousers or ClothingType.Skirt;
    }
}