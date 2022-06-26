using AirlineManagement;

namespace AirlineManagement;

public class Attendance : Employee
{
    private readonly HashSet<Language> _languages = new();

    public Attendance(string name, DateOnly birthDate) : base(name, birthDate)
    {
    }

    public void AddLanguage(Language language)
    {
        _languages.Add(language);
    }

    public bool KnowsLanguage(Language language)
    {
        return _languages.Contains(language);
    }
}