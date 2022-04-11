import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
def get_candidate(db: _orm.Session, user_id: int):
    return db.query(_models.User).filter(_models.User.id == user_id).first()
"""

def get_candidate_by_email(db: _orm.Session, email: str):
    return db.query(_models.Candidate).filter(_models.Candidate.email == email).first()

def get_candidates(db: _orm.Session, skip: int = 0, limit: int = 500):
    return db.query(_models.Candidate).offset(skip).limit(500).all()

def get_candidate(db: _orm.Session, candidate_id: int):
    return db.query(_models.Candidate).filter(_models.Candidate.id == candidate_id).first()

def create_candidate(db: _orm.Session, candidate: _schemas.CandidateCreate):
    db_candidate = _models.Candidate(firstname=candidate.firstname, surname=candidate.surname, email=candidate.email,mobile=candidate.mobile)
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

def update_candidate(db: _orm.Session, candidate_id: int, post: _schemas.CandidateCreate):
    db_candidate = get_candidate(db=db, candidate_id=candidate_id)
    db_candidate.firstname = post.firstname
    db_candidate.surname = post.surname
    db_candidate.email = post.email
    db_candidate.mobile = post.mobile
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


def get_jobs(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Job).offset(skip).limit(limit).all()
"""

def create_user(db: _orm.Session, user: _schemas.UserCreate):
    fake_hashed_password = user.password + "thisisnotsecure"
    db_user = _models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_posts(db: _orm.Session, skip: int = 0, limit: int = 10):
    return db.query(_models.Post).offset(skip).limit(limit).all()


def create_post(db: _orm.Session, post: _schemas.PostCreate, user_id: int):
    post = _models.Post(**post.dict(), owner_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_post(db: _orm.Session, post_id: int):
    return db.query(_models.Post).filter(_models.Post.id == post_id).first()


def delete_post(db: _orm.Session, post_id: int):
    db.query(_models.Post).filter(_models.Post.id == post_id).delete()
    db.commit()




"""