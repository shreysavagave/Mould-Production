frappe.ui.form.on("Production Orders", {
    validate: function(frm) {
        frm.refresh_field("remaining_quantity");
    }
});