from __future__ import print_function
from future.utils import iteritems
import pytest
import xarray as xr
import numpy as np
import os
from xarrayutils.utils import dummy_function

def dummy_test():
    assert dummy_function()==1


# aggregate
# Test if exception is raised when dimensions are mislabeled

# Test if exception is raised when the blocks input is constructed wrong
# def test_aggregate_input():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0
# Need a fixture for all these tests...
