# Copyright (c) 2023, Josin Benny and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class ServerClientsidescripting(Document):

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc=frappe.new_doc('Client Side Scripting')
	# 	doc.first_name='andrews'
	# 	doc.last_name='p'
	# 	doc.age=13
	# 	doc.append("family_members",{	"name1":"aaaa",
	# 						   			"relation":"brother",
	# 						   			"age":12
	# 						   })
	# 	doc.insert()
    
	# def get_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting',self.client_side)
	# 	frappe.msgprint(("the first name is {0} and age is {1}").format(doc.first_name,doc.age))

	# 	for row in doc.get("family_members"):
	# 		frappe.msgprint(("{0}. The family member name is '{1}' and the relation is {2} ").format(row.idx,row.name1,row.relation))

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', 'CR0005')

	# def validate(self):
	# 	self.db_set_document()
	# def db_set_document(self):
	# 	doc=frappe.get_doc('Client Side Scripting', 'CR0004')
	# 	doc.db_set('first_name','andrews')



	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc= frappe.db.get_list('Client Side Scripting',
	# 					  filters={
	# 						  'enable':1,
							
	# 					  },
	# 					  fields=['first_name','age']
	# 					  )
	# 	for d in doc:
	# 		frappe.msgprint(("the Parent name is {0} and age is {1}").format(d.first_name,d.age))	
	# @frappe.whitelist()	
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
	# 	frappe.msgprint(msg)
	# 	self.mobile_number=123456789
	# 	self.age=55
	# 	self.email="josin@gm.com"
	# 	return "Hi this message from call"



	# def validate(self):
	# 	self.get_list()
	
	# def get_list(self):
	# 	data=frappe.db.get_list('Server Client side scripting',
	# 			filters={
	# 				'enable':1
	# 			})

	# 	for d in data:
	# 		frappe.msgprint(("name is {0}").format(d.name))

	# def validate(self):
	# 	self.exists()

	# def exists(self):
	# 	# data=frappe.db.exists({"doctype":"Server Client side scripting","first_name":"josin"})
	# 	# data=frappe.db.exists("Server Client side scripting","SR0014",cache=True)
	# 	data=frappe.db.exists("Server Client side scripting",{'first_name':'josin'})	
	# 	if data:
	# 		frappe.msgprint("Data Available")


	# def validate(self):
	# 	self.count()

	# def count(self):
	# 	data=frappe.db.count("Server Client side scripting")
	# 	frappe.msgprint(("Count is {0}").format(data))

	# def validate(self):
	# 	self.describe()

	# def describe(self):
	# 	data=frappe.db.describe("Server Client side scripting")
	# 	frappe.msgprint(("Description is {0}").format(data))


	# def validate(self):
	# 	self.describe()

	# def describe(self):
	# 	data=frappe.db.describe("Server Client side scripting")
	# 	frappe.msgprint(("Description is {0}").format(data))

	# def validate(self):
	# 	self.truncate()

	# def truncate(self):
	# 	data=frappe.db.truncate("Fee paid")
	# 	frappe.msgprint("db cleared")

	# def validate(self):
	# 	self.last_doc()

	# def last_doc(self):
	# 	data=frappe.get_last_doc("Server Client side scripting")
	# 	frappe.msgprint(("last doc :- {0}").format(data))



	# def validate(self):
	# 	self.get_doc()

	# def get_doc(self):
	# 	data=frappe.get_doc('Server Client side scripting','SR0016')
	# 	frappe.msgprint(("doc :- {0}").format(data))
	pass
