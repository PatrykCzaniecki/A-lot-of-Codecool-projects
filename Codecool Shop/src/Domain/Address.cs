using System.ComponentModel.DataAnnotations;

namespace Domain;

public class Address
{
    public int Id { get; set; }

    [Required] public string Street { get; set; } = null!;

    [Required]
    [RegularExpression(@"^\w{2,30}$|^[A-Z]{1}[a-z]{1,30}$|^\w{2,30}\s{1}\w{2,30}")]
    public string City { get; set; } = null!;

    [Required]
    [RegularExpression(@"^\w{2,30}$|^[A-Z]{1}[a-z]{1,30}$|^\w{2,30}\s{1}\w{2,30}")]
    public string Country { get; set; } = null!;

    [Required]
    [RegularExpression(@"^\w{2,30}$|^[A-Z]{1}[a-z]{1,30}$|^\w{2,30}\s{1}\w{2,30}")]
    public string FullName { get; set; } = null!;

    [Required]
    [RegularExpression(
        "\\A(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)\\Z")]
    public string Email { get; set; } = null!;

    [Required]
    [RegularExpression("^[0-9]{3}-[0-9]{3}-[0-9]{3}|[0-9]{9}")]
    public string Phone { get; set; } = null!;

    [Required]
    [RegularExpression(@"^[0-9]{2}-[0-9]{3}$")]
    public string Zip { get; set; } = null!;
}