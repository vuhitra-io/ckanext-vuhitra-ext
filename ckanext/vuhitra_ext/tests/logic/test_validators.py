"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.vuhitra_ext.logic import validators


def test_vuhitra_ext_reauired_with_valid_value():
    assert validators.vuhitra_ext_required("value") == "value"


def test_vuhitra_ext_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.vuhitra_ext_required(None)
