from typing import List
import datetime as _dt
import pydantic as _pydantic


class _CandidateBase(_pydantic.BaseModel):
    firstname: str
    surname: str
    email: str
    mobile: str


class CandidateCreate(_CandidateBase):
    pass


class Candidate(_CandidateBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class _JobBase(_pydantic.BaseModel):
    shortdescription: str
    detaileddescription: str


class JobCreate(_JobBase):
    pass


class Job(_JobBase):
    id: int
    jobid: str
    is_active: bool
    

    class Config:
        orm_mode = True