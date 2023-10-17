import frappe
from frappe.utils.response import json_response
from frappe import get_request_header


@frappe.whitelist(allow_guest=True)
def read_data(doctype,name):
    doc=frappe.get_doc(doctype,name)
    return json_response(doc.as_dict())

