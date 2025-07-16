from pydantic import BaseModel, EmailStr 

class Contact(BaseModel):
    name: str
    email: EmailStr
    phone: str
    active: bool = True

#Because this class manages multiple contacts, just store a list of contacts inside the class instead
class ContactBookClass:
    def __init__(self):
        self.contacts = []

    #method to add a contact
    def add_contact(self, contact):
        self.contacts.append(contact)

    #first parameter is the contacts object referred to as self. Second is the input from the user
    #none is an optional paramter to be passed.
    def delete_contact(self, name: str= None, email: str = None):
        for contact in self.contacts:
            if ((name and contact.name.lower() == name.lower())
                 or (email and contact.name.lower() == email.lower())
                ):
                contact.active = False
                print(f"{name} has been marked inactive.")
                return
        print("Contact not found")
            
    def show_contacts(self):
        """Shows all contacts if they are active"""
        active_contacts = [c for c in self.contacts if c.active]
        sorted_contacts = sorted(active_contacts, key=lambda c: c.name.lower())  
        for contact in sorted_contacts:
            print(contact.dict())          



      
#Test block
if __name__=="__main__":
    book = ContactBookClass()
    contact = Contact(name="Bob", email="marie@example.com", phone="1234567890")
    book.add_contact(contact)
    print(book.contacts)
    book.delete_contact(name="Marie")
    book.show_contacts()