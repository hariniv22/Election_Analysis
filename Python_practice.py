print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

if "Araphoe" and "El Paso" in counties:
    print("Arapahoe and El Paso are in counties list")
else:
    print("Arapahoe or El Paso are not in the counties list")
if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso in the list of counties")
else:
    print("Arapahoe and El Paso not in the list of counties")
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for n in numbers:
    print(n)
for num in range(5):
    print (num)
for num in range(len(counties)):
    print (counties[num])

counties_tuple = ("Alpahoe", "Denver", "Jefferson")
print (len(counties_tuple))
for county in counties_tuple:
    print (county)
print(counties_tuple[0])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
print("DICTIONARY....")
for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))
print("KEY:VALUE PAIR")
for key,value in counties_dict.items():
    print(key + " county has " + str(value) + " voters")
    print(f"{key} county has {value:,} voters.........")

print("----------------------------------------------------")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for data in voting_data:
    print(data)
    for value in data.values():
        print(value)
    for key, value in data.items():
        print(f"{key} county has {value} registered voters............")
for county_dict in voting_data:
    county = county_dict["county"]
    registered_voters = county_dict["registered_voters"]
    print(f"county {county} has {registered_voters:,} registered voters")

my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("How many votes are there in total?"))
percentage_votes = (my_votes/total_votes)*100
#print("I received " + str(percentage_votes) + "% of total votes")
print(f"I received {percentage_votes} %of total votes")
print("--------------------------------")
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
candidate_messages = {
    f"You received {candidate_votes:,} votes in the election. "
    f"There are total of {total_votes:,} votes in the election. "
    f"You received {candidate_votes/total_votes * 100:.2f} percentage of votes"
}
print(candidate_messages)
