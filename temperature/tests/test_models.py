# temperature/tests/test_models.py
import pytest
from django.utils import timezone
from temperature.models import TemperatureReading

@pytest.mark.django_db
def test_create_and_retrieve_temperature_reading():
    # Create a temperature reading
    temp_reading = TemperatureReading.objects.create(
        value=25.5, 
        timestamp=timezone.now()
    )

    # Retrieve the created reading
    retrieved = TemperatureReading.objects.last()

    # Assert that the created reading is correctly retrieved
    assert retrieved.value == 25.5
