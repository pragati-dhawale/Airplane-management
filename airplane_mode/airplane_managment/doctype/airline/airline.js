// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });


frappe.ui.form.on('Airline', {
    refresh(frm) {
       const website = frm.doc.website ;
       frm.add_web_link(website, "Visit Website");
    }
});


