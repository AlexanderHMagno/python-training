import PrettyTable

table = PrettyTable.PrettyTable()

table.add_row(["Name", "Age", "Gender"])
table.add_row(["John", 25, "Male"])
table.add_row(["Jane", 23, "Female"])

print(table)