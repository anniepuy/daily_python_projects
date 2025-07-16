# Contact Manager

## Purpose

Simple contact manager that user can add, list, delete contacts.
Each contact has a name, phone number, and email.

## Project Breakdown

Functional or OOP?
OOP because it has stateful objects which are the contacts

Components

1. Contact Objects

- Need email, phone, and name validation
- Use Pyndantic models for type validation

2. Methods

- Add method to add to the items
- Delete to 'soft -delete' - tag the item as inactive
- Retrieve or list all the items

Flow using CLI:
START: CLI prompts user "Welcome to contact manager. Would you like to (a) add, (d) delete, or (l) list the contacts?" Based on user a, d, or l selection, the result is shown in the CLI.
For ADDING: User is prompted to enter name, email, and phone number.
For DELETING: Need a way to seach, view, and select a contact.
For VIEW: Method to pull all contacts in JSON format alphabetically.
