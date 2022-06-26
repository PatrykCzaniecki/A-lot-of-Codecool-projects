namespace Library;

public class TownResidence : People
{
    private const int AmountOfItemsToBorrow = 5;

    public TownResidence(string firstName, string lastName, string email) : base(firstName, lastName, email)
    {
    }

    public override bool CanBorrowItem => Items.Count < AmountOfItemsToBorrow;
}