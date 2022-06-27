namespace DesignPatternsInfo;

public class CompanyBankAccount : BankAccount
{
    public void TakeLoan(float amount)
    {
        Console.WriteLine("Taking loan..");
    }

    public override void MakeWithDrawal(float amount)
    {
        Console.WriteLine("Company bank account withdrawal");
        if (amount < 0) throw new Exception("Amount must be positive number");

        Balance -= amount;
    }
}