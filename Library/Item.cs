namespace Library;

public abstract class Item
{
    protected Item(int id, string name)
    {
        Id = id;
        Name = name;
    }

    public int Id { get; set; }

    public string Name { get; set; }

    public bool IsBorrowed { get; set; } = false;

    public override string ToString()
    {
        return $"ID: {Id}, Name: {Name}";
    }
}