import ckan.plugins.toolkit as tk


def vuhitra_ext_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "vuhitra_ext_required": vuhitra_ext_required,
    }
