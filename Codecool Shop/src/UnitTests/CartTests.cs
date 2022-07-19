using Codecool.CodecoolShop.Models;

namespace UnitTests;

public class CartTests
{
    private Cart _cart;

    [SetUp]
    public void Setup()
    {
        _cart = new Cart();
    }

    [Test]
    public void AddProduct_Test()
    {
        //Arrange

        var product1 = new Product {Id = 1, Name = "TestProduct1"};
        _cart.Products.Add(product1, 1);
        var testDictionary = new Dictionary<Product, int> {{product1, 2}};

        //Act

        _cart.AddProduct(product1);

        //Assert

        Assert.That(testDictionary, Is.EqualTo(_cart.Products));
    }

    [Test]
    public void MinusProduct_Test()
    {
        //Arrange

        var product1 = new Product {Id = 1, Name = "TestProduct1"};
        _cart.Products.Add(product1, 2);
        var testDictionary = new Dictionary<Product, int> {{product1, 1}};

        //Act

        _cart.MinusProduct(product1);

        //Assert

        Assert.That(testDictionary, Is.EqualTo(_cart.Products));
    }

    [Test]
    public void DeleteProduct_Test()
    {
        //Arrange

        var product1 = new Product {Id = 1, Name = "TestProduct1"};
        var product2 = new Product {Id = 2, Name = "TestProduct2"};
        _cart.Products.Add(product1, 1);
        _cart.Products.Add(product2, 1);
        var testDictionary = new Dictionary<Product, int> {{product1, 1}};

        //Act

        _cart.DeleteProduct(product2);

        //Assert

        Assert.That(testDictionary, Is.EqualTo(_cart.Products));
    }

    [Test]
    public void TotalProduct_Test()
    {
        //Arrange

        var product1 = new Product {Id = 1, Name = "TestProduct1"};
        _cart.Products.Add(product1, 1);
        var expectedResult = 1;

        //Act

        var productsInCart = _cart.TotalProducts();

        //Assert

        Assert.That(productsInCart, Is.EqualTo(expectedResult));
    }

    [Test]
    public void TotalPrice_Test()
    {
        //Arrange

        var product1 = new Product {Id = 1, Name = "TestProduct1", DefaultPrice = 10};
        var product2 = new Product {Id = 2, Name = "TestProduct2", DefaultPrice = 20};
        _cart.Products.Add(product1, 1);
        _cart.Products.Add(product2, 2);
        var expectedResult = 50;

        //Act

        var totalPrice = _cart.TotalPrice();

        //Assert

        Assert.That(totalPrice, Is.EqualTo(expectedResult));
    }
}