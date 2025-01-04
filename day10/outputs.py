def format_name(f_name, l_name):
  '''
  Take a first and last name and format it to return the title case version of the name
  Args:
    f_name (str): The first name
    l_name (str): The last name
  Returns:
    str: The formatted name
  '''
  return f"{f_name} {l_name}".title()

print(format_name("john", "smith"))