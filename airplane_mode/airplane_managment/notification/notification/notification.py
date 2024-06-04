# import frappe

# def get_context(context):
# 	# do your magic here
# 	pass


import frappe

def get_context(context):
    # Retrieve some data from the database
    some_data = frappe.get_list("Some Doctype", filters={"some_field": "some_value"}, fields=["name", "some_field"])

    # Add the retrieved data to the context
    context["some_data"] = some_data

    # Modify an existing key in the context
    context["title"] = "Custom Page Title"
