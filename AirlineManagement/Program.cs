using AirlineManagement;

namespace AirlineManagement;

internal class Program
{
    public static void Main(string[] args)
    {
        var flight = new Flight("1", Language.Russian);
        var captain = new Pilot("Bob", DateOnly.Parse("1990-01-01"));
        flight.AddCaptain(captain);
        Status(flight);

        captain.GivePilotAnalogCompass();

        var secondPilot = new Pilot("Gorge", DateOnly.Parse("1879-09-21"));
        secondPilot.GivePilotAnalogCompass();
        flight.AddSecondPilot(secondPilot);

        Status(flight);

        var attendance1 = new Attendance("Lola1", DateOnly.Parse("1994-12-31"));
        attendance1.AddLanguage(Language.Russian);
        flight.AddAttendance(attendance1);
        Status(flight);

        var attendance2 = new Attendance("Lola2", DateOnly.Parse("1994-12-31"));
        attendance2.AddLanguage(Language.Russian);
        flight.AddAttendance(attendance2);
        Status(flight);

        var attendance3 = new Attendance("Lola3", DateOnly.Parse("1994-12-31"));
        attendance3.AddLanguage(Language.German);
        flight.AddAttendance(attendance3);
        Status(flight);

        attendance3.AddLanguage(Language.Russian);
        Status(flight);
    }

    public static void Status(Flight flight)
    {
        Console.WriteLine(flight.IsReadyToTakeOff() ? "Take off" : "Not yet");
    }
}