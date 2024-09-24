"""Tests for views.py."""

import pytest

import ckanext.vuhitra_ext.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "vuhitra_ext")
@pytest.mark.usefixtures("with_plugins")
def test_vuhitra_ext_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("vuhitra_ext.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, vuhitra_ext!"
