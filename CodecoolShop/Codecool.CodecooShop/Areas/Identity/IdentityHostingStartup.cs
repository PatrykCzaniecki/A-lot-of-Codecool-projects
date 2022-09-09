using Codecool.CodecoolShop.Areas.Identity;
using Codecool.CodecoolShop.Areas.Identity.Data;
using Codecool.CodecoolShop.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

[assembly: HostingStartup(typeof(IdentityHostingStartup))]

namespace Codecool.CodecoolShop.Areas.Identity;

public class IdentityHostingStartup : IHostingStartup
{
    public void Configure(IWebHostBuilder builder)
    {
        builder.ConfigureServices((context, services) =>
        {
            services.AddDbContext<CodecoolCodecoolShopContext>(options =>
                options.UseSqlServer(
                    context.Configuration.GetConnectionString("CodecoolCodecoolShopContextConnection")));

            services.AddDefaultIdentity<CodecoolCodecoolShopUser>(
                    options =>
                    {
                        options.SignIn.RequireConfirmedAccount = false;
                        options.Password.RequireLowercase = false;
                        options.Password.RequireUppercase = false;
                    })
                .AddEntityFrameworkStores<CodecoolCodecoolShopContext>();
        });
    }
}