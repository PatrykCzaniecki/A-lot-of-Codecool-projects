using Codecool.CodecoolShop.Daos;
using Codecool.CodecoolShop.Models;
using Codecool.CodecoolShop.Services;
using NSubstitute;

namespace UnitTests;

public class ProductServiceTests
{
    private IProductCategoryDao _categoryDao;
    private IProductDao _productDao;
    private ProductService _productService;
    private ISupplierDao _supplierDao;

    [SetUp]
    public void Setup()
    {
        _categoryDao = Substitute.For<IProductCategoryDao>();
        _supplierDao = Substitute.For<ISupplierDao>();
        _productDao = Substitute.For<IProductDao>();
        _productService = new ProductService(_productDao, _categoryDao, _supplierDao);
    }

    [Test]
    public void GetProductCategory_Test()
    {
        //Arrange

        var category = new ProductCategory {Id = 1, Name = "TestCategory"};
        _categoryDao.Get(category.Id).Returns(category);

        //Act

        var result = _productService.GetProductCategory(1);

        //Assert

        Assert.That(result, Is.EqualTo(category));
    }

    [Test]
    public void GetProductsForCategory_Test()
    {
        //Arrange

        var category = new ProductCategory {Id = 1, Name = "TestCategory"};
        _categoryDao.Get(1).Returns(category);
        IEnumerable<Product> productList = new List<Product>
        {
            new() {Id = 1, Name = "TestProduct1"},
            new() {Id = 2, Name = "TestProduct2"}
        };

        _productDao.GetBy(category).Returns(productList);

        //Act

        var result = _productService.GetProductsForCategory(1);

        //Assert

        Assert.That(result, Is.EqualTo(productList));
    }

    [Test]
    public void GetAllProducts_Test()
    {
        //Arrange

        IEnumerable<Product> productList = new List<Product>
        {
            new() {Id = 1, Name = "TestProduct1"},
            new() {Id = 2, Name = "TestProduct2"}
        };

        _productDao.GetAll().Returns(productList);

        //Act

        var result = _productService.GetAllProducts();

        //Assert

        Assert.That(result, Is.EqualTo(productList));
    }

    [Test]
    public void GetProductsSupplier_Test()
    {
        //Arrange

        var supplier = new Supplier {Id = 1, Name = "TestSupplier"};
        _supplierDao.Get(supplier.Id).Returns(supplier);

        //Act

        var result = _productService.GetProductSupplier(1);

        //Assert

        Assert.That(result, Is.EqualTo(supplier));
    }

    [Test]
    public void GetProductsForSupplier_Test()
    {
        //Arrange

        var supplier = new Supplier {Id = 1, Name = "TestSupplier"};
        _supplierDao.Get(1).Returns(supplier);
        IEnumerable<Product> productList = new List<Product>
        {
            new() {Id = 1, Name = "TestProduct1"},
            new() {Id = 2, Name = "TestProduct2"}
        };

        _productDao.GetBy(supplier).Returns(productList);

        //Act

        var result = _productService.GetProductsForSupplier(1);

        //Assert

        Assert.That(result, Is.EqualTo(productList));
    }
}