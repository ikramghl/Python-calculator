# Interview Questions and Answers

1. **What is normalization?**  
   Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It typically involves dividing large tables into smaller, related ones.

2. **Explain primary key vs foreign key.**  
   - **Primary key**: A column (or set of columns) that uniquely identifies each record in a table.  
   - **Foreign key**: A column in one table that refers to the primary key in another table, establishing a relationship between the two tables.

3. **What are constraints?**  
   Constraints are rules enforced on data columns to ensure data integrity. Examples include `NOT NULL`, `UNIQUE`, `CHECK`, and `FOREIGN KEY`.

4. **What is a surrogate key?**  
   A surrogate key is an artificial, usually numeric, identifier used as a primary key when no natural unique key exists in the data.

5. **How do you avoid data redundancy?**  
   By normalizing the database, using primary and foreign keys, and avoiding storing the same data in multiple places.

6. **What is an ER diagram?**  
   An Entity-Relationship (ER) diagram is a visual representation of database entities, their attributes, and the relationships between them.

7. **What are the types of relationships in DBMS?**  
   - One-to-One  
   - One-to-Many  
   - Many-to-Many

8. **Explain the purpose of `AUTO_INCREMENT`.**  
   `AUTO_INCREMENT` automatically generates a unique number for a column (usually a primary key) whenever a new record is inserted.

9. **What is the default storage engine in MySQL?**  
   The default storage engine is **InnoDB**, which supports transactions and foreign keys.

10. **What is a composite key?**  
    A composite key is a primary key made up of two or more columns combined to uniquely identify a record.

