using System;
using System.Collections.Generic;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Daos.Implementations;

public class OrderDaoMemory : IOrderDao
{
    private static OrderDaoMemory _instance;
    private readonly List<Order> _data = new();
    public Order order;
    public PaymentInfo paymentInfo;

    private OrderDaoMemory()
    {
    }

    public void Add(Order item)
    {
        throw new NotImplementedException();
    }

    public void Remove(int id)
    {
        throw new NotImplementedException();
    }

    public Order Get(int id)
    {
        throw new NotImplementedException();
    }

    public IEnumerable<Order> GetAll()
    {
        throw new NotImplementedException();
    }

    public static OrderDaoMemory GetInstance()
    {
        if (_instance == null) _instance = new OrderDaoMemory();

        return _instance;
    }
}