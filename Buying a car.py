'''A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. 
He wants to keep his old car until he can buy the secondhand one.
He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. 
Furthermore this percent of loss increases of 0.5 percent at the end of every two months. 
Our man finds it difficult to make all these calculations.
How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?'''

def nbMonths(priceold, pricenew, savingperMonth, percentloss):
    month = 0
    saving = 0           
    
    while pricenew > saving + priceold:
        if priceold >= pricenew:
            break       
        month += 1     
        if month % 2 == 0 and month != 0:
            percentloss += 0.5       
        pricenew -= (pricenew * percentloss) / 100
        priceold -= (priceold * percentloss) / 100
        saving += savingperMonth
        
    leftover = priceold - pricenew + saving
    
    return [month, round(leftover, 0)]