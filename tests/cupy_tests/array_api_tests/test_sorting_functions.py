import pytest

from cupy import array_api as xp


@pytest.mark.parametrize(
    "obj, axis, expected",
    [
        ([0, 0], -1, [0, 1]),
        ([0, 1, 0], -1, [1, 0, 2]),
        ([[0, 1], [1, 1]], 0, [[1, 0], [0, 1]]),
        ([[0, 1], [1, 1]], 1, [[1, 0], [0, 1]]),
    ],
)
@pytest.mark.skipif(
    # https://github.com/cupy/cupy/issues/5701
    True, reason="Sorting functions miss arguments kind and order")
def test_stable_desc_argsort(obj, axis, expected):
    """
    Indices respect relative order of a descending stable-sort

    See https://github.com/numpy/numpy/issues/20778
    """
    x = xp.asarray(obj)
    out = xp.argsort(x, axis=axis, stable=True, descending=True)
    assert xp.all(out == xp.asarray(expected))
