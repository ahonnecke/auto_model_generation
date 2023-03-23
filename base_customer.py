# generated by datamodel-codegen:
#   filename:  customer.json
#   timestamp: 2023-03-23T20:13:44+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class BaseCustomer(BaseModel):
    class Config:
        allow_population_by_field_name = True

    name: str
    email: str
    role: str
    customer_id: int = Field(..., alias='customerId')
