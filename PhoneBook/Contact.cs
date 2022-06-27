namespace PhoneBook;

public class Contact
{
    public Contact(string name, string number)
    {
        Name = name;
        Number = number;
    }

    public string Name { get; set; }
    public string Number { get; set; }
}