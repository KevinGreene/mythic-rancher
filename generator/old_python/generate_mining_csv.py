f = open('data/mining.csv', 'w')

header = "name,primary_resource,secondary_resource,tertiary_resource"

card_lines = [header]

energy_types = [
    "Fire",
    "Gas",
    "Oil",
    "Uranium",
    "Coal",
    "Trash",
]

energy_count = len(energy_types)


def format_resource(element, value):
    return element + ": " + value

# 1 type - 1
for j in range(3):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "1"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          "",
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)


for j in range(2):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "2"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          "",
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)

for j in range(2):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "3"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          "",
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)

for j in range(1):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "5"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          "",
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)

for j in range(1):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "1"
       secondary_element = energy_types[(i+1) % energy_count]
       secondary_value = "1"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          format_resource(secondary_element, secondary_value),
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)

    
for j in range(1):
   for i in range(energy_count):
       primary_element = energy_types[i]
       primary_value = "2"
       secondary_element = energy_types[(i + 3) % energy_count]
       secondary_value = "1"
       
       card_line_array = ["Resources!",
                          format_resource(primary_element, primary_value),
                          format_resource(secondary_element, secondary_value),
                          "",
       ]
       card_line = ",".join(card_line_array)
   
       card_lines.append(card_line)
       
for card_line in card_lines:
    f.write(card_line)
    f.write("\n")
