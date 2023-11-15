import csv

movies = {}
ratings = {}
people_that_we_need = []

input_film = input()
film_id = 0
film_genre = 0

with open("movies.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            count = 0
        else:
            if row[0] not in movies.keys():
                movies[row[0]] = []

            movies[row[0]].append(row[1])
            movies[row[0]].append(row[2])
            movies[row[0]].append(0)

            if row[1] == input_film:
                film_id = row[0]
                film_genre = row[2]
        count += 1

with open("ratings.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count = 0
    for row in file_reader:
        if count == 0:
            count = 0
        else:
            if row[0] not in ratings.keys():
                ratings[row[0]] = []
            ratings[row[0]].append([row[1], row[2], row[3]])
            if (row[1] == film_id) and (4.0 <= float(row[2]) <= 5.0):
                people_that_we_need.append(row[0])
        count += 1

for row in people_that_we_need:
    for i in ratings[row]:
        if (4.0 <= float(i[1]) <= 5.0) and (i[0] != film_id) and (movies[i[0]][1] == film_genre):
            movies[i[0]][2] += 2 * float(i[1])
        elif (4.0 <= float(i[1]) <= 5.0) and (i[0] != film_id):
            movies[i[0]][2] += float(i[1])

for i in movies.keys():
    if movies[i][1] == film_genre:
        movies[i[0]][2] += 0.5 * float(i[1])


sorted_movies = []

for i in movies.keys():
    if movies[i][2] != 0:
        sorted_movies.append((movies[i][2], movies[i][0]))

sorted_movies.sort()
sorted_movies = sorted_movies[::-1]

n = 0
for i in sorted_movies:
    print(i)
    n += 1
    if n == 20:
        break