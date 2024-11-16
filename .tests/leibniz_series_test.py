from leibniz_series_exercise import approximate_pi

def test_leibniz_series():
    assert abs(approximate_pi(1) - 4) < 0.1, "Test failed: approximate_pi(1) should be close to 4"
    assert abs(approximate_pi(5) - 3.339) < 0.01, "Test failed: approximate_pi(5) should be close to 3.339."
    assert abs(approximate_pi(99) - 3.151) < 0.01, "Test failed: approximate_pi(99)."
    assert abs(approximate_pi(999) - 3.1425) < 0.001, "Test failed: approximate_pi(999)."

