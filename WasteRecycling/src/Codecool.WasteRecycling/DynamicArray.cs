namespace Codecool.WasteRecycling;

//Dynamic array for garbage
public class DynamicArray
{
    public DynamicArray()
    {
        _array = new Garbage[1];
        _count = 0;
        _size = 1;
    }

    public Garbage[] _array { get; private set; }
    public int _count { get; private set; }
    public int _size { get; private set; }

    public void Add(Garbage data)
    {
        if (_count == _size) Grow();

        _array[_count] = data;
        _count++;
    }

    public void Clear()
    {
        _array = new Garbage[1];
        _count = 0;
        _size = 1;
    }

    public void Grow()
    {
        Garbage[] TemporaryArray = null;
        if (_count == _size)
        {
            TemporaryArray = new Garbage[_size * 2];
            {
                _array.CopyTo(TemporaryArray, 0);
            }

            _array = TemporaryArray;

            _size = _size * 2;
        }
    }
}
