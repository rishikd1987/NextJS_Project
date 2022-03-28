import datetime as _dt
from enum import unique
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database


class Candidate(_database.Base):
    __tablename__ = "candidate"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    firstname = _sql.Column(_sql.String(30), index=True)
    surname = _sql.Column(_sql.String(30), index=True)
    email = _sql.Column(_sql.String(100), index=True)
    mobile = _sql.Column(_sql.String(15), index=True)
    is_active = _sql.Column(_sql.Boolean, default=True)

    # posts = _orm.relationship("Post", back_populates="owner")


class Job(_database.Base):
    __tablename__ = "job"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    jobid = _sql.Column(_sql.String(15), unique=True, index=True)
    shortdescription = _sql.Column(_sql.String(50), index=True)
    detaileddescription = _sql.Column(_sql.String(500), index=True)
    is_active = _sql.Column(_sql.Boolean, default=True)

    # owner = _orm.relationship("User", back_populates="posts")