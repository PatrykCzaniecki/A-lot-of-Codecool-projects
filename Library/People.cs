namespace Library;

public abstract class People
{
    public List<Item> Items = new();

    protected People(string firstName, string lastName, string email)
    {
        FirstName = firstName;
        LastName = lastName;
        Email = email;
    }

    public string FirstName { get; }

    public string LastName { get; }

    public string Email { get; }

    public abstract bool CanBorrowItem { get; }

    public override string ToString()
    {
        return $"First Name: {FirstName}, Last Name: {LastName}, Email: {Email}";
    }

    public void AddItem(Item item)
    {
        Items.Add(item);
    }

    public void ReturnItem(int id)
    {
        var item = Items.FirstOrDefault(item => item.Id == id);

        if (item != null)
            Items.Remove(item);
        else
            throw new Exception($"This person doesn't have this item: {id}");
    }
}