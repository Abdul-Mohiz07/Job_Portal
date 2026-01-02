import streamlit as st
import psycopg2
import pandas as pd
from datetime import date

#--------------------- PAGE NAME -----------------
st.set_page_config(
    page_title="Job Portal Admin",
    page_icon="favicon.ico",
    layout="wide"
)

# Custom CSS for dark theme
st.markdown("""
<style>
/* Background of the whole app */
.stApp {
    background-color: #000000;  /* black background */
    color: #D3D3D3;             /* gray text */
}

/* Dataframe/table headers and cells */
.stDataFrame th {
    background-color: #1a1a1a;
    color: #D3D3D3;
}
.stDataFrame td {
    background-color: #000000;
    color: #D3D3D3;
}

/* Buttons */
.stButton>button {
    background-color: #333333;  /* dark button */
    color: #D3D3D3;             /* gray text */
    border: 1px solid #555555;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111111;
    color: #D3D3D3;
}
</style>
""", unsafe_allow_html=True)



# ----------------- DB CONNECTION -----------------
def get_connection():
    return psycopg2.connect(
        host="Enter Host Name", 
        port="Enter Port Name",
        database="Enter Db Name",
        user="Enter Username",
        password="Enter Password"  
    )

def fetch_table(table_name):
    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 100;", conn)
    conn.close()
    return df

# ----------------- INSERT FUNCTIONS -----------------
def insert_user(email, name, age, gender, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (email,name,age,gender,password) VALUES (%s,%s,%s,%s,%s)",
        (email,name,age,gender,password)
    )
    conn.commit()
    conn.close()

def insert_company(name, phone, address, industry):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO company (company_name, phone, address, industry) VALUES (%s,%s,%s,%s)",
        (name, phone, address, industry)
    )
    conn.commit()
    conn.close()

def insert_job(comp_id, title, description, location, salary, start_date, end_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO job (comp_id, title, description, location, salary, start_date, end_date) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (comp_id, title, description, location, salary, start_date, end_date)
    )
    conn.commit()
    conn.close()

def insert_skill(skill_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO skill (skill_name) VALUES (%s)", (skill_name,))
    conn.commit()
    conn.close()

def insert_application(email, job_id, status, applied_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO application (email, job_id, status, applied_date) VALUES (%s,%s,%s,%s)",
        (email, job_id, status, applied_date)
    )
    conn.commit()
    conn.close()

def insert_user_skill(email, skill_id, proficiency_level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user_skill (email, skill_id, proficiency_level) VALUES (%s,%s,%s)",
        (email, skill_id, proficiency_level)
    )
    conn.commit()
    conn.close()

def insert_job_skill(job_id, skill_id, importance_level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO job_skill (job_id, skill_id, importance_level) VALUES (%s,%s,%s)",
        (job_id, skill_id, importance_level)
    )
    conn.commit()
    conn.close()

# ----------------- UPDATE FUNCTIONS -----------------
def update_user(email_user, name, age, gender, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name=%s, age=%s, gender=%s, password=%s WHERE email=%s",
        (name, age, gender, password, email)
    )
    conn.commit()
    conn.close()

def update_company(comp_id, name, phone, address, industry):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE company SET company_name=%s, phone=%s, address=%s, industry=%s WHERE comp_id=%s",
        (name, phone, address, industry, comp_id)
    )
    conn.commit()
    conn.close()

def update_job(job_id, comp_id, title, description, location, salary, start_date, end_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE job SET comp_id=%s, title=%s, description=%s, location=%s, salary=%s, start_date=%s, end_date=%s WHERE job_id=%s",
        (comp_id, title, description, location, salary, start_date, end_date, job_id)
    )
    conn.commit()
    conn.close()

def update_skill(skill_id, skill_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE skill SET skill_name=%s WHERE skill_id=%s", (skill_name, skill_id))
    conn.commit()
    conn.close()

def update_application(app_id, email, job_id, status, applied_date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE application SET email=%s, job_id=%s, status=%s, applied_date=%s WHERE app_id=%s",
        (email, job_id, status, applied_date, app_id)
    )
    conn.commit()
    conn.close()

def update_user_skill(user_skill_id, email, skill_id, proficiency_level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE user_skill SET email=%s, skill_id=%s, proficiency_level=%s WHERE user_skill_id=%s",
        (email, skill_id, proficiency_level, user_skill_id)
    )
    conn.commit()
    conn.close()

def update_job_skill(job_skill_id, job_id, skill_id, importance_level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE job_skill SET job_id=%s, skill_id=%s, importance_level=%s WHERE job_skill_id=%s",
        (job_id, skill_id, importance_level, job_skill_id)
    )
    conn.commit()
    conn.close()

# ----------------- DELETE FUNCTIONS -----------------
def delete_row(table_name, pk_col, pk_val):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table_name} WHERE {pk_col}=%s", (pk_val,))
    conn.commit()
    conn.close()

# ----------------- STREAMLIT UI -----------------
st.title("Job Portal Admin Panel")

table_name = st.selectbox("Select Table", ["users","company","job","skill","application","user_skill","job_skill"])

