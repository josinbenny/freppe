# Copyright (c) 2023, Josin Benny and contributors
# For license information, please see license.txt
import frappe


def execute(filters=None):
	if not filters:filters = {}

	columns, data = [], []

	columns = get_columns()
	cs_data = get_cs_data(filters)

	if not cs_data:
		frappe.msgprint(('No records found'))
		return columns, cs_data
	
	data=[]
	for d in cs_data:
		row = frappe._dict({
				'article_name':d.article_name,
				'author':d.author
			})
		data.append(row)

	chart=get_chart_data(data)
	return columns,data

def get_columns():
	return [
		{
			'fieldname':'article_name',
			'label':('Article Name'),
			'fieldtype':'Data',
			'width':120
		},
		{
			'fieldname':'author',
			'label':('Author Name'),
			'fieldtype':'Data',
			'width':120
		}
	]

def get_cs_data(filters):
	conditions = get_conditions(filters)
	data= frappe.get_all(
		doctype='Article',
		fields=['article_name','author'],
		filters=conditions,
		order_by='article_name desc'
	)
	return data

def get_conditions(filters):
	conditions = {}
	for key, value in filters.items():
		if filters.get(key):
			conditions[key] = value
		
	return conditions

def get_chart_data(data):
	if not data:
		return None
	