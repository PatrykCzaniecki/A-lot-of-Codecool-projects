namespace DentalClinic;

internal class Program
{
    public static void Main(string[] args)
    {
        var dentist = new Dentist("Bob", "doctor");
        var hygienist = new Hygienist("Ala", "helper");
        var tech = new Technician("George", "XRay");

        var patient = new Patient("1", "Patrick");

        var patricksConsultation = new Visit(patient, "My first visit", new DateTime(2022 - 06 - 21), false,
            TypeOfVisit.Consultation, new List<DentalStuff> {dentist});
        patient.AddVisitToList(patricksConsultation);

        var patricksVisit = new Visit(patient, "My second visit", new DateTime(2022 - 06 - 22), true,
            TypeOfVisit.ToothTreatment, new List<DentalStuff> {dentist, hygienist});
        patient.AddVisitToList(patricksVisit);

        var patricksVisit2 = new Visit(patient, "My third visit", new DateTime(2022 - 06 - 23), false,
            TypeOfVisit.Operation, new List<DentalStuff> {dentist, hygienist, tech});
        patient.AddVisitToList(patricksVisit2);

        var patricksVisit3 = new Visit(patient, "My fourth visit", new DateTime(2022 - 06 - 24), false,
            TypeOfVisit.Cleaning, new List<DentalStuff>());
        patricksVisit3.ListOfDentalStuffs.Add(hygienist);
        patient.AddVisitToList(patricksVisit3);

        patient.PatientIsLoyalCustomer();

        dentist.AddVisitAndPatientToHistory(patricksConsultation, patient);
        dentist.AddVisitAndPatientToHistory(patricksVisit, patient);
        dentist.AddVisitAndPatientToHistory(patricksVisit2, patient);
        dentist.AddVisitAndPatientToHistory(patricksVisit3, patient);

        dentist.MakeReportVisitLastWeek(patient);
    }
}