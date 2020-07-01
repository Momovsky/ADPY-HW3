class Contact:
  def __init__(self, name, surname, telephone, fav_cont=False, *args, **kwargs):
    self.name = name
    self.surname = surname
    self.telephone = telephone
    self.fav_cont = fav_cont
    self.args = args
    self.kwargs = [(f'{key}: {item}') for key, item in kwargs.items()]

  def __str__(self):
    my_n = '\n\t'
    return(f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: {self.telephone}\nВ избранных: {"да" if self.fav_cont else "нет"}\nДополнительная информация:{my_n + ", ".join(self.args) if self.args else ""}{my_n + my_n.join(item for item in self.kwargs) if self.kwargs else ""}{my_n + "Нет" if not self.args and not self.kwargs else ""}')

class PhoneBook:
  def __init__(self, name):
    self.name = name
    self.contact_list = []

  def contact_output(self):
    for Contact in self.contact_list:
      print(Contact)
  
  def add_contact(self, Contact):
    self.contact_list.append(Contact)
  
  def del_by_number(self, number):
    for Contact in self.contact_list:
      if Contact.telephone == number:
        self.contact_list.remove(Contact)

  def find_favs(self):
    for Contact in self.contact_list:
      if Contact.fav_cont == True:
        print(Contact.telephone)

  def find_contact(self, name, surname):
    for Contact in self.contact_list:
      if Contact.name == name and Contact.surname == surname:
        print(Contact.telephone)
