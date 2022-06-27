namespace DentalClinic;

public class Visit
{
    public Visit(Patient patient, string description, DateTime dateTime, bool wasToothInvolved, TypeOfVisit typeOfVisit,
        List<DentalStuff> listOfDentalStuffs)
    {
        Patient = patient;
        Description = description;
        DateTime = dateTime;
        WasToothInvolved = wasToothInvolved;
        this.typeOfVisit = typeOfVisit;
        ListOfDentalStuffs = listOfDentalStuffs;
    }

    public Patient Patient { get; }

    public string Description { get; }

    public DateTime DateTime { get; }

    public bool WasToothInvolved { get; }

    public TypeOfVisit typeOfVisit { get; }

    public List<DentalStuff> ListOfDentalStuffs { get; set; }
}