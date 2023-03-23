#!/usr/bin/env python3

from faker import Faker
from pydantic_factories import ModelFactory

from customer_model import Customer

FAKE = Faker() # Seed the fake data generator

class MockCustomerFactory(ModelFactory):
    __model__ = Customer

    email: str = FAKE.email()
    name: str = FAKE.name()
    role: str = FAKE.job()
