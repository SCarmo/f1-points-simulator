# first thing to do is get all races for each year
import xml.etree.ElementTree as ET
import requests

def getSeasons():
    response = requests.get("http://ergast.com/api/f1/2021/5/results")
    print(response.text)

    startYear = 1950
    endYear = 2020

    for i in range(startYear, endYear+1):
        response = requests.get("http://ergast.com/api/f1/" + str(i))
        # save responses to files
        f = open("Seasons/" + str(i) + ".xml", "a")
        f.write(response.text)

    f.close()

def main():
    # getSeasons()

if __name__ == "__main__":
    # execute only if run as a script
    main()
