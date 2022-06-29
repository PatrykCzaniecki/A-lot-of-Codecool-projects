namespace CallCenter;

public class HighPriorityQueue : Queue
{
    public HighPriorityQueue(string queueName, List<Call> listOfCallsWaitingToAnswer,
        List<Agent> listOfAgentsToPickUp) : base(queueName, listOfCallsWaitingToAnswer, listOfAgentsToPickUp)
    {
    }

    public Agent? Agent { get; set; }

    public void CheckIfIsAgentToPickUpCall(Call call)
    {
        if (Agent is {Seniority: Seniority.Level3})
        {
            ListOfAgentsToPickUp.Add(Agent);
        }
        else
        {
            ListOfCallsWaitingToAnswer.Add(call);
            Console.WriteLine("There is no agent with Level 3 to pick up call!");
        }
    }
}