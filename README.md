
# **Database Migration Pipeline**

This is a repo for compling and installing Python from scratch.

## **Business Context**



## **Design Decisions**

| Design                                                             | Rationale                                                                           |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|

## **Architecture**

## **Tech Stack**

|Tool          | Purpose                  |
|--------------|--------------------------|
| Docker       | Run SQL Server on macOS  |
| Python       | Pipeline orchestration   |
| SQL Server   | Source database          |
| PostgreSQL   | Target database          |

## **How to Run**

## **Source Database**

**AdventureWorks2025** is Microsoft's official **OLTP sample database**, modelling a fictional manufacturing and sales company — AdventureWorks Cycles. The database is designed for high-concurrency business operations, using a normalized relational schema typical of operational databases to support daily transactions. 

It models real-world e-commerce workloads, including the management of customers, products, categories, and suppliers. This structure is ideal for testing migrations that require strict referential integrity and transactional accuracy

Database can be downloaded [here](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms).
