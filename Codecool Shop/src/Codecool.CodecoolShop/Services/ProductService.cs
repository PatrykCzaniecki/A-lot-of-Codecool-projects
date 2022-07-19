using System.Collections.Generic;
using Codecool.CodecoolShop.Daos;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Services;

public class ProductService
{
    private readonly IProductCategoryDao productCategoryDao;
    private readonly IProductDao productDao;
    private readonly ISupplierDao supplierDao;

    public ProductService(IProductDao productDao, IProductCategoryDao productCategoryDao, ISupplierDao supplierDao)
    {
        this.productDao = productDao;
        this.supplierDao = supplierDao;
        this.productCategoryDao = productCategoryDao;
    }

    public ProductCategory GetProductCategory(int categoryId)
    {
        return productCategoryDao.Get(categoryId);
    }

    public IEnumerable<Product> GetProductsForCategory(int categoryId)
    {
        var category = productCategoryDao.Get(categoryId);
        return productDao.GetBy(category);
    }

    public Supplier GetProductSupplier(int supplierId)
    {
        return supplierDao.Get(supplierId);
    }

    public IEnumerable<Product> GetProductsForSupplier(int supplierId)
    {
        var supplier = supplierDao.Get(supplierId);
        return productDao.GetBy(supplier);
    }

    public IEnumerable<Product> GetAllProducts()
    {
        return productDao.GetAll();
    }
}