from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
import database


app = FastAPI()

#Case pydantic
class Case(BaseModel):
    
    title: str 
    victim_name: str
    crime_type: str

#Suspect pydantic
class Suspect(BaseModel):
    case_id: int
    name: str
    age: int
    motive: str
    alibi: str

#Witness pydantic
class Witnesses(BaseModel):
    case_id : int
    name : str 
    statement : str 

#Evidence pydantic
class Evidence(BaseModel):
    case_id: int
    evidence : str
    evidence_status : str


#Case adding 
@app.post("/case")
def create_case (case:Case):

    database.cursor.execute("""
    insert into cases(title, victim_name, crime_type)
    values (?,?,?)""",
    (
     case.title,
     case.victim_name,
     case.crime_type ))

    database.connection.commit()

    return {
        "message": "Case Created Successfully"
    }

# Suspect Adding 
@app.post("/suspect")
def create_suspect(suspect:Suspect):

    database.cursor.execute("""
    insert into suspects(case_id, name, age, motive,alibi) values (?,?,?,?,?)""" , 

    (
        suspect.case_id,
        suspect.name,
        suspect.age,
        suspect.motive,
        suspect.alibi
    )
    )

    database.connection.commit()

    return{"Message" : "suspect added sucessfully to the case "}


#Witness adding 
@app.post("/witnesses/")
def add_witness(witnesses:Witnesses):
   database.cursor.execute("""insert into witnesses(case_id,name,statement) values(?,?,?)""", 
   (

    witnesses.case_id,
    witnesses.name,
    witnesses.statement

   )
   )

   database.connection.commit()
   return{"Message" : "Witness added sucessfully to the case "}


#Evidence adding 
@app.post("/evidence/")
def add_evidence(evidence:Evidence):
    database.cursor.execute("""insert into evidence(case_id ,evidence,evidence_status)values(?,?,?)""",

    (
        evidence.case_id,
        evidence.evidence,
        evidence.evidence_status
    )
    )
    database.connection.commit()
    return{"Message":"Evidence Added sucessfully to the Case"}








@app.get("/cases/{id}")
def get_case(id:int):
    database.cursor.execute("SELECT * FROM cases WHERE id=?", (id,))

    data = database.cursor.fetchone()

    if data is None:
        raise HTTPException(
        status_code = 404 , 
        detail = "Case not found")

    return data


@app.get("/suspects/{case_id}")
def get_suspects(case_id:int):
    database.cursor.execute("SELECT * FROM suspects WHERE case_id=?", (case_id,))

    data = database.cursor.fetchall()

    if not data:
        raise HTTPException(status_code=404,detail="Suspect not exists")

    return data 


@app.get("/witnesses/{case_id}")
def get_wintess_statement(case_id:int):
    
    database.cursor.execute("SELECT * FROM witnesses WHERE case_id =?" , (case_id,))

    data = database.cursor.fetchall()
    if len(data)==0:
        raise HTTPException(status_code=404,detail="Wintess Not Available")

    return data

@app.get("/evidence/{case_id}")
def get_evidence(case_id:int):
    database.cursor.execute("SELECT * FROM evidence WHERE case_id = ?" , (case_id,))

    data = database.cursor.fetchall()

    if not data:
        raise HTTPException(status_code=404,
        detail="Evidence not present")

    return data



#updating the case database 

@app.put("/cases/{id}")
def update_case(cases:Case , id:int):
    database.cursor.execute(""" update cases set title = ? , victim_name = ? , crime_type = ? where id = ? """, 
    
    (
        cases.title,
        cases.victim_name,
        cases.crime_type,
        id

    )
    
    )
    database.connection.commit()

    return {"Message:""Update saved Sucessfully"}

# deleting the case from database 

@app.delete("/cases/{id}")
def delete_case(id:int):
    database.cursor.execute("""DELETE FROM cases WHERE id = ? """ , (id,))
    database.connection.commit()
    return{"Message:""Case is Deleted from the database Sucessfully"}



# Get the full case details 

@app.get("/detail-case/{case_id}")
def get_case_detail(case_id:int):
    database.cursor.execute("""SELECT * FROM cases 
                            JOIN suspects
                            ON cases.id = suspects.case_id WHERE cases.id = ?""",(case_id,))

    data = database.cursor.fetchall()
    return data
                           


#Query Parameter
@app.get("/cases")
def search_cases(crime_type: str):

    database.cursor.execute("""
        SELECT *
        FROM cases
        WHERE crime_type = ?
    """, (crime_type,))

    data = database.cursor.fetchall()

    return data