import frappe

@frappe.whitelist()
def update_production_order_completed_quantity(production_order, pattern, completed_quantity):
    doc = frappe.get_doc("Production Orders", production_order)

    for row in doc.production_details:
        if row.pattern == pattern:
            row.completed_quantity = completed_quantity
            break
    else:
        frappe.throw("Pattern not found in Production Order.")

    doc.save(ignore_permissions=True)
    frappe.db.commit()
    return "Updated"