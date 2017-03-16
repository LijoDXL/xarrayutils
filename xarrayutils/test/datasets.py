from __future__ import print_function
from future.utils import iteritems
import pytest
import xarray as xr
import numpy as np
import dask.array as da

a_2d_nan = np.array([
    [1,1,1,3,3,3,5,5],
    [1,np.nan,1,3,3,3,5,5],
    [1,1,1,3,3,3,5,5],
    [2,2,2,4,4,4,6,6],
    [2,2,2,4,4,4,6,6],
    [2,2,2,4,4,4,6,6]
],dtype=np.float)

ones_2d = np.ones([6,8],dtype=np.float)

ones_2d_nan      = ones_2d.copy()
ones_2d_nan[2,2] = np.nan

# for the grid dataset
grid_i = np.arange(0,8)
grid_j = np.arange(0,6)
grid_XC,grid_YC = np.meshgrid(grid_i+0.5,grid_j+0.5)
grid_XG,grid_YG = np.meshgrid(grid_i,grid_j)
grid_dxC = np.ones_like(grid_XG)
grid_dxG = grid_dxC
grid_dyC = grid_dxC
grid_dyG = grid_dxC


dataarrays= {
    # the comodo example
    'datagrid_dimtest': xr.Dataset(
        coords={'j': (['j',], grid_j),
        'j_g': (['j_g',], grid_j),
        'i': (['i',], grid_i),
        'i_g': (['i_g',], grid_i),
        'XC': (['j','i'], grid_XC),
        'YC': (['j','i'], grid_YC),
        'XG': (['j_g','i_g'], grid_XG),
        'YG': (['j_g','i_g'], grid_YG),
        'dxG': (['j_g','i'], grid_dxG),
        'dxC': (['j','i_g'], grid_dxC),
        'dyG': (['j','i_g'], grid_dyG),
        'dyC': (['j_g','i'], grid_dyC)},
        ),
    'dataarray_2d_example': xr.DataArray(
        da.from_array(a_2d_nan,a_2d_nan.shape,name='a_2d_nan'),
        coords={'j': (['j',], np.arange(0,6)),
        'i': (['i',], np.arange(0,8))},
        dims=['j','i']
        ),
    'dataarray_2d_ones': xr.DataArray(
        da.from_array(ones_2d,ones_2d.shape,name='ones_2d'),
        coords={'j': (['j',], np.arange(0,6)),
        'i': (['i',], np.arange(0,8))},
        dims=['j','i']
        ),
    'dataarray_2d_ones_nan': xr.DataArray(
        da.from_array(ones_2d_nan,ones_2d_nan.shape,name='ones_2d_nan'),
        coords={'j': (['j',], np.arange(0,6)),
        'i': (['i',], np.arange(0,8))},
        dims=['j','i']
        )

}

@pytest.fixture(params=['dataarray_2d_example'])
def dataarray_2d_example(request):
    return dataarrays[request.param]

@pytest.fixture(params=['dataarray_2d_ones'])
def dataarray_2d_ones(request):
    return dataarrays[request.param]

@pytest.fixture(params=['dataarray_2d_ones_nan'])
def dataarray_2d_ones_nan(request):
    return dataarrays[request.param]

@pytest.fixture(params=['datagrid_dimtest'])
def datagrid_dimtest(request):
    return dataarrays[request.param]

datagrid_dimtest
# @pytest.fixture(scope="module", params=['nonperiodic_1d'])
# def nonperiodic_1d(request):
#     return datasets[request.param]
#
# @pytest.fixture(scope="module", params=['periodic_1d'])
# def periodic_1d(request):
#     return datasets[request.param]
