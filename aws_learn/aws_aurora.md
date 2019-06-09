# Aurora DB

- Amazon's own RDS
- Can migrate from MySql and PostgresSql to AuroraDb.
- Start with 10 GB and auto scales in 10 GB increments(upto 64 TB)
- Compute resources can scale 32 vCPU's and 244 Gb of memory.
- 2 copies of your data in each avalability zone with minimum of 3 availability zones.(Has 6 copies)
- Can share Aurora Snapshots with other AWS accounts

### 2 types of Aurora Read replicas -

- Aurora Replicas (Upto 15)
  **Automatic failover is only avaialable with Aurora replicas.**
- MySql read replica(Upto 5)

Backups with Aurora -
Automated backups are enabled, backups do not impact performance.
Also take Snapshots with aurora, do not affect performance.
