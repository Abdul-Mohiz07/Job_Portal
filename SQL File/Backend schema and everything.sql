CREATE TABLE "User" (
    email VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age > 0),
    gender VARCHAR(10),
    password VARCHAR(100) NOT NULL
);

INSERT INTO "User" (email, name, age, gender, password) VALUES
('ahmed@gmail.com', 'Ahmed Raza', 24, 'Male', 'pass123'),
('sara@gmail.com', 'Sara Khan', 22, 'Female', 'secure456'),
('mohiz@gmail.com', 'Abdul Mohiz', 21, 'Male', 'mechaline789');

CREATE TABLE Company (
    comp_id SERIAL PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(150),
    industry VARCHAR(50)
);

INSERT INTO Company (company_name, phone, address, industry) VALUES
('TechNova', '0301-1112233', 'Lahore, Pakistan', 'IT'),
('AutoWorks', '0322-4445566', 'Karachi, Pakistan', 'Automobile'),
('HealthCare Plus', '0315-9998887', 'Islamabad, Pakistan', 'Healthcare');

CREATE TABLE Job (
    job_id SERIAL PRIMARY KEY,
    comp_id INT NOT NULL,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(100),
    salary INT CHECK (salary >= 0),
    start_date DATE,
    end_date DATE,
    CONSTRAINT fk_job_company FOREIGN KEY (comp_id)
        REFERENCES Company (comp_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Job (comp_id, title, description, location, salary, start_date, end_date) VALUES
(1, 'Data Analyst', 'Analyze company data and create reports.', 'Lahore', 90000, '2025-11-01', '2026-01-30'),
(2, 'Auto Engineer', 'Responsible for car diagnostics and maintenance.', 'Karachi', 120000, '2025-12-10', '2026-02-10'),
(3, 'Nurse', 'Assist doctors in patient care.', 'Islamabad', 80000, '2025-11-05', '2026-03-05');

CREATE TABLE Skill (
    skill_id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO Skill (skill_name) VALUES
('Python'),
('Auto Mechanics'),
('Patient Care');

CREATE TABLE Application (
    app_id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    job_id INT NOT NULL,
    applied_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(50) CHECK (status IN ('Pending', 'Accepted', 'Rejected')),
    CONSTRAINT fk_application_user FOREIGN KEY (email)
        REFERENCES "User" (email)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_application_job FOREIGN KEY (job_id)
        REFERENCES Job (job_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Application (email, job_id, applied_date, status) VALUES
('ahmed@gmail.com', 1, '2025-10-20', 'Pending'),
('sara@gmail.com', 2, '2025-10-21', 'Accepted'),
('mohiz@gmail.com', 3, '2025-10-22', 'Rejected');

CREATE TABLE User_Skill (
    user_skill_id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    skill_id INT NOT NULL,
    proficiency_level VARCHAR(50)
        CHECK (proficiency_level IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')),
    CONSTRAINT fk_user_skill_user FOREIGN KEY (email)
        REFERENCES "User" (email)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_user_skill_skill FOREIGN KEY (skill_id)
        REFERENCES Skill (skill_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT uq_user_skill UNIQUE (email, skill_id)
);

INSERT INTO User_Skill (email, skill_id, proficiency_level) VALUES
('ahmed@gmail.com', 1, 'Advanced'),
('sara@gmail.com', 2, 'Intermediate'),
('mohiz@gmail.com', 1, 'Expert');

CREATE TABLE Job_Skill (
    job_skill_id SERIAL PRIMARY KEY,
    job_id INT NOT NULL,
    skill_id INT NOT NULL,
    importance_level VARCHAR(50)
        CHECK (importance_level IN ('Low', 'Medium', 'High')),
    CONSTRAINT fk_job_skill_job FOREIGN KEY (job_id)
        REFERENCES Job (job_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_job_skill_skill FOREIGN KEY (skill_id)
        REFERENCES Skill (skill_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT uq_job_skill UNIQUE (job_id, skill_id)
);

INSERT INTO Job_Skill (job_id, skill_id, importance_level) VALUES
(1, 1, 'High'),
(2, 2, 'High'),
(3, 3, 'Medium');


--- Updation queries
ALTER TABLE User    
RENAME COLUMN email to EEmail;

ALTER TABLE User    
ALTER COLUMN EMAIL TYPE ----;

ALTER TABLE User
RENAME TO members;
