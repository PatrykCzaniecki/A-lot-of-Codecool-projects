using System.ComponentModel.DataAnnotations;

namespace Domain;

public class PaymentInfo
{
    [Key] public int Id { get; set; }
    public string NameOnCard { get; set; } = null!;
    public string CardNumber { get; set; } = null!;
    public string ExpMonth { get; set; } = null!;
    public string ExpYear { get; set; } = null!;
    public string CVV { get; set; } = null!;
}