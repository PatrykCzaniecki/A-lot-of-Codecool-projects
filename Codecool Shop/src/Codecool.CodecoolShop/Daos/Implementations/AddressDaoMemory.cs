using System;
using System.Collections.Generic;
using Codecool.CodecoolShop.Models;

namespace Codecool.CodecoolShop.Daos.Implementations;

public class AddressDaoMemory : IAddressDao
{
    private static AddressDaoMemory instance;

    public Address adress = new();

    private AddressDaoMemory()
    {
    }

    public void Add(Address item)
    {
        throw new NotImplementedException();
    }

    public void Remove(int id)
    {
        throw new NotImplementedException();
    }

    public Address Get(int id)
    {
        throw new NotImplementedException();
    }

    public IEnumerable<Address> GetAll()
    {
        throw new NotImplementedException();
    }

    public static AddressDaoMemory GetInstance()
    {
        if (instance == null) instance = new AddressDaoMemory();

        return instance;
    }
}