using System;
using System.Collections.Generic;
using System.Linq;
using Codecool.CodecoolShop.Models;
using Domain;
using Product = Codecool.CodecoolShop.Models.Product;
using Supplier = Codecool.CodecoolShop.Models.Supplier;

namespace Codecool.CodecoolShop.Daos.Implementations;

public class ProductDaoMemory : IProductDao
{
    private static ProductDaoMemory instance;
    private readonly List<Product> data = new();

    private ProductDaoMemory()
    {
    }

    public void Add(Product item)
    {
        item.Id = data.Count + 1;
        data.Add(item);
    }

    public void Remove(int id)
    {
        data.Remove(Get(id));
    }

    public Product Get(int id)
    {
        return data.Find(x => x.Id == id);
    }

    public IEnumerable<Product> GetAll()
    {
        return data;
    }

    public IEnumerable<Product> GetBy(Supplier supplier)
    {
        return data.Where(x => x.Supplier.Id == supplier.Id);
    }

    public IEnumerable<Product> GetBy(ProductCategory productCategory)
    {
        return data.Where(x => x.ProductCategory.Id == productCategory.Id);
    }

    public void GetBy(Category productCategory)
    {
        throw new NotImplementedException();
    }

    public void Clear()
    {
        foreach (var product in data)
        {
            product.IsInCart = false;
            product.CartQuantity = 0;
        }
    }

    public static ProductDaoMemory GetInstance()
    {
        if (instance == null) instance = new ProductDaoMemory();

        return instance;
    }
}