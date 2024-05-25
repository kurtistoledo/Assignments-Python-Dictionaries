# Lesson 1: Python Dictionaries
# 3. Python Programming Challenges for Customer Service Data Handling

class TicketTracker:
    def __init__(self):
        # Initialize the ticket tracker with sample tickets
        self.service_tickets = {
            "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
            "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
        }

    def open_ticket(self, ticket_id, customer_name, issue_description):
        """
        Open a new service ticket.
        """
        if ticket_id not in self.service_tickets:
            self.service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
            print(f"New ticket {ticket_id} opened for {customer_name}: {issue_description}")
        else:
            print(f"Ticket {ticket_id} already exists.")

    def update_status(self, ticket_id, new_status):
        """
        Update the status of an existing ticket.
        """
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = new_status
            print(f"Ticket {ticket_id} status updated to {new_status}.")
        else:
            print(f"Ticket {ticket_id} does not exist.")

    def display_tickets(self, status_filter=None):
        """
        Display all tickets or filter by status.
        """
        print("Service Tickets:")
        for ticket_id, ticket_info in self.service_tickets.items():
            if status_filter is None or ticket_info["Status"] == status_filter:
                print(f"{ticket_id}: {ticket_info['Customer']} - {ticket_info['Issue']} ({ticket_info['Status']})")

# Example usage
if __name__ == "__main__":
    ticket_system = TicketTracker()
    ticket_system.open_ticket("Ticket003", "Charlie", "Network connectivity issue")
    ticket_system.update_status("Ticket001", "closed")
    ticket_system.display_tickets(status_filter="open")
