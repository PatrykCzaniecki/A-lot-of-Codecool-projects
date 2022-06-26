namespace Library;

public class Library
{
    private const int MaxNumberDayBorrow = 7;

    private readonly List<Borrow> _borrows = new();

    private readonly List<Item> _items = new();

    private readonly List<People> _people = new();

    public void AddItem(Item item)
    {
        if (_items.Contains(item))
            Console.WriteLine($"This item {item} is already added!");
        else
            _items.Add(item);
    }

    public void RegisterPeople(People people)
    {
        if (_people.Contains(people))
            Console.WriteLine($"Person {people} is already registered!");
        else
            _people.Add(people);
    }

    public void BorrowItem(int id, string email, DateTime dateTime)
    {
        var item = _items.FirstOrDefault(item => item.Id == id);

        var people = _people.FirstOrDefault(people => people.Email == email);

        if (item is null) Console.WriteLine($"Item {id} is not in library!");

        if (item != null && item.IsBorrowed) Console.WriteLine($"Item {id} is already borrowed for somebody else!");

        if (people is null) Console.WriteLine($"People with email {email} in not registered!");

        if (people != null && people.CanBorrowItem)
        {
            item.IsBorrowed = true;
            _borrows.Add(new Borrow(id, people, dateTime));
            people.AddItem(item);

            Console.WriteLine($"Item {id} was borrow to {people} on {dateTime.ToShortDateString()}");
        }
        else
        {
            Console.WriteLine("This reader reach the limit of the items to borrow!");
        }
    }
}