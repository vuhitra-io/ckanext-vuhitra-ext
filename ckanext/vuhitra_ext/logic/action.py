import ckan.plugins.toolkit as tk
import ckanext.vuhitra_ext.logic.schema as schema


@tk.side_effect_free
def vuhitra_ext_get_sum(context, data_dict):
    tk.check_access(
        "vuhitra_ext_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.vuhitra_ext_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'vuhitra_ext_get_sum': vuhitra_ext_get_sum,
    }
