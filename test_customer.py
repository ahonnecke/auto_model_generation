#!/usr/bin/env python3

import pytest

from customer_mock_factory import MockCustomerFactory


@pytest.fixture
def customers():
    return [MockCustomerFactory.build() for x in range(25)]

def test_customer(customers):
    for customer in customers:
        assert customer.name
        assert customer.email
        assert customer.role
        assert customer.customer_id

    breakpoint()
