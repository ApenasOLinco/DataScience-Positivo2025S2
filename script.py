import csv

if __name__ == '__main__':
    with open('./world_imdb_movies_top_movies_per_year.csv', newline='', mode='r', encoding="utf8") as database:
        spamreader = csv.reader(database, delimiter=',')

        for row in spamreader:
            print(', '.join(row))