## 1. Reading our MoMA Data Set ##

from csv import reader

# Read the `artworks_clean.csv` file
opened_file = open('artworks_clean.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

# Convert the birthdate values
for row in moma:
    birth_date = row[3]
    if birth_date != "":
        birth_date = int(birth_date)
    row[3] = birth_date
    
# Convert the death date values
for row in moma:
    death_date = row[4]
    if death_date != "":
        death_date = int(death_date)
    row[4] = death_date

# Write your code below

for row in moma:
    date = row[6]
    if date != "":
        date = int(date)
    row[6] = date 

## 2. Calculating Artist Ages ##

ages = []
for row in moma:
    date = row[6]
    birth = row[3]
    if type(birth)!= int:
        age = 0
        
    else:
        age = date - birth
    ages.append(age)
        
final_ages = []
for age in ages:
    if age > 20:
        final_age = age 
    else:
        final_age = "Unknown"
    final_ages.append(final_age)
  
    
         
    
    

## 3. Converting Ages to Decades ##

# The ages variable is available
# from the previous screen
decades = [ ]
for age in ages:
    if age == "Unknown":
        decade = age
    else:
        decade = str(age)
        decade = decade[:-1]
        decade = decade +"0s"
    decades.append(decade)
    
  

## 4. Summarizing the Decade Data ##

# The decades variable is available
# from the previous screen
decade_frequency = { }
for decade in decades:
    if decade in decade_frequency:
        decade_frequency[decade] += 1
    else:
        decade_frequency[decade] = 1



## 5. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881
template = "{painter}'s birth year is {year}"
message = template.format(painter =artist,year= birth_year)
print (message)

## 6. Creating an Artist Frequency Table ##

artist_freq = { } 
for row in moma:
    artist = row[1]
    if artist in artist_freq:
        artist_freq[artist] += 1
    else:
        artist_freq[artist] = 1

## 7. Creating an Artist Summary Function ##

def artist_summary(artist):
    print (artist)
    num_artworks = artist_freq[artist]
    output = "There are {num} artworks by {painter} in the data set"
    print (output.format(num=num_artworks, painter = artist))
     
artist_summary("Henri Matisse")
           
   

## 8. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]
template = "The population of {} is {:,.2f} million"

for country in pop_millions:
    name = country[0]
    popul = country[1]
    output = template.format(name, popul)
    print (output)
                    
                                                  

## 9. Challenge: Summarizing Artwork Gender Data ##

gender_freq = { }
for row in moma:
    gender = row[5]
    if gender in gender_freq:
        gender_freq[gender] += 1
    else:
        gender_freq[gender] = 1
        
for gender,freq in gender_freq.items():
    output = "There are {q:,} artworks by {g} artists".format(q = freq, g = gender)
    print (output)
                                                          
 