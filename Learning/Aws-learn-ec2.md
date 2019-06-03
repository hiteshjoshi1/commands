# EC2 - Elastic Compute cloud

Pricing philosophy(Not needed for exam)

- Pay as you go and pay for what you use
- Pay less as you use more
- Pay even less when you reserve capacity

## EC2 Pricing Models -

- On Demand
- Reserved
- Spot - Price moves around
- Dedicated Hosts

### On Demand -
Low cost, no upfront fee and no long term commitment
Good for 1st time amazon AWS users
Good for short term, spiky or unpredicatble workloads that cannot be interrupted

### Reserved Pricing -

Used for predictable usage
Upfront payments lead to cheaper pricing

    + Standard Reserved Instances -
    75% cheaper, more you pay upfront, longer the contract, higher the discount.
    You cant convert one reserved instances to other instances.
    
    + Convertible Reserved Instances - 
    You can convert one reserved instances to another.
    
    + Scheduled Reserved Instances -
    Available within the time windows you reserve.
    
### Spot Pricing - Might use this for own websites
AWS selling off its unused inventory.
Applications that have flexible start and end times.
Applications that are only feasible at very low compute prices.

### Dedidicated Host Pricing

Useful for regulatory requirements which do not allow multi tenant virtualization.
Can be purchased ON -Demand or at Reserved Pricing(discounted).

    
