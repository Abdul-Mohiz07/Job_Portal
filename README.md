# Job Portal Project Report
1. Introduction
This project is a Job Portal Management System developed using PostgreSQL (backend) and
Streamlit (frontend). It allows administrators to manage users, companies, jobs, skills, applications,
and skill associations.
2. Backend (Database Schema)
The PostgreSQL database contains the following tables with ON UPDATE CASCADE and ON
DELETE CASCADE relationships: users(email PK, name, age, gender, password)
company(comp_id PK, company_name, phone, address, industry) job(job_id PK, comp_id
FK→company, title, description, location, salary, start_date, end_date) skill(skill_id PK, skill_name)
application(app_id PK, email FK→users, job_id FK→job, status, applied_date)
user_skill(user_skill_id PK, email FK→users, skill_id FK→skill, proficiency_level)
job_skill(job_skill_id PK, job_id FK→job, skill_id FK→skill, importance_level) These relationships
ensure automatic propagation of updates and deletions across dependent tables.
3. Frontend (Streamlit)
The admin dashboard is built with Streamlit and includes: Dark theme custom layout Sidebar
navigation for table selection Data viewing with pagination limit Form-based insertion for each table
Automatic dropdowns for foreign keys Update and delete record management The frontend
interacts with the PostgreSQL database using psycopg2.
4. Functionality Overview
Add Records: Insert new users, companies, jobs, skills, and associations. Display Records: View
the first 100 entries of any table. Update Records: Edit existing rows with validated form fields.
Delete Records: Delete rows safely using primary key selection. Automatic Rerendering: The
interface refreshes after insert/update/delete.
5. Technologies Used
PostgreSQL – database system psycopg2 – Python PostgreSQL driver Pandas – for DataFrame
handling Streamlit – frontend UI framework Python – primary programming language
6. Conclusion
This project demonstrates a complete end-to-end CRUD-based admin panel with a relational
database backend and a dynamic, interactive frontend. It fully handles foreign key constraints,
provides a clean UI, and ensures data consistency
