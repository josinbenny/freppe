# Copyright (c) 2023, Josin Benny and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import money_in_words,validate_json_string

class ClientSideScripting(Document):
	def before_save(self):
	# 	# m=1520335
	# 	self.full_name=f'{self.first_name} {self.middle_name} {self.last_name or ""}'
	# 	# frappe.msgprint(money_in_words(m))


# No Exception thrown
		# validate_json_string('[]')
		# validate_json_string('[{}]')
		# validate_json_string('[{"player": "one", "score": 199}]')

		# try:
		# 	# Throws frappe.ValidationError
		# 	validate_json_string('invalid json')
		# except frappe.ValidationError:
		# 	frappe.throw('Not a valid JSON string')
		pass

		
