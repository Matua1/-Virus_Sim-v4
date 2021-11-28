#Data Storage
names = []
infected = []

#Data creation
print("Welcome to Pap High's Virus Simulator.\nPlease follow the promtps.\nPlease enter a name of country or /done/ if you wish to exit.  ")
name_input = input()
while name_input != "done":
  names.append(name_input)
  print("Please enter the number of infected percentage for the country. ")
  infected_input = int(input())
  infected.append(int(infected_input))
  print(names,infected)
  print("Please enter a name of country or /done/ if you wish to exit.  ")
  name_input = input()


#Modify/Adjusting Data
number_of_countries = len(names)
for i in range(number_of_countries):
  print(" You may type the following to help: Country A | Country B | Country C to help or q to Quit.")
  help_input = input()
  while help_input != "q" or "Q":
      if help_input == "Country A" or "A":
        print("Country A health increases by 40%  while Country B and C decreases by 20%")
        amount = input()
        infected[i] += int(amount)

      elif help_input == "Country B" or 'b':
        print("Country B health increases by 40% while Country A and C decreases by 20%")

      elif help_input == "Country C" or 'c':
        print("Country C health increases by 40% while Country A and B decreases by 20%")
        print(" You may type the following to help: Country A | Country B | Country C to help or q to Quit.")
        help_input = input()

  #Output Data
  for i in range(number_of_countries):
    print(names[i])
    if infected[i] >= 50:
      print(names[i], infected[i], "and is in lockdown")
    elif infected[i] <= 49:
      print(names[i],"is at:", infection[i],"and is NOT in Lock down!")
    else:
      print(names[i], infected[i])



      






