# beneficiary.py

beneficiaries = []
next_id = 1

def add_beneficiary(name, card_no, family_size, category):
    global next_id
    beneficiary = {
        "id": next_id,
        "name": name,
        "card_no": card_no,
        "family_size": family_size,
        "category": category
    }
    beneficiaries.append(beneficiary)
    print("✅ Beneficiary added successfully!")
    next_id += 1


def view_beneficiaries():
    if not beneficiaries:
        print("No beneficiaries found.")
        return
    print("\n--- Beneficiaries List ---")
    for b in beneficiaries:
        print(f"ID: {b['id']}, Name: {b['name']}, Card No: {b['card_no']}, Family Size: {b['family_size']}, Category: {b['category']}")


def update_beneficiary(id, name, family_size, category):
    for b in beneficiaries:
        if b["id"] == id:
            b["name"] = name
            b["family_size"] = family_size
            b["category"] = category
            print("✅ Beneficiary updated successfully!")
            return
    print("❌ Beneficiary not found.")


def delete_beneficiary(id):
    for b in beneficiaries:
        if b["id"] == id:
            beneficiaries.remove(b)
            print("✅ Beneficiary deleted successfully!")
            return
    print("❌ Beneficiary not found.")
