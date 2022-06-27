namespace PhoneBook;

internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Welcome in PhoneBook");
        Console.WriteLine("1 Add contact");
        Console.WriteLine("2 Display contact by number");
        Console.WriteLine("3 Display all contacts");
        Console.WriteLine("4 Search contacts");
        Console.WriteLine("5 Delete specific contact");
        Console.WriteLine("6 To exit from PhoneBook");

        var userInput = Console.ReadLine();
        var phoneBook = new PhoneBook();

        while (true)
        {
            switch (userInput)
            {
                case "1":
                    Console.WriteLine("Insert Name");
                    var name = Console.ReadLine();
                    Console.WriteLine("Insert Number");
                    var number = Console.ReadLine();
                    var newContact = new Contact(name, number);
                    phoneBook.AddContact(newContact);
                    break;
                case "2":
                    Console.WriteLine("Insert number to search");
                    var numberToSearch = Console.ReadLine();
                    phoneBook.DisplayContact(numberToSearch);
                    break;
                case "3":
                    phoneBook.DisplayAllContacts();
                    break;
                case "4":
                    Console.WriteLine("Insert search phrase");
                    var searchPhrase = Console.ReadLine();
                    phoneBook.DisplayMatchingContacts(searchPhrase);
                    break;
                case "5":
                    Console.WriteLine("Insert number of contact to delete");
                    var numberToDelete = Console.ReadLine();
                    phoneBook.DeleteContact(numberToDelete);
                    break;
                case "6":
                    return;
                default:
                    Console.WriteLine("Invalid operation");
                    break;
            }

            Console.WriteLine("Select operation");
            userInput = Console.ReadLine();
        }
    }
}