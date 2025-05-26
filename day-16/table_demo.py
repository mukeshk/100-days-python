from prettytable import  PrettyTable
from typing_inspection.typing_objects import te_alias

table = PrettyTable()
table.add_column("Pokeman Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["electric","water","fire"])

table.align='l'
print(table.align)
print(table)