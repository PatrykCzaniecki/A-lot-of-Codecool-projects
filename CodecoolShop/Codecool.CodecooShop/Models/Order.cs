namespace Codecool.CodecoolShop.Models;

public class Order
{
    public Cart Cart { get; set; }

    public PaymentInfo PaymentInfo { get; set; }

    public Address Address { get; set; }
}