st.subheader(f"{table_name} Table")
df = fetch_table(table_name)
st.dataframe(df)

st.subheader(f"Add New Record to {table_name}")

# ----------------- ADD RECORDS -----------------
if table_name == "users":
    email = st.text_input("Email", key="email")
    name = st.text_input("Name", key="user_name")
    age = st.number_input("Age", min_value=1, key="user_age")
    gender = st.selectbox("Gender", ["Male","Female","Other"], key="user_gender")
    password = st.text_input("Password", type="password", key="user_pass")
    if st.button("Add User"):
        insert_user(email,name,age,gender,password)
        st.success("User added!")
        st.experimental_rerun()

elif table_name == "company":
    comp_name = st.text_input("Company Name", key="comp_name")
    phone = st.text_input("Phone", key="comp_phone")
    address = st.text_input("Address", key="comp_address")
    industry = st.text_input("Industry", key="comp_industry")
    if st.button("Add Company"):
        insert_company(comp_name, phone, address, industry)
        st.success("Company added!")
        st.experimental_rerun()

elif table_name == "job":
    comp_id = st.number_input("Company ID", min_value=1, key="job_comp_id")
    title = st.text_input("Job Title", key="job_title")
    desc = st.text_input("Description", key="job_desc")
    location = st.text_input("Location", key="job_loc")
    salary = st.number_input("Salary", min_value=0, key="job_salary")
    start_date = st.date_input("Start Date", value=date.today(), key="job_start")
    end_date = st.date_input("End Date", value=date.today(), key="job_end")
    if st.button("Add Job"):
        insert_job(comp_id, title, desc, location, salary, start_date, end_date)
        st.success("Job added!")
        st.experimental_rerun()

elif table_name == "skill":
    skill_name = st.text_input("Skill Name", key="skill_name")
    if st.button("Add Skill"):
        insert_skill(skill_name)
        st.success("Skill added!")
        st.experimental_rerun()

elif table_name == "application":
    users_df = fetch_table("users")
    jobs_df = fetch_table("job")
    email_options = list(users_df['email'])
    job_options = list(jobs_df['job_id'])
    email = st.selectbox("User Email", email_options, key="app_email")
    job_id = st.selectbox("Job ID", job_options, key="app_job_id")
    status = st.selectbox("Status", ["Pending","Accepted","Rejected"], key="app_status")
    applied_date = st.date_input("Applied Date", value=date.today(), key="app_date")
    if st.button("Add Application"):
        insert_application(email, job_id, status, applied_date)
        st.success("Application added!")
        st.experimental_rerun()

elif table_name == "user_skill":
    users_df = fetch_table("users")
    skills_df = fetch_table("skill")
    email_options = list(users_df['email'])
    skill_options = list(skills_df['skill_id'])
    proficiency_options = ["Beginner","Intermediate","Advanced","Expert"]
    email = st.selectbox("User Email", email_options, key="us_email")
    skill_id = st.selectbox("Skill ID", skill_options, key="us_skill_id")
    proficiency_level = st.selectbox("Proficiency", proficiency_options, key="us_prof")
    if st.button("Add User Skill"):
        insert_user_skill(email, skill_id, proficiency_level)
        st.success("User Skill added!")
        st.experimental_rerun()

elif table_name == "job_skill":
    jobs_df = fetch_table("job")
    skills_df = fetch_table("skill")
    job_options = list(jobs_df['job_id'])
    skill_options = list(skills_df['skill_id'])
    importance_options = ["Low","Medium","High"]
    job_id = st.selectbox("Job ID", job_options, key="js_job_id")
    skill_id = st.selectbox("Skill ID", skill_options, key="js_skill_id")
    importance_level = st.selectbox("Importance", importance_options, key="js_importance")
    if st.button("Add Job Skill"):
        insert_job_skill(job_id, skill_id, importance_level)
        st.success("Job Skill added!")
        st.experimental_rerun()

# ----------------- UPDATE/DELETE -----------------
st.subheader(f"Update/Delete Records in {table_name}")

# Map table to primary key column
pk_map = {
    "users":"email",
    "company":"comp_id",
    "job":"job_id",
    "skill":"skill_id",
    "application":"app_id",
    "user_skill":"user_skill_id",
    "job_skill":"job_skill_id"
}

pk_col = pk_map[table_name]
selected_pk = st.selectbox(f"Select {pk_col} to edit/delete", df[pk_col])
record = df[df[pk_col]==selected_pk].iloc[0]

