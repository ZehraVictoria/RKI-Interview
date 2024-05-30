import fastapi
import uvicorn

from rki.interview.models import Candidate

app = fastapi.FastAPI()

dummy_database = [
    Candidate(
        id=1,
        full_name="Lisa Simpson",
        experiences=["Saxophonist", "Fast food vendor"],
    ),
    Candidate(
        id=2,
        full_name="Ned Flanders",
        experiences=["Pharmaceutical salesmen"],
    ),
    Candidate(
        id=3,
        full_name="Bernd das Brot",
        experiences=["TV host","Motivational speaker"],
    ),
]

# POST endpoint adding candidate to db
@app.post("/candidates/", response_model=Candidate)
async def create_candidate(candidate: Candidate):
    # Check if candidate ID already exists
    if any(person.id == candidate.id for person in dummy_database):
        raise fastapi.HTTPException(status_code=400, detail="This Candidate ID already exists")
    
    dummy_database.append(candidate)
    return candidate

@app.get("/candidates")
def read_candidates() -> list[Candidate]:
    """Return a list of interview candidates."""
    return dummy_database


def run() -> None:
    """Start the server process."""
    uvicorn.run("rki.interview.main:app", reload=True)
