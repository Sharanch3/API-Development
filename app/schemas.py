from typing import Optional

from pydantic import BaseModel, Field, computed_field


class Patient(BaseModel):
    name: str = Field(
        ...,
        description="name of the patient",
        examples=["Suraj", "Sujata"],
        min_length=2,
    )

    city: str = Field(..., description="name of the city", examples=["Mumbai", "Delhi"])

    age: int = Field(
        ..., description="age of the patient", examples=[21, 30, 42], ge=1, le=100
    )

    gender: Optional[str] = Field(
        default=None, description="sex of the patient", min_length=3
    )

    weight: float = Field(
        ..., description="weight of the patient in kg", examples=[30, 60]
    )
    height: float = Field(..., description="height of the patient")

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height**2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        else:
            return "Obese"


class PatientInput(Patient):
    id: str = Field(
        ..., description="Unique identifier of a patient", examples=["P0001"]
    )


class PatientUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        description="name of the patient",
        examples=["Suraj", "Sujata"],
        min_length=2,
    )

    city: Optional[str] = Field(
        default=None, description="name of the city", examples=["Mumbai", "Delhi"]
    )

    age: Optional[int] = Field(
        default=None,
        description="age of the patient",
        examples=[21, 30, 42],
        ge=1,
        le=100,
    )

    gender: Optional[str] = Field(
        default=None, description="sex of the patient", min_length=3
    )

    weight: Optional[float] = Field(
        default=None, description="weight of the patient in kg", examples=[30, 60]
    )
    height: Optional[float] = Field(default=None, description="height of the patient")
