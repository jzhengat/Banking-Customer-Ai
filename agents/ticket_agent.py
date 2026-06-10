from database import create_ticket, get_ticket

def handle_complaint(message):
    ticket_id = create_ticket(message)

    return f"""

    Your ticket has been created.

    Ticket ID: {ticket_id}
    """


def check_ticket(ticket_id):
    ticket = get_ticket(ticket_id)

    if not ticket:
        return "ERROR: ticket not found"

    return f"""
    Ticket ID: {ticket[0]}
    Issue: {ticket[1]}
    Status: {ticket[2]}
    """