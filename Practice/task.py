class Ticket:
    tickets_created = 0
    tickets_resolved = 0
    tickets_to_solve = 0

    def __init__(self, creator_name, staff_id, email, description):
        Ticket.tickets_created += 1
        self.ticket_number = Ticket.tickets_created + 2000
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        if "Password Change" in description:
            self.resolve_password_change()

    def resolve_password_change(self):
        self.response = f"New password generated: {self.staff_id[:2]}{self.creator_name[:3]}"
        self.status = "Closed"
        Ticket.tickets_resolved += 1

    @classmethod
    def print_statistics(cls):
        print("\nDisplaying Ticket Statistics")
        print(f"Tickets Created: {cls.tickets_created}")
        print(f"Tickets Resolved: {cls.tickets_resolved}")
        print(f"Tickets To Solve: {cls.tickets_created - cls.tickets_resolved}")

    def print_ticket(self):
        print("\nPrinting Tickets:")
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Ticket Creator: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Ticket Status: {self.status}")


# Creating ticket instances
ticket1 = Ticket("Subin", "Shrestha", "subin@whitecliffe.co.nz", "My monitor stopped working")
ticket2 = Ticket("Simeera", "Pradhan", "Simeera@whitecliffe.co.nz", "Request for a videocamera to conduct webinars")
ticket3 = Ticket("Sarita", "Maharjan", "sarita@whitecliffe.co.nz", "Password change")

# Resolving ticket 3 manually
ticket3.response = "New password generated: SARITA"
ticket3.status = "Pending"  # Changing status to Pending

# Manually resolving ticket 2
ticket2.resolve_password_change()

# Printing ticket statistics
Ticket.print_statistics()

# Printing ticket information
ticket1.print_ticket()
ticket2.print_ticket()
ticket3.print_ticket()
