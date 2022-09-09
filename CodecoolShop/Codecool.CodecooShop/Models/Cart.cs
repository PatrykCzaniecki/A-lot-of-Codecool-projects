using System.Collections.Generic;
using System.Linq;

namespace Codecool.CodecoolShop.Models;

public class Cart : BaseModel
{
    public Cart()
    {
        Products = new Dictionary<Product, int>();
    }

    public Dictionary<Product, int> Products { get; set; }

    private bool IsProductInCart(Product product)
    {
        var results = Products.Where(p => p.Key.Id == product.Id).Select(p => p.Key);
        if (results.Any()) return true;

        return false;
    }

    public void AddProduct(Product product)
    {
        if (IsProductInCart(product))
        {
            product.CartQuantity += 1;
            Products[product] += 1;
        }
        else
        {
            product.IsInCart = true;
            product.CartQuantity = 1;
            Products.Add(product, 1);
        }
    }

    public void MinusProduct(Product product)
    {
        if (IsProductInCart(product))
        {
            if (Products[product] == 1)
            {
                product.CartQuantity = 0;
                product.IsInCart = false;
                Products.Remove(product);
            }
            else
            {
                product.CartQuantity -= 1;
                Products[product] -= 1;
            }
        }
    }

    public void DeleteProduct(Product product)
    {
        if (IsProductInCart(product))
        {
            product.CartQuantity = 0;
            product.IsInCart = false;
            Products.Remove(product);
        }
    }

    public int TotalProducts()
    {
        return Products.Sum(p => p.Value);
    }

    public int TotalPrice()
    {
        return (int) Products.Sum(p => p.Key.DefaultPrice * p.Value);
    }
}