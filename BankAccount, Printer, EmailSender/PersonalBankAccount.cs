namespace DesignPatternsInfo;

public class PersonalBankAccount : BankAccount
{
    public void RequestPersonalLoan()
    {
        Console.WriteLine("Making personal request");
    }

    public override void MakeWithDrawal(float amount)
    {
        Console.WriteLine("Personal bank account withdrawal");
        if (amount < 0) throw new Exception("Amount must be positive number");

        if (Balance - amount < 0) throw new Exception("Personal bank account cannot go in debt");

        Balance -= amount;
    }
}