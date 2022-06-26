namespace Library;

public class Student : People
{
    private const int AmountOfItemsToBorrow = 3;

    public Student(string firstName, string lastName, string email) : base(firstName, lastName, email)
    {
    }

    public override bool CanBorrowItem => Items.Count < AmountOfItemsToBorrow;
}