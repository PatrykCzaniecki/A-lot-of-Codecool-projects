using System;
using System.Collections.Generic;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Daos.Implementations;

public class CartDaoMemory : ICartDao
{
    private static CartDaoMemory instance;
    private readonly ProductDaoMemory productDaoMemory = ProductDaoMemory.GetInstance();
    public Cart cart = new();

    private CartDaoMemory()
    {
    }

    public void Add(Cart item)
    {
        throw new NotImplementedException();
    }

    public void Remove(int id)
    {
        throw new NotImplementedException();
    }

    public Cart Get(int id)
    {
        throw new NotImplementedException();
    }

    public IEnumerable<Cart> GetAll()
    {
        throw new NotImplementedException();
    }

    public void AddProductToCart(int? id)
    {
        if (id != null)
        {
            var product = productDaoMemory.Get((int) id);
            cart.AddProduct(product);
        }
    }

    public void MinusProductFromCart(int? id)
    {
        if (id != null)
        {
            var product = productDaoMemory.Get((int) id);
            cart.MinusProduct(product);
        }
    }

    public void DeleteProductFromCart(int? id)
    {
        if (id != null)
        {
            var product = productDaoMemory.Get((int) id);
            cart.DeleteProduct(product);
        }
    }

    public static CartDaoMemory GetInstance()
    {
        if (instance == null) instance = new CartDaoMemory();

        return instance;
    }
}