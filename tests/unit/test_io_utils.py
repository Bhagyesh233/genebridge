# tests.unit.test_io_utils

"""
Unit tests for assignment4.io_utils module.
"""


import pytest
import assignment4.io_utils as io_utils


def test_getfilehandle_oserror():
    """Test if get_filehandle raises OSError for a non-existent file."""
    with pytest.raises(OSError):
        io_utils.get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_invalid_mode():
    """Test if get_filehandle raises ValueError for an invalid mode."""
    with pytest.raises(ValueError):
        io_utils.get_filehandle(file='invalid_file.txt', mode='invalid')
