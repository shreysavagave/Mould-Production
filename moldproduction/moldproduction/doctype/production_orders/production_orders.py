# Copyright (c) 2025, shrey and contributors
# For license information, please see license.txt



import frappe
from frappe.model.document import Document

class ProductionOrders(Document):
    def validate(self):
        self.set_totals()

    def set_totals(self):
        total_production = 0
        total_completed = 0

        for row in self.production_details:
            # Convert safely
            production_qty = float(row.production_quantity or 0)
            completed_qty = float(row.completed_quantity or 0)

            row.remaining_quantity = production_qty - completed_qty

            total_production += production_qty
            total_completed += completed_qty

        self.total_production_quantity = total_production
        self.total_completed_quantity = total_completed
        self.total_remaining_quantity = total_production - total_completed
