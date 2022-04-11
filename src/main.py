from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.get("/candidates/", response_model=List[_schemas.Candidate])
def read_candidates(
    skip: int = 0,
    limit: int = 500,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    candidates = _services.get_candidates(db=db, skip=skip, limit=limit)
    return candidates

@app.post("/candidates/", response_model=_schemas.Candidate)
def create_candidates(
    candidate: _schemas.CandidateCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_candidate = _services.get_candidate_by_email(db=db, email=candidate.email)
    if db_candidate:
        raise _fastapi.HTTPException(
            status_code=400, detail="The email is in use"
        )
    return _services.create_candidate(db=db, candidate=candidate)

@app.post("/candidates/{candidate_id}", response_model=_schemas.Candidate)
def update_candidate(
    candidate_id: int,
    post: _schemas.CandidateCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_candidate(db=db, post=post, candidate_id=candidate_id)

@app.get("/jobs/", response_model=List[_schemas.Job])
def read_jobs(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    jobs = _services.get_jobs(db=db, skip=skip, limit=limit)
    return jobs



