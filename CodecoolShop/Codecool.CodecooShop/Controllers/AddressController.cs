using System;
using System.Linq;
using Codecool.CodecoolShop.Areas.Identity.Data;
using Data;
using Domain;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace Codecool.CodecoolShop.Controllers;

public class AddressController : Controller
{
    private readonly CodecoolShopContext _context;
    private readonly ILogger<AddressController> _logger;
    private readonly UserManager<CodecoolCodecoolShopUser> _userManager;

    public AddressController(ILogger<AddressController> logger, CodecoolShopContext context,
        UserManager<CodecoolCodecoolShopUser> userManager)
    {
        _logger = logger;
        _context = context;
        _userManager = userManager;
    }

    public IActionResult Index()
    {
        if (User.Identity.IsAuthenticated && CartIsNotEmpty())
        {
            _logger.LogInformation($"Address page viewed on {DateTime.Now}");
            return View();
        }

        _logger.LogInformation($"Address page tried to view on {DateTime.Now}");
        return RedirectToAction("Index", "Product");
    }

    [HttpPost]
    [AcceptVerbs]
    public IActionResult Index(Address addressGet)
    {
        _logger.LogInformation($"{DateTime.Now} Action Controller HttpPost executed");
        if (User.Identity.IsAuthenticated)
        {
            _logger.LogInformation($"{DateTime.Now} User Identity Authenticated.");
            if (!ModelState.IsValid)
            {
                _logger.LogInformation($" {DateTime.Now} Modelstate in address is not valid.");
                return View();
            }

            if (User.Identity.IsAuthenticated && CartIsNotEmpty())
            {
                _logger.LogInformation(
                    $" {DateTime.Now} adding address information into DB. Cart verified/ is not empty.");
                var userId = _userManager.GetUserId(User);
                var addressId = _context.Orders.Where(o => o.User_id == userId && o.OrderPayed == "No")
                    .Select(o => o.Address.Id).First();
                var address = _context.Addresses.First(a => a.Id == addressId);
                address.Phone = addressGet.Phone;
                address.City = addressGet.City;
                address.Country = addressGet.Country;
                address.Email = addressGet.Email;
                address.FullName = addressGet.FullName;
                address.Street = addressGet.Street;
                address.Zip = addressGet.Zip;
                _context.SaveChanges();
            }

            return RedirectToAction("Index", "Payment");
        }

        return RedirectToAction("Index", "Product");
    }

    public IActionResult Submit(IFormCollection collection)
    {
        _logger.LogInformation($"{DateTime.Now} User pressed submit on Address page.");
        return View("Index");
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        _logger.LogInformation($"Error on: {DateTime.Now}");
        return RedirectToAction("Index", "Product");
    }

    private bool CartIsNotEmpty()
    {
        var userId = _userManager.GetUserId(User);
        var cart = _context.OrderedProducts
            .Include(p => p.Order)
            .Any(p => p.Order.User_id == userId && p.Order.OrderPayed == "No");

        return cart;
    }
}