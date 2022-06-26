namespace AirlineManagement;

public class Pilot : Employee
{
    public Pilot(string name, DateOnly birthDate) : base(name, birthDate)
    {
    }

    public bool HasAnalogCompass { get; private set; }

    public void GivePilotAnalogCompass()
    {
        HasAnalogCompass = true;
    }
}