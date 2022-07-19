using System.ComponentModel.DataAnnotations.Schema;
using Microsoft.AspNetCore.Identity;

namespace Codecool.CodecoolShop.Areas.Identity.Data;

// Add profile data for application users by adding properties to the CodecoolCodecoolShopUser class
public class CodecoolCodecoolShopUser : IdentityUser
{
    [PersonalData]
    [Column(TypeName = "nvarchar(100)")]
    public string FirstName { get; set; }

    [PersonalData]
    [Column(TypeName = "nvarchar(100)")]
    public string LastName { get; set; }
}