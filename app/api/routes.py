from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the CI/CD demo"}

@router.get("/health")
def health():
    return {"status": "ok"}