import frappe
from frappe.model.document import Document
from frappe import _
import random
import string
from frappe.utils.data import cint

class AirplaneTicket(Document):

    def validate(self):
        self.calculate_total()
        self.check_capacity()
        self.validate_add_ons()

    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.seat = self.generate_seat()

    def generate_seat(self):
        random_integer = random.randint(1, 99)
        random_alphabet = random.choice('ABCDE')
        seat = str(random_integer) + random_alphabet
        return seat

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw(_("Airplane Ticket cannot be submitted unless the status is 'Boarded'."))

    def validate_add_ons(self):
        unique_add_ons = {}
        for add_on in self.add_ons:
            key = add_on.item
            if key not in unique_add_ons:
                unique_add_ons[key] = add_on

        self.set("add_ons", list(unique_add_ons.values()))
        self.calculate_total()

    def calculate_total(self):
        total = 0
        for row in self.add_ons:
            total += cint(row.amount)
        self.total_amount = total + self.flight_price

    def check_capacity(self):
        if self.flight:
            ticket_count = frappe.db.count("Airplane Ticket", 
                                       filters={"flight": self.flight, 
                                                "name": ("!=", self.name) if self.name else None})

        flight = frappe.get_doc("Airplane Flight", self.flight)
        if flight:
            airplane = frappe.get_doc("Airplane", flight.airplane)
            if ticket_count >= airplane.capacity:
                frappe.throw("Number of tickets exceeds or equals airplane capacity. Cannot create Airplane Ticket.")
