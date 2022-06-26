using AirlineManagement;

namespace AirlineManagement;

public class Flight
{
    private const int NumberOfAttendance = 3;

    private readonly List<Attendance> listOfAttendances = new();

    private Pilot? _captain;

    private Pilot? _secondPilot;

    public Flight(string id, Language language)
    {
        FlightId = id;
        FlightLanguage = language;
    }

    public string FlightId { get; }

    public Language FlightLanguage { get; }

    public void AddCaptain(Pilot captain)
    {
        _captain = captain;
    }

    public void AddSecondPilot(Pilot secondPilot)
    {
        _secondPilot = secondPilot;
    }

    public void AddAttendance(Attendance attendance)
    {
        listOfAttendances.Add(attendance);
    }

    public bool IsReadyToTakeOff()
    {
        var completeCrew = CompleteCrew();
        var allPilotsHaveCompass = AllPilotsHaveCompass();
        var allAttendancesSpeakInFlightsLanguage = AllAttendancesSpeakInFlightsLanguage();

        return completeCrew && allPilotsHaveCompass && allAttendancesSpeakInFlightsLanguage;
    }

    private bool CompleteCrew()
    {
        var result = true;

        if (_captain is null)
        {
            Console.WriteLine("We need Captain to take off");
            result = false;
        }

        if (_secondPilot is null)
        {
            Console.WriteLine("We need SecondPilot to take off");
            result = false;
        }

        if (listOfAttendances.Count() == NumberOfAttendance)
        {
            return result;
        }

        Console.WriteLine(
            $"We need {NumberOfAttendance} attendances to take off but now we got {listOfAttendances.Count}!");
        result = false;

        return result;
    }

    private bool AllPilotsHaveCompass()
    {
        var result = true;

        if (_captain is not null && !_captain.HasAnalogCompass)
        {
            Console.WriteLine("Captain must have analog compass to take off");
            result = false;
        }

        if (_secondPilot is not null && !_secondPilot.HasAnalogCompass)
        {
            Console.WriteLine("SecondPilot must have analog compass to take off");
            result = false;
        }

        return result;
    }

    private bool AllAttendancesSpeakInFlightsLanguage()
    {
        var result = true;

        foreach (var flightAttendant in GetFlightAttendantsWithoutNeededLanguage())
        {
            Console.WriteLine($"Flight attendant \"{flightAttendant}\" must know language \"{FlightLanguage}\"!");
            result = false;
        }

        return result;
    }

    private IEnumerable<Attendance> GetFlightAttendantsWithoutNeededLanguage()
    {
        return listOfAttendances.Where(flightAttendant => !flightAttendant.KnowsLanguage(FlightLanguage));
    }
}