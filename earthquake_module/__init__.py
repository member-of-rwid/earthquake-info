import requests
from bs4 import BeautifulSoup


def extract_data():
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        date_time = soup.find('span', {'class': 'waktu'})
        date = date_time.text.split(', ')[0]
        time = date_time.text.split(', ')[1]

        update = dict()
        update["date"] = date   #"7 April 2022"
        update["time"] = time   #"16:52:58"
        update["magnitude"] = 5.1
        update["depth"] = 118
        update["location"] = {"LU": 6.01, "BT": 125.79}
        update["source"] = "244 km BaratLaut MELONGUANE-SULUT"
        return update
    else:
        return None


def visualize_data(result):
    if result is None:
        print("Can't find the data")
        return
    print("Latest Earthquake of Indonesia")
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : LU = {result['location']['LU']}, BT = {result['location']['BT']}")
    print(f"Source : {result['source']}")
