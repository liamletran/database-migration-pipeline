
# **Database Migration Pipeline**

This is a repo for compling and installing Python from scratch.

## **I. Project Framming and Success Criteria** 

### **Business Objectives and Context**
Business Problem: Tại sao lại di trú? (Tiết kiệm chi phí bản quyền SQL Server, chuyển sang hệ sinh thái AWS/PostgreSQL)
công ty muốn chuyển sang hệ sinh thái AWS (AWS ecosystem) vì hai lý do chính:
Chi phí bản quyền (Licensing Costs): SQL Server có chi phí bản quyền rất đắt đỏ, đặc biệt là khi doanh nghiệp mở rộng quy mô
. Trong khi đó, PostgreSQL là mã nguồn mở, giúp công ty cắt giảm đáng kể chi phí này
.
Sự hỗ trợ và tương thích: PostgreSQL được hỗ trợ tốt hơn và vận hành mượt mà hơn trong hệ sinh thái của AWS so với SQL Server


### **Source Database**

**AdventureWorks2025** is Microsoft's official **OLTP sample database**, modelling a fictional manufacturing and sales company — AdventureWorks Cycles. The database is designed for high-concurrency business operations, using a normalized relational schema typical of operational databases to support daily transactions. 

It models real-world e-commerce workloads, including the management of customers, products, categories, and suppliers. This structure is ideal for testing migrations that require strict referential integrity and transactional accuracy

Database can be downloaded [here](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver17&tabs=ssms).


### **Project Framming**
**Migration Classification:** 
- Type: Heterogeneous migration (SQL Server → PostgreSQL)
- Approach: Big Bang — all 71 tables migrated in single operation
- Scope: Application-specific — single OLTP database


### **Success Criteria**
- Success Criteria: Zero Data Loss, all row counts match 100%, zero data integrity errors.

- Migration Type: This is a heterogeneous migration from SQL Server to PostgreSQL and Cloud Migration

**UAT Objective:** 
Validate zero data loss and full constraint preservation before promoting the pipeline to production. 
Once UAT is approved, the same Python scripts can be executed against production credentials with no code changes — only environment variables in .env need to be updated.



## **II.Environment Setup and Security**

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

