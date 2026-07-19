import json
from typing import Dict

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query, status
from schemas import Patient, PatientInput

app = FastAPI(
    title="Patient Management",
    description="Patients Record Management API",
    version="1.0.0",
)


def load_data():
    with open("./patients.json", "r") as f:
        data = json.load(f)

    return data


def save_data(data):
    with open("./patients.json", "w") as f:
        json.dump(data, f, indent=4)


@app.get("/patients", response_model=Dict[str, Patient], tags=["patient"])
def fetch_all_records():
    data = load_data()

    return data


@app.get("/patients/{patient_id}", response_model=Patient, tags=["patient"])
def fetch_patient(
    patient_id: str = Path(
        examples=["P0001"], description="unique identifier of a patient"
    ),
):

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient record not Found")


@app.get("/sort", response_model=Dict[str, Patient], tags=["patient"])
def filter_patients(
    sort_by: str = Query(description="sort on the basis of height or weight"),
    asc: bool = Query(default=True, description="order of sorting"),
):

    data = load_data()

    if sort_by in ["height", "weight"]:
        sorted_data = dict(
            sorted(data.items(), key=lambda item: item[1][sort_by], reverse=not asc)
        )

        return sorted_data

    raise HTTPException(
        status_code=400, detail="Invalid name choose either height or weight"
    )


@app.post(
    "/add_patient",
    response_model=Dict[str, str],
    tags=["patient"],
    status_code=status.HTTP_201_CREATED,
)
def add_patient(request: PatientInput):

    data = load_data()

    if request.id in data:
        raise HTTPException(status_code=400, detail="Patient record already exists.")

    data[request.id] = request.model_dump(exclude=["id"])

    save_data(data)

    return {"message": "Successfully added."}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, log_level="info", reload=True)
