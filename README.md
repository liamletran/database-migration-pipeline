
# **Database Migration Pipeline**

This is a heterogeneous Big Bang migration of an application-specific OLTP database, following a UAT-first approach before production promotion to AWS RDS PostgreSQL.

## **A. Project Framming and Success Criteria** 

### **1. Business Objectives and Context**

Organizations running SQL Server reporting queries performance on the legacy system are slowing down due to scaling, and a more flexible platform is needed. Additionally, they face increasing licensing pressure as they scale. PostgreSQL offers a production-grade, open-source alternative with native compatibility on AWS RDS and Azure Database, with the advantage of eliminating per-core licensing costs while maintaining ACID compliance and relational integrity.  


### **2. Source Database**

**AdventureWorks2025** 

It is a Microsoft's official OLTP sample database, modelling a fictional manufacturing and sales company — AdventureWorks Cycles. The database is designed for high-concurrency business operations, using a normalized relational schema typical of operational databases to support daily transactions. 

It models real-world e-commerce workloads, including the management of customers, products, categories, and suppliers. This structure is ideal for testing migrations that require strict referential integrity and transactional accuracy.

**Specifications**

| Specification     | Details       |
|-------------------|---------------|
| Number of Tables  | 71 tables     |
| Number of Rows    | 760,167 rows  |
| Views             | 20 views      |
| Stored Procedures | 10 procedures |
| Functions         | 11 functions  |


**ERD**

**Technical Complexity**
This database presents challenging migration scenarios due to its use of complex data types and structures:

Special Data Types: Including `hierarchyid` for tree structures, `geography` for spatial coordinates, `xml` for demographic and technical information, and unique identifier types `uniqueidentifier`.

Constraints: Extensive use of Foreign Keys, Primary Keys, and Check constraints to preserve business logic.

**Download**

Database can be downloaded [here](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms).



### **3. Migration Strategy and Scalability** 

**Technical Justification**
Due to the relatively small size of this dataset (~5MB, 71 tables, >760k rows), adopting heavyweight enterprise tools like AWS DMS, Talend, or Informatica is not cost-effective. Furthermore, this heterogeneous migration poses unique challenges—such as mapping specialized SQL Server data types (e.g., `hierarchyid`, `geography`) and complex Composite Foreign Keys—that require the granular control offered by custom Python and SQL scripts to ensure Zero Data Loss.

**Approach Selection**
We implement a Big Bang migration strategy, executing the transfer in a single operation. This approach is faster for our current data volume but inherently riskier as issues can impact the entire system. To mitigate this, the pipeline is built and validated in a UAT (sandbox) environment before any production cutover.

**Enterprise Scalability**
For enterprise data volumes exceeding the hundreds of Gigabytes (GB) range, or when real-time synchronization is required, tools like AWS DMS with CDC (Change Data Capture) capability are recommended. In such cases, Trickle migrations (phased approach) would be used to allow for parallel operation and testing, significantly reducing risk and downtime.

When data reaches tens or hundreds of Terabytes (TB), network bandwidth becomes a physical barrier. At this scale, we would leverage physical data transfer services such as AWS Snowball (80TB of capacity) or Google Transfer Appliance (480TB of capacity) to bypass internet latency and packet loss. 

In the current scenario, we accept a short downtime window. However, for critical systems requiring 24/7 operational continuity, a Parallel Running strategy is essential to ensure the new system performs as expected before the formal cutover.

**Migration Classification Summary**

| Dimension         | Details                                               |
|-------------------|-------------------------------------------------------|
| Type              | Heterogeneous — SQL Server → PostgreSQL               |
| Approach          | Big Bang — 71 tables in single operation              |
| Scope             | Application-specific — single OLTP database           |
| Environment       | UAT — SQL Server local running on Docker + PostgreSQL |
| Production target | AWS RDS PostgreSQL or Azure Database                  |


**UAT Objective** 

This pipelione executes in a UAT environment that mirrors production. Source: SQL Server in Docker. Target: PostgreSQL via Homebrew. Once UAT is approved, the same scripts execute against production credentials. Only the environment variables in .env file need to be updated. 



### **4. Success Criteria**

| Criterion             | Target        | Result |
|-----------------------|---------------|--------|
| Row count match       | 71/71 tables  |        |
| FK constraints        | 91/91         |        |
| Check constraints     | 89/89         |        |
| PK constraints        | All tables    |        |
| NOT NULL constraints  | All columns   |        |
| Data loss             | Zero          |        |








## **B.Tech Stack and Environment Setup**

### **1. Tech Stack**

|Tool          | Purpose                  |
|--------------|--------------------------|
| Docker       | Run SQL Server on macOS  |
| Python       | Pipeline orchestration   |
| SQL Server   | Source database          |
| PostgreSQL   | Target database          |

### **2. Security**

- Credentials stored in `.env` file — never committed to Git
- `.gitignore` configured to exclude `.env` and credential files
- SQLAlchemy parameterized queries used where applicable


### **3. Environment** 
This notebook executes in a UAT environment — source data runs on SQL Server in Docker, target database is PostgreSQL running locally via Homebrew. The UAT environment mirrors a production migration scenario where the target would be PostgreSQL on AWS RDS or Azure Database for PostgreSQL.




## **C. Assessment and Planning**

### **1. Architecture**
```
[SQL Server — AdventureWorks2025 OLTP]
         ↓  Schema Exploration (sys.tables, sys.columns, 
         |  sys.foreign_keys, sys.primary_keys)


```


### **2. Design Decisions**

| Design                                                             | Rationale                                                                           |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|



### **3. Pre-Migration Findings**

| Category          | Issues Found                  | Blocking          |
|-------------------|-------------------------------|-------------------|
| Null checks       | 0                             | No                |
| Orphaned FK       | 0                             | No                |
| Negative values   | 0                             | No                |
| Future dates      | 3 tables (123 rows)           | No                |
| Unsupported types | 6 type categories, 52 columns | Yes — handled     |
| Composite FK      | 1 constraint                  | Partial - handled |










## **D. Execution**


## **E. Validation and Reporting**

| Step              | Result                            |
|-------------------|-----------------------------------|
| Tables migrated   | 71/71                             |
| FK constraints    | 90/91 (89 regular + 1 composite ) |
| Check constraints | 89/89                             |



### **1. Technical Validation**

### **2. Visualization**







## **F. Migration Retrospective amd Future Roadmap**

