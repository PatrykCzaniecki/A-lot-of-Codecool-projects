using System.Collections.Generic;
using System.IO;
using Domain;
using Newtonsoft.Json;

namespace Codecool.CodecoolShop.JSON;

public static class JsonFile
{
    public static void SaveToJsonFile(Order order, List<OrderedProduct> products)
    {
        var serializer = new JsonSerializer();
        serializer.NullValueHandling = NullValueHandling.Ignore;

        var jsonOrder = new JsonOrder
        {
            order = order,
            products = products
        };

        using (var sw = new StreamWriter($"../Order{order.Id}.txt"))
        using (JsonWriter writer = new JsonTextWriter(sw))
        {
            serializer.Serialize(writer, jsonOrder);
        }
    }
}

public class JsonOrder
{
    public Order order { get; set; }
    public List<OrderedProduct> products { get; set; }
}