# generated by datamodel-codegen:
#   filename:  problems.json
#   timestamp: 2023-03-23T20:36:04+00:00

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class AssociatedDrugItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: str
    dose: str
    strength: str


class AssociatedDrug2Item(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: str
    dose: str
    strength: str


class ClassNameItem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    associated_drug: List[AssociatedDrugItem] = Field(..., alias='associatedDrug')
    associated_drug_2: List[AssociatedDrug2Item] = Field(..., alias='associatedDrug#2')


class ClassName2Item(BaseModel):
    class Config:
        allow_population_by_field_name = True

    associated_drug: List[AssociatedDrugItem] = Field(..., alias='associatedDrug')
    associated_drug_2: List[AssociatedDrug2Item] = Field(..., alias='associatedDrug#2')


class MedicationsClass(BaseModel):
    class Config:
        allow_population_by_field_name = True

    class_name: List[ClassNameItem] = Field(..., alias='className')
    class_name2: List[ClassName2Item] = Field(..., alias='className2')


class Medication(BaseModel):
    class Config:
        allow_population_by_field_name = True

    medications_classes: List[MedicationsClass] = Field(..., alias='medicationsClasses')


class Lab(BaseModel):
    class Config:
        allow_population_by_field_name = True

    missing_field: str


class Diabetes(BaseModel):
    class Config:
        allow_population_by_field_name = True

    medications: List[Medication]
    labs: List[Lab]


class Problem(BaseModel):
    class Config:
        allow_population_by_field_name = True

    diabetes: List[Diabetes] = Field(..., alias='Diabetes')
    asthma: List[Dict[str, Any]] = Field(..., alias='Asthma')


class BaseProblems(BaseModel):
    class Config:
        allow_population_by_field_name = True

    problems: List[Problem]