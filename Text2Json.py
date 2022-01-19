import argparse, json


js = {}
p = argparse.ArgumentParser(description="Text to Json convertor !")
p.add_argument("--key", help="Key for json", metavar="", nargs='*')
p.add_argument("--value", help="Value for json", metavar="", nargs='*')
p.add_argument("--multiply", action="store_true", help="Print multiply jsons in an interactive mode")
args = p.parse_args()


def txt2json(valued, keyed):
    return json.dumps({keyed,valued})


def get_key(x):
    keys = []
    key1 = ""
    for j in x:
        if j != "," and j != x[-1]:
            key1 = key1 + j + " "
        elif j == x[-1]:
            key1 = key1 + j
            keys.append(key1)
        else:
            keys.append(key1)
            key1 = ""
    return keys


try:
    if args.multiply or not args.key or not args.value:
        try:
            while True:
                key = input("\nKey : ")
                value = input("Value : ")
                js[key] = value
        except KeyboardInterrupt:
            print("\nThank you for using, have a great day !")
            print(json.dumps(js))
    else:
        keys = get_key(args.key)
        values = get_key(args.value)
        if len(keys) == len(values):
            for i in range(len(values)):
                js[keys[i]] = values[i]
            print("\nThank you for using, have a great day !")
            print(json.dumps(js))
except Exception as e:
    print("Sorry, there was an error while running.\nPlease try again later.\nError Code : " + str(e))
