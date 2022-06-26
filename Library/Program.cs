namespace Library;

internal class Program
{
    public static void Main(string[] args)
    {
        var myLibrary = new Library();

        myLibrary.AddItem(new Book(1, "Hobbit", 500, Book.BookCategory.Novel));
        myLibrary.AddItem(new Book(2, "Zosia samosia", 123, Book.BookCategory.Textbook));
        myLibrary.AddItem(new CD(3, "Classic audiobook", 21));

        myLibrary.RegisterPeople(new Student("Patryk", "Czaniecki", "patrykczaniecki@gmail.com"));
        myLibrary.RegisterPeople(new TownResidence("Sławek", "Świętoniowski", "slawekswietoniowski@gmail.com"));

        myLibrary.BorrowItem(1, "patrykczaniecki@gmail.com", DateTime.Now);
    }
}