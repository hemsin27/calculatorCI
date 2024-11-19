import calculator

class TestCalculator:


    def test_add(self):
        assert  4 == calculator.add(2, 2)


    def test_sub(self):
        assert  3 == calculator.sub(5, 2)

    def test_mul(self):
        assert  10 == calculator.mul(5, 2)