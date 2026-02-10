import pytest
from even_number_bitwise_ors import Solution_1002


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4, 5, 6], 6),
        ([7, 9, 11], 0),
        ([1, 8, 16], 24),
        ([], 0),
        ([2], 2),
        ([1], 0),
        ([0, 2, 4], 6),
        ([1024, 2048], 3072),
    ]
)
def test_even_number_bitwise_ors(nums, expected):
    sol = Solution_1002()
    assert sol.evenNumberBitwiseORs(nums) == expected
