# Create new shopping list (the new list should have a title)
# Edit list's name
# See all items
# Add new item
# Exit

# shopping list
# Food shopping list+ gift shopping list

import email

class ShoppingList:

  def __init__(self):
    self.contents = []

  def add_item(self, item):
    self.contents.append(item)

  def mark_achieved(self, item):
    for this_item in self.contents:
      if this_item == item:
        self.contents.remove(item)
    else: return "Not found"


class FoodShoppingList(ShoppingList):

  def __init__(self):
    super().__init__()
    self.contents.append("pizza")

class GiftShoppingList(ShoppingList):

  def __init__(self):
    super().__init__()

  def email_gift_reciept(self, gift):
    email.message['subject'] = 'Python roolz!'
    email.message['body'] = 'Wow, this email thing is real and pretty awesome. There is more to it than this, but it actually is an easy way to construct and send emails!'



kroger_list = FoodShoppingList()

print(kroger_list.contents)

kroger_list.mark_achieved("pizza")

print(kroger_list.contents)

gift_list = GiftShoppingList()

gift_list.add_item("Myrrh")

gift_list.add_item("Frankincense")

print(gift_list.contents)

gift_list.mark_achieved("Frankincense")

print(gift_list.contents)
