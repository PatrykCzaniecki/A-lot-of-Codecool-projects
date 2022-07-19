namespace Domain;

public class Product
{
    public int Id { get; set; }
    public string Name { get; set; } = null!;
    public string Currency { get; set; } = null!;
    public string Description { get; set; } = null!;
    public double DefaultPrice { get; set; }
    public Category Category { get; set; } = null!;
    public Supplier Supplier { get; set; } = null!;
}