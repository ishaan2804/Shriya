from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Load CSV data
csv_file = "q-fastapi.csv"
df = pd.read_csv(csv_file)

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (allowing all origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/api")
def get_students(class_: list[str] = Query(None, alias="class")):
    """
    Fetch students data, optionally filtered by class.
    Example:
    - GET /api → Returns all students
    - GET /api?class=1A → Returns students in class 1A
    - GET /api?class=1A&class=1B → Returns students in class 1A and 1B
    """
    if class_:
        filtered_df = df[df["class"].isin(class_)]
    else:
        filtered_df = df

    students = filtered_df.to_dict(orient="records")
    return {"students": students}

# Run the server using: uvicorn main:app --reload
