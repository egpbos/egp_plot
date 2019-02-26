#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the egp_plot module.
"""
import pytest

from egp_plot import egp_plot


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_egp_plot(an_object):
    assert an_object == {}