# ----------------- UPDATE/DELETE LOGIC -----------------
def render_update_delete(table_name, record):
    pk_col = pk_map[table_name]

    if table_name == "users":
        name = st.text_input("Name", value=record['name'], key="edit_user_name")
        age = st.number_input("Age", min_value=1, value=record['age'], key="edit_user_age")
        gender = st.selectbox("Gender", ["Male","Female","Other"], index=["Male","Female","Other"].index(record['gender']), key="edit_user_gender")
        password = st.text_input("Password", type="password", value=record['password'], key="edit_user_pass")
        if st.button("Update User"):
            update_user(selected_pk, name, age, gender, password)
            st.success("User updated!")
            st.experimental_rerun()
        if st.button("Delete User"):
            delete_row("users","email",selected_pk)
            st.success("User deleted!")
            st.experimental_rerun()

    elif table_name == "company":
        name = st.text_input("Company Name", value=record['company_name'], key="edit_comp_name")
        phone = st.text_input("Phone", value=record['phone'], key="edit_comp_phone")
        address = st.text_input("Address", value=record['address'], key="edit_comp_address")
        industry = st.text_input("Industry", value=record['industry'], key="edit_comp_industry")
        if st.button("Update Company"):
            update_company(selected_pk, name, phone, address, industry)
            st.success("Company updated!")
            st.experimental_rerun()
        if st.button("Delete Company"):
            delete_row("company","comp_id",selected_pk)
            st.success("Company deleted!")
            st.experimental_rerun()

    elif table_name == "job":
        comp_id = st.number_input("Company ID", value=record['comp_id'], key="edit_job_comp")
        title = st.text_input("Job Title", value=record['title'], key="edit_job_title")
        desc = st.text_input("Description", value=record['description'], key="edit_job_desc")
        location = st.text_input("Location", value=record['location'], key="edit_job_loc")
        salary = st.number_input("Salary", value=record['salary'], key="edit_job_salary")
        start_date = st.date_input("Start Date", value=record['start_date'], key="edit_job_start")
        end_date = st.date_input("End Date", value=record['end_date'], key="edit_job_end")
        if st.button("Update Job"):
            update_job(selected_pk, comp_id, title, desc, location, salary, start_date, end_date)
            st.success("Job updated!")
            st.experimental_rerun()
        if st.button("Delete Job"):
            delete_row("job","job_id",selected_pk)
            st.success("Job deleted!")
            st.experimental_rerun()

    elif table_name == "skill":
        skill_name = st.text_input("Skill Name", value=record['skill_name'], key="edit_skill_name")
        if st.button("Update Skill"):
            update_skill(selected_pk, skill_name)
            st.success("Skill updated!")
            st.experimental_rerun()
        if st.button("Delete Skill"):
            delete_row("skill","skill_id",selected_pk)
            st.success("Skill deleted!")
            st.experimental_rerun()

    elif table_name == "application":
        users_df = fetch_table("users")
        jobs_df = fetch_table("job")
        email_options = list(users_df['email'])
        job_options = list(jobs_df['job_id'])
        status_options = ["Pending","Accepted","Rejected"]

        email = st.selectbox("User Email", email_options, index=email_options.index(record['email']), key="edit_app_email")
        job_id = st.selectbox("Job ID", job_options, index=job_options.index(record['job_id']), key="edit_app_job")
        status = st.selectbox("Status", status_options, index=status_options.index(record['status']), key="edit_app_status")
        applied_date = st.date_input("Applied Date", value=record['applied_date'], key="edit_app_date")

        if st.button("Update Application"):
            update_application(selected_pk, email, job_id, status, applied_date)
            st.success("Application updated!")
            st.experimental_rerun()
        if st.button("Delete Application"):
            delete_row("application","app_id",selected_pk)
            st.success("Application deleted!")
            st.experimental_rerun()

    elif table_name == "user_skill":
        users_df = fetch_table("users")
        skills_df = fetch_table("skill")
        email_options = list(users_df['email'])
        skill_options = list(skills_df['skill_id'])
        prof_options = ["Beginner","Intermediate","Advanced","Expert"]

        email = st.selectbox("User Email", email_options, index=email_options.index(record['email']), key="edit_us_email")
        skill_id = st.selectbox("Skill ID", skill_options, index=skill_options.index(record['skill_id']), key="edit_us_skill")
        proficiency_level = st.selectbox("Proficiency", prof_options, index=prof_options.index(record['proficiency_level']), key="edit_us_prof")

        if st.button("Update User Skill"):
            update_user_skill(selected_pk, email, skill_id, proficiency_level)
            st.success("User Skill updated!")
            st.experimental_rerun()
        if st.button("Delete User Skill"):
            delete_row("user_skill","user_skill_id",selected_pk)
            st.success("User Skill deleted!")
            st.experimental_rerun()

    elif table_name == "job_skill":
        jobs_df = fetch_table("job")
        skills_df = fetch_table("skill")
        job_options = list(jobs_df['job_id'])
        skill_options = list(skills_df['skill_id'])
        imp_options = ["Low","Medium","High"]

        job_id = st.selectbox("Job ID", job_options, index=job_options.index(record['job_id']), key="edit_js_job")
        skill_id = st.selectbox("Skill ID", skill_options, index=skill_options.index(record['skill_id']), key="edit_js_skill")
        importance_level = st.selectbox("Importance", imp_options, index=imp_options.index(record['importance_level']), key="edit_js_imp")

        if st.button("Update Job Skill"):
            update_job_skill(selected_pk, job_id, skill_id, importance_level)
            st.success("Job Skill updated!")
            st.experimental_rerun()
        if st.button("Delete Job Skill"):
            delete_row("job_skill","job_skill_id",selected_pk)
            st.success("Job Skill deleted!")
            st.experimental_rerun()

# call the function
render_update_delete(table_name, record)
