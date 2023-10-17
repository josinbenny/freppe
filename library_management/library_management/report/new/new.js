// Copyright (c) 2023, Josin Benny and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["new"] = {
	"filters": [
		{
			"fieldname":"article_name",
			"label":("Article"),
			"fieldtype":"Link",
			"options":"Article"
		},
		{
			"fieldname":"author",
			"label":("Author"),
			"fieldtype":"Data"
		}

	]
};