# Copyright (c) 2024, Pragati Dhawale and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class AirplaneTicket(Document):
	pass

# class AirplaneTicket(Document):
#     def validate(self):
#         self.check_status()
#     def check_status(self):
#         status =frappe.db.get_simple_value("")
        


