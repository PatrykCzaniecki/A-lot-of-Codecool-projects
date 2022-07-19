namespace Domain;

public class OrderedProduct
{
    public int Id { get; set; }
    public string Name { get; set; } = null!;
    public string Currency { get; set; } = null!;
    public double Price { get; set; }
    public Order Order { get; set; } = null!;
    public int ProductId { get; set; }
    public int Quantity { get; set; }
}