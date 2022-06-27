namespace DesignPatternsInfo;

public class EmailSender
{
    public void ConnectToSmtpServer()
    {
        Console.WriteLine("Connecting to smtp server");
    }

    public void InsertCredentials()
    {
        Console.WriteLine("Inserting credentials");
    }

    public void SendEmail(string to, string title, string body)
    {
        ConnectToSmtpServer();
        InsertCredentials();
        Console.WriteLine($"Sending email to: {to}, {title} {body}");
        Disconnect();
    }

    public void Disconnect()
    {
        Console.WriteLine("Disconnected from, the server");
    }
}