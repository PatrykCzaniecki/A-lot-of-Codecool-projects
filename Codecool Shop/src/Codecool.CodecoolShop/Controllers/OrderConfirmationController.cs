using System;
using System.Collections.Generic;
using System.Linq;
using Codecool.CodecoolShop.Areas.Identity.Data;
using Codecool.CodecoolShop.JSON;
using Data;
using Domain;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace Codecool.CodecoolShop.Controllers;

public class ModelOrderConfirmationContainer
{
    public Order order { get; set; }
    public List<OrderedProduct> products { get; set; }
}

public class OrderConfirmationController : Controller
{
    private readonly CodecoolShopContext _context;
    private readonly ILogger<ProductController> _logger;
    private readonly UserManager<CodecoolCodecoolShopUser> _userManager;

    public OrderConfirmationController(ILogger<ProductController> logger, CodecoolShopContext context,
        UserManager<CodecoolCodecoolShopUser> userManager)
    {
        _logger = logger;
        _context = context;
        _userManager = userManager;
    }

    public IActionResult Index()
    {
        _logger.LogInformation($"Order confirmation page viewed on {DateTime.Now}");
        if (User.Identity.IsAuthenticated)
        {
            var userId = _userManager.GetUserId(User);
            var order = _context.Orders
                .Include(o => o.Address)
                .Include(o => o.PaymentInfo)
                .First(o => o.User_id == userId && o.OrderPayed == "No");
            var orderedProducts = _context.OrderedProducts
                .Include(p => p.Order)
                .Where(p => p.Order.User_id == userId && p.Order.OrderPayed == "No")
                .ToList();
            var model = new ModelOrderConfirmationContainer {order = order, products = orderedProducts};
            return View(model);
        }

        return RedirectToAction("Index", "Product");
    }

    [HttpPost]
    public IActionResult Send()
    {
        var userId = _userManager.GetUserId(User);
        var order = _context.Orders
            .Include(o => o.Address)
            .Include(o => o.PaymentInfo)
            .First(o => o.User_id == userId && o.OrderPayed == "No");
        var orderedProducts = _context.OrderedProducts
            .Include(p => p.Order)
            .Where(p => p.Order.User_id == userId && p.Order.OrderPayed == "No")
            .ToList();
        Email.SendEmail(order, orderedProducts);
        JsonFile.SaveToJsonFile(order, orderedProducts);
        order.OrderPayed = "Yes";
        _context.SaveChanges();
        return RedirectToAction("Confirmation");
    }

    public IActionResult Confirmation()
    {
        return View();
    }
}