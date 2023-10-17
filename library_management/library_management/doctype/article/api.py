import frappe

@frappe.whitelist()
def get_article_details(article_id=True):
    return frappe.db.sql(f"""SELECT article_name FROM tabArticle where owner='Administrator';""", as_dict=True)



