namespace Library;

public class Book : Item
{
    public enum BookCategory
    {
        Novel,
        Textbook,
        Encyclopedia
    }

    public Book(int id, string name, int numberOfPages, BookCategory bookCategory) : base(id, name)
    {
        NumberOfPages = numberOfPages;
    }

    private int NumberOfPages { get; }

    public BookCategory Category { get; }

    public override string ToString()
    {
        return base.ToString() + $", NumberOfPages: {NumberOfPages}, Category: {Category}";
    }
}