# Ticket Management System

Ticket Management System Overview. This Python script displays a basic ticket management system. It enables users to generate tickets for various requests or challenges, maintain records of the amount of tickets created and addressed, and print ticket data.

Features Ticket Creation: Users can create tickets with information such as the creator's name, staff ID, email address, and a description of the issue/request. Ticket Resolution: The ticket can be resolved automatically if a password change request is stated in the description. Otherwise, tickets may be resolved manually. Ticket Statistics: The system tracks the number of tickets created, resolved, and pending. Ticket Information: Users may print out full information on the purchased tickets.

Installation Python 3. x download the repository to your local machine.

Usage Launch a program called terminal or command prompt. You can go to the folder where the script (ticket_management.py) is submitted. Run the script using Python 3. python ticket_management.py

Instructions for Users When the script goes through execution, three ticket instances are immediately created with examples of data. Ticket descriptions with "Password Change" will be automatically managed with a generated password. To manually resolve a ticket, edit the response assets with the resolution information. Change the status of assets to "Pending" or "Closed" as required. Use the Ticket class' print_statistics() work to print ticket statistics. To print specific information about each ticket, use the print_ticket() function on the ticket object.

Contributors [Subin Shrestha]

License This project has been licensed under the MIT Licence; read the LICENCE file for additional information.
