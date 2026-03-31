
# **Database Migration Pipeline**

This is a repo for compling and installing Python from scratch.

## **I. Project Framming and Success Criteria** 

### **Business Objectives and Context**

Organizations running SQL Server face increasing licensing pressure as they scale. PostgreSQL offers a production-grade, open-source alternative with native compatibility on AWS RDS and Azure Database, with the advantage of eliminating per-core licensing costs while maintaining ACID compliance and relational integrity. 


### **Source Database**

**AdventureWorks2025** is Microsoft's official **OLTP sample database**, modelling a fictional manufacturing and sales company — AdventureWorks Cycles. The database is designed for high-concurrency business operations, using a normalized relational schema typical of operational databases to support daily transactions. 

It models real-world e-commerce workloads, including the management of customers, products, categories, and suppliers. This structure is ideal for testing migrations that require strict referential integrity and transactional accuracy

Database can be downloaded [here](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms).


### **Project Framming**
**Migration Classification:** 
| Dimension | Details |
|---|---|
| Type | Heterogeneous — SQL Server → PostgreSQL |
| Approach | Big Bang — 71 tables in single operation |
| Scope | Application-specific — single OLTP database |
| Environment | UAT — SQL Server local running on Docker + PostgreSQL |
| Production target | AWS RDS PostgreSQL or Azure Database |


**UAT Objective:** 

This pipelione executes in a UAT environment that mirrors production. Source: SQL Server in Docker. Target: PostgreSQL via Homebrew. Once UAT is approved, the same scripts execute against production credentials. Only the environment variables in .env file need to be updated. 

### **Success Criteria**
| Criterion | Target | Result |
|---|---|---|
| Row count match | 71/71 tables |  |
| FK constraints | 91/91 | |
| Check constraints | 89/89 |  |
| PK constraints | All tables | |
| NOT NULL constraints | All columns |  |
| Data loss | Zero |  |


## **II.Tech Stack and Environment Setup**

### **Tech Stack**

|Tool          | Purpose                  |
|--------------|--------------------------|
| Docker       | Run SQL Server on macOS  |
| Python       | Pipeline orchestration   |
| SQL Server   | Source database          |
| PostgreSQL   | Target database          |

### **Security**

### **Environment:** 
This notebook executes in a UAT environment — source data runs on SQL Server in Docker, target database is PostgreSQL running locally via Homebrew. The UAT environment mirrors a production migration scenario where the target would be PostgreSQL on AWS RDS or Azure Database for PostgreSQL.

## **How to Run**
[SQL Server — AdventureWorks2025 OLTP]
         ↓  Schema Exploration (sys.tables, sys.columns, 
         |  sys.foreign_keys, sys.primary_keys)




## **III. Assessment and Planning**

### **Architecture**



### **Design Decisions**

| Design                                                             | Rationale                                                                           |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|



### **Pre-migration Audit and ERD**




## **IV. Execution (The ETL Pipeline)**








## **V. Validation and Reporting**


### **Technical Validation**

### **Visualization**


## **VI: Migration Retrospective amd Future Roadmap**

