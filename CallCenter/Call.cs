namespace CallCenter;

public class Call
{
    public Call(Agent agent, DateTime callDate, bool isCallHighPriority)
    {
        CallDate = callDate;
        this.isCallHighPriority = isCallHighPriority;
    }

    public Agent? Agent { get; set; }

    public DateTime CallDate { get; set; }

    public bool wasCallAccepted { get; set; }

    public bool isCallHighPriority { get; set; }

    public void AcceptCall(Agent? agent)
    {
        wasCallAccepted = true;

        if (wasCallAccepted)
        {
            Agent = agent;
            CallDate = new DateTime();
        }
        else
        {
            wasCallAccepted = false;
        }
    }
}