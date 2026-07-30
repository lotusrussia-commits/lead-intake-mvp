from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import engine, get_db
from app.logger import log_error, log_lead_created
from app.models import Base, Lead
from app.schemas import Lead as LeadSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Некорректные данные заявки",
            "details": exc.errors(),
        },
    )


@app.get("/")
def home():
    return {"message": "Lead Intake MVP работает!"}


@app.post("/lead")
def create_lead(lead: LeadSchema, db: Session = Depends(get_db)):
    try:
        new_lead = Lead(
            name=lead.name,
            contact=lead.contact,
            source=lead.source,
            comment=lead.comment,
        )

        db.add(new_lead)
        db.commit()
        db.refresh(new_lead)

        log_lead_created(new_lead.id)

        return {
            "status": "success",
            "message": "Заявка сохранена",
            "id": new_lead.id,
        }

    except Exception as e:
        db.rollback()
        log_error(e)
        raise HTTPException(
            status_code=500,
            detail="Ошибка сохранения заявки",
        )
