import pytest

from utils import arrs

@pytest.fixture
def collections_for_testing():
    return [1, 2, 3, 4]

def test_get(collections_for_testing):
    assert arrs.get(collections_for_testing, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"

def test_slice(collections_for_testing):
    assert arrs.my_slice(collections_for_testing, 1, 3) == [2, 3]
    assert arrs.my_slice(collections_for_testing, 1) == [2, 3, 4]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(collections_for_testing, -2) == [3, 4]
    assert arrs.my_slice(collections_for_testing, -6) == [1, 2, 3, 4]