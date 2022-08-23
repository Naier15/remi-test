from django.http import JsonResponse
from api.views import get_currency_rates

import pytest


@pytest.mark.django_db
def test_get_currency_rates():
    result = get_currency_rates({})

    assert type(result) == JsonResponse
    assert result.status_code == 200