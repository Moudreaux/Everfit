import requests
import json
from trainer.trainers import Trainer


if __name__ == "__main__":
    headers = {
        "Content-Type": "application/json",
        "x-hasura-admin-secret": "unv9y631mTMBOe95zBZixiWJaUpZ9CvWT9pDOX9DWZKvd3hNwXOSRwkuYi9yIrVl"
    }
    url = "https://everfit.hasura.app/v1/graphql"
    body = ""
    query = """{
                  classes(order_by: {day: asc, hour: asc}) {
                    Profe:Trainer {
                      firstname
                      lastname
                      photo
                    }
                    Dia:dayByDay {
                      day_name
                    }
                    Hora:hour
                    Clase:classType {
                      type_name
                      minutes
                    }
                  }
                }"""
    response = requests.post(url=url, headers=headers, json={'query': query}).text
    data = json.loads(response).get('data', {})
    if data:
        classes = data.get('classes')
        for c in classes:
            t = Trainer(**c.get('Profe'))
            print(t)
        print(json.dumps(data, indent=4, sort_keys=True))
    else:
        print(f"Error contacting endpoint.")
        print(f"URL:{url}")
        print(json.dumps(json.loads(response).get('errors'), indent=4, sort_keys=True))
