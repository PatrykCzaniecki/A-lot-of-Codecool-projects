using System.Collections.Generic;
using Codecool.CodecoolShop.Models;
using Domain;
using Product = Codecool.CodecoolShop.Models.Product;
using Supplier = Codecool.CodecoolShop.Models.Supplier;

namespace Codecool.CodecoolShop.Daos;

public interface IProductDao : IDao<Product>
{
    IEnumerable<Product> GetBy(Supplier supplier);
    IEnumerable<Product> GetBy(ProductCategory productCategory);
    void GetBy(Category productCategory);
}