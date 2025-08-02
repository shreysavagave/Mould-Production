# Copyright (c) 2025, shrey and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ProductionOrders(Document):
    def validate(self):
        self.set_totals()

    def set_totals(self):
        self.remaining_quantity = self.production_quantity - self.completed_quantity
        frappe.msgprint(f"Prod: {self.production_quantity}, Completed: {self.completed_quantity}, Remaining: {self.remaining_quantity}")
