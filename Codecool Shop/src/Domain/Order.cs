namespace Domain;

public class Order
{
    public int Id { get; set; }
    public Address Address { get; set; } = null!;
    public string User_id { get; set; } = null!;
    public PaymentInfo PaymentInfo { get; set; } = null!;
    public string OrderPayed { get; set; } = null!;
}