namespace CallCenter;

public class NormalQueue : Queue
{
    public NormalQueue(string queueName, List<Call> listOfCallsWaitingToAnswer, List<Agent> listOfAgentsToPickUp) :
        base(queueName, listOfCallsWaitingToAnswer, listOfAgentsToPickUp)
    {
    }

    public Agent? Agent { get; set; }

    public void CheckIfIsAgentToPickUpCall(Call call)
    {
        if (Agent != null)
        {
            ListOfAgentsToPickUp.Add(Agent);
        }
        else
        {
            ListOfCallsWaitingToAnswer.Add(call);
            Console.WriteLine("There is no agent to pick up call!");
        }
    }
}