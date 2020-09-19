import pandas as pd

#due to VSCode pylint limitations, must use absolute path, change in release or when using locally
neighbourhoods = pd.read_csv('C:/Users/lavao/Documents/GitHub/HackMIT-2020/datasets/Toronto_Neighbourhood.csv')
#print (neighbourhoods.head())

neighbourhoods.drop(["Neighbourhood ID"], axis = 1, inplace = True)
#neighbourhoods.drop(["Missing Address/Postal Code"], axis = 0, inplace = True)

#higher count neighbourhood, sorted by descending
higher_count = neighbourhoods.sort_values(by=['Case Count'], ascending=False)
danger_zone = higher_count['Neighbourhood Name'].head(n=6).tolist()

#list comprehension, using lists in place of df
danger_zone[:] = [x for x in danger_zone if "Missing Address/Postal Code" not in x]

#slimming
while (len(danger_zone) > 5):
    del (danger_zone[-1])

#opens absolute path danger.txt in write mode and prints each item of list
with open("C:/Users/lavao/Documents/GitHub/HackMIT-2020/scripts/danger.txt", "w") as output_file:
   for item in danger_zone:
       output_file.write(str(item + '\n'))

#lower count neighbourhood, sorted by ascending
lower_count = neighbourhoods.sort_values(by=['Case Count'], ascending=True)
safety_zone = lower_count['Neighbourhood Name'].head(n=6).tolist()
safety_zone[:] = [x for x in safety_zone if "Missing Address/Postal Code" not in x]

while (len(safety_zone) > 5):
    del (safety_zone[-1])

with open("C:/Users/lavao/Documents/GitHub/HackMIT-2020/scripts/safety.txt", "w") as output_file:
   for item in safety_zone:
       output_file.write(str(item + '\n'))

if __name__ == '__main__':
    print(danger_zone)
    print(safety_zone)