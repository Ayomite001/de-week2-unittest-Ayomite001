import sys
import os
import pytest

# Add the main folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture
def system():
    return ArtificialPancreasSystem(glucose_level=100)


def test_glucose_increases_after_meal(system):
    system.glucose_level += 40 * ArtificialPancreasSystem.GLUCOSE_PER_CARB
    assert system.glucose_level > 100


def test_glucose_never_below_min(system):
    system.glucose_level -= 50 * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN
    assert system.glucose_level >= 0


def test_glucose_decreases_after_excercise(system):
    system.glucose_level -= 20 * ArtificialPancreasSystem.GLUCOSE_BURN_PER_MIN
    assert system.glucose_level < 100