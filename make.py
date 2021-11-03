import json

def make():
    print("DID NOT FIND DATA.JSON!")
    print("MAKING DATA.JSON...")


    a = input("Github username: ")
    b = input("Github secret key: ")

    data = {
        "usr":f"{a}",
        "pass":f"{b}"
    }

    dump = json.dumps(data, indent=2)

    with open("data.json", 'w') as f:
        f.write(dump)

