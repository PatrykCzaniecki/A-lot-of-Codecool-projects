namespace DesignPatternsInfo;

public class BankAccount
{
    protected float Balance;

    public string Name { get; set; }

    public void MakeDeposite(float amount)
    {
        if (amount < 0) throw new Exception("Amount must be positive number");

        Balance += amount;
    }

    public virtual void MakeWithDrawal(float amount)
    {
        if (amount < 0) throw new Exception("Amount must be positive number");

        Balance -= amount;
    }

    public float GetBalance()
    {
        return Balance;
    }
}