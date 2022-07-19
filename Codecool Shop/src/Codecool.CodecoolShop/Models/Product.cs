namespace Codecool.CodecoolShop.Models;

public class Product : BaseModel
{
    public string Currency { get; set; }
    public decimal DefaultPrice { get; set; }
    public ProductCategory ProductCategory { get; set; }
    public Supplier Supplier { get; set; }

    public bool IsInCart { get; set; } = false;
    public int CartQuantity { get; set; }

    public void SetProductCategory(ProductCategory productCategory)
    {
        ProductCategory = productCategory;
        ProductCategory.Products.Add(this);
    }
}