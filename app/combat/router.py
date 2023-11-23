from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.combat.schemas import Combat
from app.combat.dependecies import get_db
from app.combat.utils import make_combat_messages, intercalate_messages

router = APIRouter(
    prefix="/combat",
    tags=["Combat"],
)


@router.post("/narration", status_code=status.HTTP_202_ACCEPTED)
def narration(combat: Combat, session: Session = Depends(get_db)):
    messages1, messages2 = make_combat_messages(combat, session)
    print(messages1)
    print(messages2)
    combat_narration = intercalate_messages(messages1, messages2)
    return {
            "narration": combat_narration
        }
