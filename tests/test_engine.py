import typing

import pytest

import aviation
from aviation import _engine as engine


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        ({"passengers_per_year": 6_000_000_000}, "passengers_per_year", 6_000_000_000),
        ({"required_global_fleet": 27_397.26}, "required_global_fleet", 27_397.26),
        (
            {"days_per_year": 365.0, "passengers_per_year": 6_000_000_000},
            "passengers_per_day",
            16_438_356.16,
        ),
        (
            {
                "passengers_per_day": 16_438_356.16,
                "seats_per_aircraft": 200.0,
                "flights_per_aircraft_per_day": 3.0,
            },
            "required_global_fleet",
            27_397.26,
        ),
        (
            {
                "days_per_year": 365.0,
                "passengers_per_year": 6_000_000_000,
                "seats_per_aircraft": 200.0,
                "flights_per_aircraft_per_day": 3.0,
            },
            "required_global_fleet",
            27_397.26,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: typing.Any,  # noqa: ANN401
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest.approx(expected, abs=1.0)
