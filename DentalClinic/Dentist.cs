namespace DentalClinic;

public class Dentist : DentalStuff
{
    public Dentist(string name, string specialization) : base(name, specialization)
    {
    }

    private Dictionary<Visit, Patient> patientsWithVisit { get; } = new();

    private List<string> ProceduresLastWeek { get; } = new();

    private List<string> ProceduresLastMonth { get; } = new();

    public override string ToString()
    {
        return $"I am Name: {Name}, Specialization: {Specialization}";
    }

    public void AddVisitAndPatientToHistory(Visit visit, Patient patient)
    {
        patientsWithVisit.Add(visit, patient);
    }

    public void MakeReportVisitLastWeek(Patient patient)
    {
        var today = DateTime.Now;
        var sevenDaysEarlier = today.AddDays(-7);

        foreach (var visit in patientsWithVisit)
            if (patientsWithVisit.ContainsValue(patient) && visit.Key.DateTime < sevenDaysEarlier)
                ProceduresLastWeek.Add(visit.Key.typeOfVisit.ToString());

        PrintReport("week");
    }

    public void MakeReportVisitLastMonth(Patient patient)
    {
        var today = DateTime.Now;
        var monthDaysEarlier = today.AddDays(-30);

        foreach (var visit in patientsWithVisit)
            if (patientsWithVisit.ContainsValue(patient) && visit.Key.DateTime < monthDaysEarlier)
                ProceduresLastMonth.Add(visit.Key.typeOfVisit.ToString());

        PrintReport("month");
    }

    private void PrintReport(string keyword)
    {
        if (keyword == "week")
            foreach (var item in ProceduresLastWeek)
                Console.WriteLine($"{item}");

        if (keyword == "month")
            foreach (var item in ProceduresLastMonth)
                Console.WriteLine($"{item}");
    }
}