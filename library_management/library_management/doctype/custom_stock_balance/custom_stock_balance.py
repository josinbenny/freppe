# Copyright (c) 2023, Josin Benny and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class CustomStockbalance(Document):
		

	def execute(filters=None):
		data = []

		# Fetch and calculate the data based on your criteria
		# Example query to get stock transactions
		stock_transactions = frappe.get_all("Stock Ledger Entry", filters)

		for entry in stock_transactions:
			item_code = entry.item_code
			item_name = entry.item_name
			stock_in = entry.in_qty if entry.actual_qty > 0 else 0
			stock_out = entry.out_qty if entry.actual_qty < 0 else 0

			data.append({
				"item_code": item_code,
				"item_name": item_name,
				"stock_in": stock_in,
				"stock_out": stock_out,
				"stock_balance": stock_in - stock_out
			})

		return data

