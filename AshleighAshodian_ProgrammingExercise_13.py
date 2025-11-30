import sqlite3
import matplotlib.pyplot as plt
import random

#create a database called population_AA
def create_database():
    conn = sqlite3.connect("population_AA.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS population(
          city TEXT,
          year INTEGER,
          population INTEGER
          )""")
    conn.commit()
    conn.close()


#Insert 2023 data if it doesn't already exist
def year_2023_data():
    conn = sqlite3.connect("population_AA.db")
    cur = conn.cursor()

    cities_2023 = [
        ("Sarasota", 2023, 576234),
        ("Pensacola", 2023, 607235),
        ("Orlando", 2023, 655840),
        ("Ocala", 2023, 349802),
        ("Tallahassee", 2023, 344169),
        ("Siesta Key", 2023, 421509),
        ("Miami Beach", 2023, 267833),
        ("St. Petersburg", 2023, 399081),
        ("Fort Lauderdale", 2023, 301005),
        ("Tampa", 2023, 564000),
    ]

    #check for existing 2023 entries
    for city, year, pop in cities_2023:
        cur.execute(
            "SELECT COUNT(*) FROM population WHERE city=? AND year=?", (city, year)
        )
        if cur.fetchone()[0] == 0:
            cur.execute(
                "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                (city, year, pop)
            )

    conn.commit()
    conn.close()
    return cities_2023  #returns the cities and their populations


#simulate population growth for 20 years
def simulate_pop(cities_2023):
    conn = sqlite3.connect("population_AA.db")
    cur = conn.cursor()

    for city, _, pop_2023 in cities_2023:
        population = pop_2023
        for year in range(2024, 2024 + 20):
            # randomize growth or decline between -2% and 6% each year
            growth_rate = random.uniform(-0.02, 0.06)
            population = int(population * (1 + growth_rate))
            cur.execute(
                "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                (city, year, population),
            )

    conn.commit()
    conn.close()


#show the population plot
def show_pop_plot():
    conn = sqlite3.connect("population_AA.db")
    cur = conn.cursor()

    #show user list of available cities
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    print("Available cities:")
    for c in cities:
        print(c)
    #prompts user to enter a city from the list shown
    city_choice = input("Enter the name of a city to view its population (case sensitive): ")

    #incase they enter a city not on the list or make a typo
    if city_choice not in cities:
        print("City not found.")
        conn.close()
        return

    cur.execute(
        "SELECT year, population FROM population WHERE city = ? ORDER BY year",
        (city_choice,),
    )
    rows = cur.fetchall()
    conn.close()

    years = [r[0] for r in rows]
    populations = [r[1] for r in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker='o', linestyle='-', color='blue')
    plt.title(f"Population Growth for {city_choice}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()


#main program
def main():
    create_database()
    cities_2023 = year_2023_data()      #insert 2023 data and get city list
    simulate_pop(cities_2023)    #simulate the next 20 years
    show_pop_plot()              #display plot for the city the user selects

if __name__ == "__main__":
    main()
