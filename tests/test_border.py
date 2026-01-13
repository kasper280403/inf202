# Teste vektor mellom to punkter i border. Er disse korrekt / 90 grader?

import pytest

from src.model.border.border import Border
from src.model.point.point import Point

def test_border_vector():
    p1 = Point((0, 0))
    p2 = Point((1, 0))

    border = Border(p1, p2)
    v = border.direction_vector()
    n = border.normal_vector()

    dot = v[0] * n[0] + v[1] * n[1]
    assert dot == pytest.approx(0.0)



    