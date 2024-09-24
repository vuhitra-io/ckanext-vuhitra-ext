import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def vuhitra_ext_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "vuhitra_ext_get_sum": vuhitra_ext_get_sum,
    }
