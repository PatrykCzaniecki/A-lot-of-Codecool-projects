namespace PhoneBook;

internal class PhoneBook
{
    public List<Contact> Contacts { get; set; } = new();

    public void AddContact(Contact contact)
    {
        Contacts.Add(contact);
    }

    public void DeleteContact(string numberToDelete)
    {
        var contactToDelete = Contacts.FirstOrDefault(x => x.Number == numberToDelete);
        if (contactToDelete == null)
        {
            Console.WriteLine("Contact not found");
        }
        else
        {
            Contacts.Remove(contactToDelete);
            Console.WriteLine($"Contact with number {numberToDelete} was deleted.");
        }
    }

    public void DisplayContact(string number)
    {
        var contact = Contacts.FirstOrDefault(x => x.Number == number);

        if (contact == null)
            Console.WriteLine("Contact not found");
        else
            DisplayContactDetails(contact);
    }

    public void DisplayAllContacts()
    {
        foreach (var contact in Contacts) DisplayContactDetails(contact);
    }

    private void DisplayContactDetails(Contact contact)
    {
        Console.WriteLine($"Contact: {contact.Name}, {contact.Number}");
    }

    public void DisplayMatchingContacts(string searchPhrase)
    {
        var matchingContacts = Contacts.Where(x => x.Name.Contains(searchPhrase)).ToList();
        foreach (var contact in matchingContacts) DisplayContactDetails(contact);
    }
}