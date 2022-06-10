using DungeonCrawl;
using NUnit.Framework;

namespace Tests
{
    public class VectorTest
    {
        [Test]
        public void Press_W_to_go_up()
        {
            Assert.AreEqual((0,1),Utilities.ToVector(Direction.Up));
        }
        [Test]
        public void Press_S_to_go_down()
        {
            Assert.AreEqual((0,-1),Utilities.ToVector(Direction.Down));
        }
        [Test]
        public void Press_A_to_go_Left()
        {
            Assert.AreEqual((-1,0),Utilities.ToVector(Direction.Left));
        }
        [Test]
        public void Press_D_to_go_Right()
        {
            Assert.AreEqual((1,0),Utilities.ToVector(Direction.Right));
        }
    }
}