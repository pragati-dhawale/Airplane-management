// Copyright (c) 2024, Pragati Dhawale and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {
//     amount(frm)
// 	},
// });


// Assuming dateStr is the date string you want to parse
// var momentDate = moment(dateStr, "YYYY-MM-DD HH:mm:ss"); // Adjust the format according to your date string

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add custom button to assign seat
        frm.add_custom_button(__('Assign Seat'), function() {
            // Show dialog box
            frappe.prompt([
                {'fieldname': 'seat_number', 'fieldtype': 'Data', 'label': __('Enter Seat Number'), 'reqd': true}
            ],
            function(values){
                // Set seat number to Seat field in form
                frm.set_value('seat', values.seat_number);
            },
            __('Seat Assignment'),
            __('Assign')
            );
        });
    }
});





