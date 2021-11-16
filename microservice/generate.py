import random


class GenerateData:

    def generate_json(self):
        json = []
        for _ in range(10):
            num = random.randint(1, 100)
            object = {
                'id': f"{num}",
                'name': f"test{num}"
            }
            json.append(object)

        return json
