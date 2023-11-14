import random
import matplotlib.pyplot as plt

num_thieves = 10
def generate_thief_info(num_thieves, weight_limit=10000):
    available_items = (
    ('phone', 150, 20000),
    ('tablets', 300, 15000),
    ('watch', 200, 5000),
    ('ring', 30, 3500),
    ('tv', 8000, 25000),
    ('laptop', 1500, 30000),
    ('camera', 500, 18000),
    ('headphones', 200, 2500),
    ('keyboard', 500, 1500),
    ('mouse', 100, 500),
    ('monitor', 3000, 7000),
    ('printer', 5000, 4000),
    ('scanner', 3500, 3500),
    ('desk', 10000, 5000),
    ('chair', 8000, 3000),
    ('lamp', 500, 1000),
    ('backpack', 500, 2000),
    ('wallet', 100, 800),
    ('sunglasses', 50, 1500),
    ('hat', 100, 500),
    ('shoes', 500, 2000),
    ('coat', 1000, 3000),
    ('gloves', 50, 800),
    ('bicycle', 12000, 7000),
    ('helmet', 400, 1500),
    ('skateboard', 2000, 3000),
    ('ball', 500, 500),
    ('racket', 300, 1500),
    ('drone', 1000, 10000),
    ('usb_drive', 20, 500),
    ('hard_drive', 500, 3000),
    ('ssd', 200, 4000),
    ('router', 500, 2500),
    ('modem', 400, 2000),
    ('speaker', 1000, 5000),
    ('microphone', 300, 2000),
    ('webcam', 150, 1500),
    ('smartwatch', 75, 10000),
    ('earbuds', 50, 2500)
    )

    thief_info = []
    
    for i in range(num_thieves):
        weight_in_bag = 0
        thief_bag = []
        
        while weight_in_bag <= weight_limit:
            random_item_tuple = random.choice(available_items)
            if weight_in_bag + random_item_tuple[1] <= weight_limit:
                weight_in_bag += random_item_tuple[1]
                thief_bag.append(random_item_tuple)
            else:
                break

        total_value = sum(item[2] for item in thief_bag)
        thief_info.append((f'thief_{i + 1}-{j+1}', thief_bag, total_value))

    return thief_info

def sort_thieves_by_fitness(thief_info):
    return sorted(thief_info, key=lambda x: x[2], reverse=True)

def crossover_thieves_greedy_from_top(sorted_thieves, weight_limit):
      # Sort thieves by their fitness value and pick the top two
      top_thief1 = sorted_thieves[0]
      top_thief2 = sorted_thieves[1]

      # Combine items from both top thieves and sort by value-to-weight ratio
      combined_items = list(set(top_thief1[1] + top_thief2[1]))  # Using set to avoid duplicates
      combined_items.sort(key=lambda item: item[2]/item[1], reverse=True)  # Sort by value-to-weight ratio

      new_bag = []
      current_weight = 0

      # Greedily add items to the bag
      for item in combined_items:
          if current_weight + item[1] <= weight_limit:
              new_bag.append(item)
              current_weight += item[1]

      total_value = sum(item[2] for item in new_bag)
      return (f'off_spring-{j + 1}', new_bag, total_value)
new_generation = []
average_fitness_values = []

#specifies the number of generation to run for
for j in range(0,5000):
  # store variables
  thief_info = generate_thief_info(num_thieves)
  sorted_thieves = sort_thieves_by_fitness(thief_info)

  offspring = crossover_thieves_greedy_from_top(sorted_thieves, weight_limit)
  new_generation.append(offspring)
  generation_count = 1
  while generation_count < num_thieves:
    new_generation.append(sorted_thieves[generation_count])
    generation_count += 1
  sorted_thieves2 = sort_thieves_by_fitness(new_generation)
  #prints out generation number
  print('generation' + str(j+1))
  generation_survival = 0
  total_fitness = 0
  #loops through all thieves for the generation
  for thief in sorted_thieves2:
      generation_survival += 1
      print(f'{thief[0]} - Total Fitness Value: {thief[2]}')
      total_fitness += thief[2]
      if generation_survival >= 10:
          break #automatically eliminates the thieves with low fitness value
  average_fitness = total_fitness/10
  average_fitness_values.append(average_fitness)
  print(f"                 Generational average fitness value: {average_fitness}")
  new_generation.clear()
  new_generation = sorted_thieves2
plt.plot(average_fitness_values, marker='o')
plt.title("Average Fitness Value per Generation")
plt.xlabel("Generation")
plt.ylabel("Average Fitness Value")
plt.show()







