using System.Security.Claims;
using System.Security.Principal;

namespace Codecool.CodecoolShop.Areas.Identity.Extension;

public static class IdentityExtension
{
    public static string GetFullName(this IIdentity identity)
    {
        if (identity == null)
            return null;

        var fullName = (identity as ClaimsIdentity).FirstOrNull("FirstName");
        fullName += " ";
        fullName += (identity as ClaimsIdentity).FirstOrNull("LastName");

        return fullName;
    }

    internal static string FirstOrNull(this ClaimsIdentity identity, string claimType)
    {
        var val = identity.FindFirst(claimType);

        return val == null ? null : val.Value;
    }
}