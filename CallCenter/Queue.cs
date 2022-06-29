namespace CallCenter;

public abstract class Queue
{
    protected Queue(string queueName, List<Call> listOfCallsWaitingToAnswer, List<Agent> listOfAgentsToPickUp)
    {
        QueueName = queueName;
        ListOfCallsWaitingToAnswer = listOfCallsWaitingToAnswer;
        ListOfAgentsToPickUp = listOfAgentsToPickUp;
    }

    public string QueueName { get; set; }

    public List<Call> ListOfCallsWaitingToAnswer { get; set; }

    public List<Agent> ListOfAgentsToPickUp { get; set; }

    public void GetLastCall(Call call)
    {
        var lastCall = ListOfCallsWaitingToAnswer.Max(call => call.CallDate);

        Console.WriteLine($"The last call was: {lastCall}");
    }

    public void AddCallToList(Call call)
    {
        ListOfCallsWaitingToAnswer.Add(call);
    }

    public void RemoveCallFromList(Call call)
    {
        ListOfCallsWaitingToAnswer.Remove(call);
    }
}