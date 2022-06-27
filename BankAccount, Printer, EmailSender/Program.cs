namespace DesignPatternsInfo;

internal class Program
{
    private static void Main(string[] args)
    {
        var person1 = new Person("Kuba", 23);

        person1.SayHi();
        Console.WriteLine(person1.Name);

        var printer = GetPrinter();
        printer.Print("This is my content");

        var bankAccount = new PersonalBankAccount();

        bankAccount.MakeDeposite(1000);
        bankAccount.MakeWithDrawal(200);
        bankAccount.Name = "My bank account name";

        Console.WriteLine(bankAccount.GetBalance());
        Console.WriteLine(bankAccount.Name);
        bankAccount.RequestPersonalLoan();

        bankAccount = (PersonalBankAccount) GetBankAccount();
        bankAccount.MakeWithDrawal(1100);

        var emailSender = new EmailSender();

        emailSender.ConnectToSmtpServer();
        emailSender.InsertCredentials();

        emailSender.SendEmail("to@gmail.com", "my title", "my message");

        emailSender.Disconnect();
    }

    private static IPrinter GetPrinter()
    {
        return new Hp();
    }

    private static BankAccount GetBankAccount()
    {
        var bankAccount = new CompanyBankAccount();
        bankAccount.MakeDeposite(1000);

        return bankAccount;
    }
}