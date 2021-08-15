class DivisionByNull:
    def __init__(self, dividend, denominator):
        self.dividend = dividend
        self.denominator = denominator

    @staticmethod
    def divide_by_null(dividend, denominator):
        try:
            return (dividend / denominator)
        except:
            return (f"На ноль делить нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(DivisionByNull.divide_by_null(10, 5))
print(DivisionByNull.divide_by_null(100, 5))
print(div.divide_by_null(100, 0))