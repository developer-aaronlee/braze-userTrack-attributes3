import pandas as pd
import requests
import json

braze_track = "https://rest.iad-06.braze.com/users/track"

track_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer api_key"
}

df = pd.read_csv("easterseals_attribute.csv")
# print(df.values)

all_data = [x[0] for x in df.values]
# print(all_data)

n = 0
for x in all_data[::]:
    n += 1
    track = {
        "attributes":
            [{
                "external_id": x,
                "initial_source": "easterseals"
            }]
    }

    track_user = json.dumps(track)
    # print(f"Row {n}:", track_user)

    # response = requests.post(url=braze_track, data=track_user, headers=track_headers)
    # print(f"Row {n}: {x} Response: ", response.json())

