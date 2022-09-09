using Domain;
using Microsoft.EntityFrameworkCore;

namespace Data;

public class CodecoolShopContext : DbContext
{
    public CodecoolShopContext(DbContextOptions options) : base(options)
    {
    }

    public DbSet<Product> Products { get; set; } = null!;
    public DbSet<Category> Categories { get; set; } = null!;
    public DbSet<Supplier> Suppliers { get; set; } = null!;
    public DbSet<Order> Orders { get; set; } = null!;
    public DbSet<PaymentInfo> PaymentInfos { get; set; } = null!;
    public DbSet<OrderedProduct> OrderedProducts { get; set; } = null!;
    public DbSet<Address> Addresses { get; set; } = null!;
}