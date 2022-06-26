namespace Library;

public class Borrow
{
    public Borrow(int id, People people, DateTime dateTime)
    {
        Id = id;
        People = people;
        DateTime = dateTime;
    }

    public int Id { get; }

    public People People { get; }

    public DateTime DateTime { get; }
}