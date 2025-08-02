// frappe.ui.form.on("Mold Production", {
//     production_order(frm) {
//         if (frm.doc.production_order) {
//             frappe.call({
//                 method: "frappe.client.get",
//                 args: {
//                     doctype: "Production Orders",
//                     name: frm.doc.production_order
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frm.set_value("shift", r.message.shift);
//                         frm.set_value("operator", r.message.operator);
//                         frm.set_value("date", r.message.date);
//                         frm.set_value("remaining_quantity", r.message.remaining_quantity);
//                     }
//                 }
//             });
//         }
//     }
// });