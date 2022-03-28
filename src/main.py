from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

_services.create_database()


@app.get("/candidates/", response_model=List[_schemas.Candidate])
def read_candidates(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    candidates = _services.get_candidates(db=db, skip=skip, limit=limit)
    return candidates

