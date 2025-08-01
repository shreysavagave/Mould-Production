// Copyright (c) 2025, shrey and contributors
// For license information, please see license.txt



frappe.ui.form.on('Mold Production', {
    production_order: function(frm) {
        if (frm.doc.production_order) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Production Orders',
                    name: frm.doc.production_order
                },
                callback: function(r) {

                    if (r.message) {

                        let production_rows = r.message.production_details;

                        frm.clear_table('production_details');  // child table fieldname

                        production_rows.forEach(row => {
                            let child = frm.add_child('production_details');
                            child.pattern = row.pattern;
                            child.production_quantity = row.production_quantity;
                            child.completed_quantity = 0; // default value
                        });

                        frm.refresh_field('production_details');
                    }
                }
            });
        }
    }
});


frappe.ui.form.on('Mold Production Details', {
    completed_quantity: function(frm, cdt, cdn) {
        let child = locals[cdt][cdn];
        console.log('Completed quantity changed:', child.completed_quantity);

        // Now call your server method to update Production Order child table
        frappe.call({
            method: 'moldproduction.moldproduction.api.update_production_order_completed_quantity',
            args: {
                production_order: frm.doc.production_order,
                pattern: child.pattern,
                completed_quantity: child.completed_quantity
            },
            callback: function(r) {
                if (!r.exc) {
                    frappe.show_alert({message: 'Production Order updated', indicator: 'green'});
                }
            }
        });
    }
});
