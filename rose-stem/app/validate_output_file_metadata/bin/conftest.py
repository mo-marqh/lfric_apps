##############################################################################
# (c) Crown copyright Met Office. All rights reserved.
# The file LICENCE, distributed with this code, contains details of the terms
# under which the code may be used.
##############################################################################
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--file", action="store", required=True, help="Input netCDF file"
    )

@pytest.fixture
def infile(request):
    return request.config.getoption("--file")
