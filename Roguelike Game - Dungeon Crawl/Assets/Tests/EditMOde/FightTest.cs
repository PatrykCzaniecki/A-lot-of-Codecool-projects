using NUnit.Framework;

namespace Tests
{
    public class FightTest
    {
        [Test]
        public void ApplyDamage()
        {
            int Damage = 10;
            int Health = 20;
            int Shield = 5;
            Damage -= Shield;
            if (Damage > 0)
            {
                Health -= Damage;
            }
            Assert.AreEqual(Health,15);
        }
    }
}