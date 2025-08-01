import frappe
from frappe.model.document import Document

class MoldProduction(Document):
    def on_submit(self):
        self.update_production_order_quantities()

    def update_production_order_quantities(self):
        if not self.production_order:
            return

        # Get the linked Production Order
        production_order = frappe.get_doc("Production Order", self.production_order)

        # Initialize completed quantity
        total_completed_qty = 0

        # Fetch all submitted Mold Production entries linked to this Production Order
        mold_productions = frappe.get_all(
            "Mold Production",
            filters={"production_order": self.production_order, "docstatus": 1},
            fields=["name"]
        )

        # Sum up produced_qty from each mold production's child table
        for mold in mold_productions:
            mold_doc = frappe.get_doc("Mold Production", mold.name)
            for item in mold_doc.child_table:  # <-- changed to child_table
                total_completed_qty += item.produced_qty  # Make sure this field exists in the child table

        # Update completed and remaining quantities in Production Order
        production_order.completedquantity = total_completed_qty
        production_order.remainingquantity = production_order.totalquantity - total_completed_qty

        production_order.save()
        frappe.msgprint("✅ Production Order updated successfully.")
