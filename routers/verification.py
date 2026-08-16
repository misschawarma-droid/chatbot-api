from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import EmailVerification
from schemas import SendVerificationCodeIn, SendVerificationCodeOut, VerifyCodeIn, VerifyCodeOut
from email_verification import generate_verification_code, get_expiry
from notifications import send_email

router = APIRouter(prefix="/api/verification", tags=["verification"])

ALLOWED_DOMAIN = "talints.fr"


@router.post("/send-code", response_model=SendVerificationCodeOut)
def send_code(payload: SendVerificationCodeIn, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    if not email.endswith(f"@{ALLOWED_DOMAIN}"):
        raise HTTPException(status_code=400, detail="Domaine email non autorisé")

    code = generate_verification_code()
    verification = EmailVerification(
        email=email,
        code=code,
        expires_at=get_expiry(),
    )
    db.add(verification)
    db.commit()

    send_email(
        email,
        "Votre code de vérification Miss Chawarma",
        f"Voici votre code de vérification : {code}\nCe code expire dans 10 minutes.",
    )

    return {"sent": True}


@router.post("/verify-code", response_model=VerifyCodeOut)
def verify_code(payload: VerifyCodeIn, db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    verification = (
        db.query(EmailVerification)
        .filter(EmailVerification.email == email, EmailVerification.code == payload.code.strip())
        .order_by(EmailVerification.created_at.desc())
        .first()
    )

    if not verification:
        return {"verified": False, "message": "Code incorrect"}
    if verification.expires_at < datetime.utcnow():
        return {"verified": False, "message": "Code expiré"}

    verification.is_verified = True
    db.commit()

    return {"verified": True}