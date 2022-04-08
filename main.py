"""
Latest Earthquake Apps
"""


def extract_data():
    update = dict()
    update["date"] = "7 April 2022"
    update["time"] = "16:52:58"
    update["depth"] = 118
    update["location"] = {"LU": 6.01, "BT": 125.79}
    update["source"] = "244 km BaratLaut MELONGUANE-SULUT"
    return update


def visualize_data():
    print("Latest Earthquake of Indonesia")
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : {result['location']}")
    print(f"Source : {result['source']}")


if __name__ == '__main__':
    print("Main Apps")
    result = extract_data()
    visualize_data(result)
