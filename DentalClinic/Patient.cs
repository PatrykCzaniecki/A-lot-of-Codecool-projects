namespace DentalClinic;

public class Patient
{
    private const int NumOfVisitToBeLoyalClient = 3;

    public Patient(string id, string name)
    {
        Id = id;
        Name = name;
    }

    public string Id { get; set; }

    public string Name { get; set; }

    public bool IsLoyalCustomer { get; private set; }

    protected List<Visit> listOfVisit { get; set; } = new();

    public void AddVisitToList(Visit visit)
    {
        listOfVisit.Add(visit);
    }

    public void PatientIsLoyalCustomer()
    {
        var today = DateTime.Now;
        var thirtyDaysEarlier = today.AddDays(-30);
        var listIfIsLoyal = new List<Visit>();

        foreach (var visit in listOfVisit)
            if (visit.DateTime < thirtyDaysEarlier)
                listIfIsLoyal.Add(visit);

        if (listIfIsLoyal.Count > NumOfVisitToBeLoyalClient)
        {
            IsLoyalCustomer = true;
            Console.WriteLine($"Patient {Name} now is loyal customer.");
        }
        else
        {
            Console.WriteLine($"Patient {Name} is not a loyal customer.");
        }
    }
}