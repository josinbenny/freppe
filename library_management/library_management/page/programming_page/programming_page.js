frappe.pages['programming-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Demo Page',
		single_column: true
	});

	page.set_title('My Page')
	page.set_indicator('Done', 'red')
	let $btn = page.set_primary_action('New', () =>frappe.msgprint("Clicked new"), 'octicon octicon-plus')
	let $btnone = page.set_secondary_action('Refresh', () =>frappe.msgprint("Clicked refresh"), 'octicon octicon-plus')
	page.add_menu_item('send Email', ()=> frappe.msgprint('Clicked email'))
	page.add_action_item('Delete', ()=> frappe.msgprint('Clicked Delete'))
	let field = page.add_field({
		label:'Status',
		fieldtype:'Select',
		fieldname:'status',
		options:[
				'Open',
				'Closed',
				'Cancelled'
			],
		change(){
			frappe.msgprint(field.get_value());
		}
	})


} 