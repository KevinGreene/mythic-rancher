f = open('data/machines.csv', 'w')

header = "name,primary_cost,secondary_cost,conversion_value,explosion_cost"

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


# 2/1 for 1
for i in range(energy_count):
    conversion_value = "1"
    
    primary_element = energy_types[i]
    secondary_element = energy_types[(i + 1) % energy_count]
    primary_cost = primary_element + ": 2"
    secondary_cost = secondary_element + ": 1"
    explosion_element = energy_types[(i + 2) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       secondary_cost,
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)
 
# 2/1 for 1
for i in range(energy_count):
    conversion_value = "1"
    
    primary_element = energy_types[i]
    secondary_element = energy_types[(i + 4) % energy_count]
    primary_cost = primary_element + ": 2"
    secondary_cost = secondary_element + ": 1"
    explosion_element = energy_types[(i +1 ) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       secondary_cost,
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)


# 2/1 for 1
for i in range(energy_count):
    conversion_value = "1"
    
    primary_element = energy_types[i]
    secondary_element = energy_types[(i + 3) % energy_count]
    primary_cost = primary_element + ": 2"
    secondary_cost = secondary_element + ": 1"
    explosion_element = energy_types[(i +1 ) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       secondary_cost,
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)



# 3 for 1
for i in range(energy_count):
    conversion_value = "1"
    
    primary_element = energy_types[i]
    primary_cost = primary_element + ": 3"
    explosion_element = energy_types[(i + 3) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       "",
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)


# 3/1 for 2
for i in range(energy_count):
    conversion_value = "2"

    primary_element = energy_types[i]
    secondary_element = energy_types[(i + 3) % energy_count]
    primary_cost = primary_element + ": 3"
    secondary_cost = secondary_element + ": 1"
    
    explosion_element = energy_types[(i + 4) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       secondary_cost,
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)

    
    
# 4/2 for 3
for i in range(energy_count):
    conversion_value = "3"

    primary_element = energy_types[i]
    secondary_element = energy_types[(i + 2) % energy_count]
    primary_cost = primary_element + ": 4"
    secondary_cost = secondary_element + ": 2"
    
    explosion_element = energy_types[(i + 4) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       secondary_cost,
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)

# 5 for 3
for i in range(energy_count):
    conversion_value = "3"

    primary_element = energy_types[i]
    primary_cost = primary_element + ": 5"
    explosion_element = energy_types[(i + 1) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       "",
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)

# 7 for 7
for i in range(energy_count):
    conversion_value = "7"

    primary_element = energy_types[i]
    primary_cost = primary_element + ": 8"
    explosion_element = energy_types[(i + 5) % energy_count]
    explosion_cost = explosion_element + ": 7"
    
    card_line_array = ["Test Name",
                       primary_cost,
                       "",
                       conversion_value,
                       explosion_cost,
    ]
    card_line = ",".join(card_line_array)

    card_lines.append(card_line)

    

    
for card_line in card_lines:
    f.write(card_line)
    f.write("\n")
