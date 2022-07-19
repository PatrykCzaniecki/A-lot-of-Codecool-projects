using System.ComponentModel;
using System.ComponentModel.DataAnnotations;

namespace Codecool.CodecoolShop.Models;

public class PaymentInfo
{
    [DisplayName("Name on card")]
    [Required]
    public string NameOnCard { get; set; }

    [StringLength(16)]
    [DisplayName("Card number")]
    [Required]
    public string CardNumber { get; set; }

    [StringLength(2)]
    [DisplayName("Expiration month")]
    [Required]
    public string ExpMonth { get; set; }

    [StringLength(2)]
    [DisplayName("Expiration year")]
    [Required]
    public string ExpYear { get; set; }

    [StringLength(3)] [Required] public string CVV { get; set; }
}