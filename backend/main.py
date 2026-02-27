from fastapi import FastAPI, Depends, HTTPException,status
from sqlalchemy.orm import Session
from pydantic import BaseModel


from typing import List
from database import engine, SessionLocal, Base
import random


Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""1. GET /comparison
Returns a blind comparison:

comparison_id
review_a (text)
review_b (text)
Model identifiers should NOT be revealed

Example response:

{ "comparison_id": 1, "review_a": "This paper proposes...", "review_b": "The methodology is unclear..." }


"""
#Answer:
#I assume I'm using Python and FastAPI to connect the front-end and back-end.


comparisons=[{"comparison_id":1, "review_a":..., "review_b":..., "model_a":..,"model_b":...},{...},{...},...]

class ComparisonResponse(BaseModel):
    comparison_id:int
    review_a:str
    review_b:str

@app.get("/comparison",response_model=ComparisonResponse)
def get_Comparsion():
    comparison_id=random.choice()
    try:
        ...
        return{"comparison_id":comparison_id,  "review_a":review_a, "review_b":review_b}
    except:
        ...
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Comparison Error")


"""
2. POST /vote
Accept:

{ "comparison_id": 1, "winner": "A" // A | B | tie }

Backend must: - Store the vote - Return the updated votes
"""
#Answer:
modelVotes={
    "model_a": {"wins":0, "lose":0,"tie":0},
    ...
}

class VoteRequest(BaseModel):
    comparison_id:int
    winner: str  # A | B | tie

@app.post("/vote")
async def vote_update(request:VoteRequest):
    try:
        comparison = next( (c for c in comparisons if (c["comparison_id"]==request.comparison_id)),None)
        if not comparison:
            raise HTTPException(status_code=404,detail=f"vote failure,wrong comparison id")
        model_a=comparison["model_a"]
        model_b=comparison["model_b"]

        if request.winner=="A":
            modelVotes[model_a]["wins"] +=1
            modelVotes[model_b]["lose"] +=1
        elif request.winner=="B":
            modelVotes[model_b]["wins"] +=1
            modelVotes[model_a]["lose"] +=1
        elif request.winner=="tie":
            modelVotes[model_a]["tie"] +=1
            modelVotes[model_b]["tie"] +=1
        else:
            raise HTTPException(status_code=status.HTTP_404_INTERNAL_SERVER_ERROR,
                                detail=f"Vote failure, wrong vote select")
        return{
            "message":"vote successfully",
            "vote":modelVotes
        }

    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Vote failure, server Error")

"""3. GET /leaderboard
Return a ranked list of models sorted by votes descending.

Example:

[ { "model": "GPT5", "votes": 1 }, { "model": "Gemini-3 Pro", "votes": 0 }]

"""
#Answer:
@app.get("/leaderboard")
async def get_leaderboard():
    leaderboard=[]
    ...
    for model, stats in modelVotes.items():
        leaderboard.append({"model":model,"votes":stats["wins"]})

    leaderboard.sort(key=lambda x :x["votes"],reverse=True)
    return leaderboard



