import frappe
from frappe.model.document import Document

class MoldProduction(Document):

    def on_submit(self):
        self.update_production_order_on_submit()

    def on_cancel(self):
        self.revert_production_order_on_cancel()

    def update_production_order_on_submit(self):
        if not self.production_orders:
            return

        po = frappe.get_doc("Production Orders", self.production_orders)

        # Update production values
        po.completed_quantity += self.completed_quantity
        po.remaining_quantity = po.production_quantity - po.completed_quantity

        # Update status
        if po.completed_quantity >= po.production_quantity:
            po.status = "Completed"
        else:
            po.status = "In Progress"

        po.save()
        self.status = "Completed"
		# self.docstatus = 2

    def revert_production_order_on_cancel(self):
        if not self.production_orders:
            return

        po = frappe.get_doc("Production Orders", self.production_orders)

        # Reverse the quantities
        po.completed_quantity -= self.completed_quantity
        po.remaining_quantity += self.completed_quantity

        # Recalculate status
        if po.completed_quantity <= 0:
            po.status = "Draft"
        else:
            po.status = "In Progress"

        po.save()
