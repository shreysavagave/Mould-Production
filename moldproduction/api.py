# import frappe

# @frappe.whitelist()
# def update_production_order_completed_quantity(production_order, pattern, completed_quantity):
#     doc = frappe.get_doc("Production Orders", production_order)

#     for row in doc.production_details:
#         if row.pattern == pattern:
#             row.completed_quantity = completed_quantity
#             row.remaining_quantity = row.production_quantity - completed_quantity
#             break
#     else:
#         frappe.throw("Pattern not found in Production Order.")

#     doc.save(ignore_permissions=True)
#     frappe.db.commit()
#     return "Updated"



import frappe

@frappe.whitelist()
def update_production_order_completed_quantity(production_order, pattern, completed_quantity):
    po = frappe.get_doc("Production Orders", production_order)

    # Convert completed_quantity to float
    completed_quantity = float(completed_quantity)

    for row in po.production_details:
        if row.pattern == pattern:
            row.completed_quantity = completed_quantity
            row.remaining_quantity = row.production_quantity - completed_quantity
            break

    total_production_quantity = sum(row.production_quantity for row in po.production_details)
    total_completed_quantity = sum(row.completed_quantity for row in po.production_details)
    total_remaining_quantity = total_production_quantity - total_completed_quantity

    po.total_production_quantity = total_production_quantity
    po.total_completed_quantity = total_completed_quantity
    po.total_remaining_quantity = total_remaining_quantity

    po.save()
    frappe.db.commit()

    return {
        "total_production_quantity": total_production_quantity,
        "total_completed_quantity": total_completed_quantity,
        "total_remaining_quantity": total_remaining_quantity
    }
