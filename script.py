from datetime import time

class Franchise:
        def __init__(self, address, menus):
            self.address = address
            self.menus = menus
        def __repr__(self):
            return self.address
        def available_menus(self, time):
            available_menus = []
            for menu in self.menus:
                if time >= menu.start_time and time <= menu.end_time:
                 available_menus.append(menu)
            return available_menus

class Business:
        def __init__(self, name, franchises):
            self.name = name
            self.franchises = franchises
                     
class Menu:
        def __init__(self, name, items, start_time, end_time):
            self.name = name
            self.items = items
            self.start_time = start_time
            self.end_time = end_time
        def __repr__(self):
            return self.name + ' Menu akan tersedia dari jam ' + str(self.start_time) + ' sampai jam ' + str(self.end_time)
        def calculate_bill(self, purchased_items):
            price = 0
            for purchased_items in purchased_items:
                if purchased_items in self.items:
                 price += self.items[purchased_items]
            return price  

#Create menu 1
brunch_meal = {
        'pancakes': 7.50, 
        'waffles': 9.00, 
        'burger': 11.00, 
        'home fries': 4.50, 
        'coffee': 1.50, 
        'espresso': 3.00,
        'tea': 1.00, 
        'mimosa': 10.50, 
        'orange juice': 3.50
}
brunch_start_times = time(hour=11, minute=00).isoformat(timespec='minutes')#Create start time
brunch_end_times = time(hour=16, minute=00).isoformat(timespec='minutes')#Create end time
brunch_menu = Menu('brunch', brunch_meal, brunch_start_times, brunch_end_times)
print(brunch_menu)
print('Total pesanannya adalah:', brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']), '\n')#Total price

#Create menu 2 
early_bird_items = {
        'salumeria plate': 8.00, 
        'salad and breadsticks (serves 2, no refills)': 14.00, 
        'pizza with quattro formaggi': 9.00,
        'duck ragu': 17.50, 
        'mushroom ravioli (vegan)': 13.50,
        'coffee': 1.50,
        'espresso': 3.00   
}
early_bird_start_times = time(hour=15, minute=00).isoformat(timespec='minutes')#Create start time
early_bird_end_times = time(hour=18, minute=00).isoformat(timespec='minutes')#Create end time
early_bird_menu = Menu('early bird', early_bird_items, early_bird_start_times, early_bird_end_times)
print(early_bird_menu)
print('total pesanannya adalah:', early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']),'\n')

#Create menu 3
dinner_items= {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}
dinner_start_times = time(hour=17, minute=00).isoformat(timespec='minutes')#Create start time
dinner_end_times = time(hour=23, minute=00).isoformat(timespec='minutes')#Create end time
dinner_menu = Menu('dinner', dinner_items, dinner_start_times, dinner_end_times)
print(dinner_menu)
print('total pesanannya adalah:', dinner_menu.calculate_bill(['crostini with eggplant caponata', 'caesar salad', 'coffee']),'\n')

#Create menu 4
kids_meal = {
  'chicken nuggets': 6.50,      
  'fusilli with wild mushrooms': 12.00,
  'apple juice': 3.00
}
kids_start_times = time(hour=11, minute=00).isoformat(timespec='minutes')#Create start time
kids_end_times = time(hour=21, minute=00).isoformat(timespec='minutes')#Create end time
kids_menu = Menu('kids', kids_meal, kids_start_times, kids_end_times)
print(kids_menu)
print('total pesanannya adalah:', kids_menu.calculate_bill(['chicken nuggets', 'apple juice']),'\n')

#Create menus for showing this in all franchise
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

#Create address for flagship store 
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)
arepas_place = Franchise("189 Fitzgerald Avenue", menus)
brunch_and_kids = time(hour=11, minute=00).isoformat(timespec='minutes')
dinner_and_kids = time(hour=19, minute=00).isoformat(timespec='minutes')
#Expect "brunch Menu akan tersedia dari jam 11:00 sampai jam 16:00" and "kids Menu akan tersedia dari jam 11:00 sampai jam 21:00"
print(flagship_store.available_menus(brunch_and_kids))
print(flagship_store.available_menus(dinner_and_kids))

#Create new menu
arepas_items = {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 
    'jamon arepa': 7.50
}
arepas_start_time = time(hour=10, minute=00).isoformat(timespec='minutes')
arepas_end_time = time(hour=20, minute=00).isoformat(timespec='minutes')
basta = Business("Basta Fazoolin' with my hear", [flagship_store, new_installment, arepas_place])
arepas_menu = Business("Take a' Arepa", arepas_items, arepas_start_time, arepas_end_time)
print(arepas_menu.franchises[0])