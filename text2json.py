import sys, json

global value2, key2, file_arg
value2, key2 = "", ""


if "--help" in sys.argv:
    print("Two arguments are required, --key & --value.\nExample : python text2json --key Error number 3 --value unrecognized file name")
    quit()


def validate():
    try:
        if sys.argv[1] == "--help":
            return True
    except IndexError:
        print("No enough arguments were given !\nAt least 4 arguments are needed. (--value <value> --key <key>)")
        return False
    if "--key" not in sys.argv or "--value" not in sys.argv:
        return False
    else:
        return True


def txt2json(values, keys):
    js = {
        values: keys
    }
    return js


if __name__ == "__main__":
    if validate():
        args = {}
        for i in range(1, 100):
            try:
                if sys.argv[i] == '--value':
                    x = sys.argv[i]
                    value = i
                    args["Value"] = i
                elif sys.argv[i] == '--key':
                    y = sys.argv[i]
                    args["Key"] = i
                elif sys.argv[i] == '--file':
                    file_arg = i
                elif sys.argv[i].upper().isupper():
                    args["Last"] = i
            except:
                continue
        for i in range(list(sorted(list(args.values())))[0] + 1, list(sorted(list(args.values())))[1]):
            value2 = value2 + sys.argv[i] + " "
        for i in range(list(sorted(list(args.values())))[1] + 1, list(sorted(list(args.values())))[2] - 1):
            key2 = key2 + sys.argv[i] + " "

        if "--file" in sys.argv:
            try:
                with open(sys.argv[file_arg+1], "a+") as file:
                    file.write(json.dumps(txt2json(values=value2, keys=key2)) + "\n")
                print("Json was wrote into " + sys.argv[file_arg + 1] + " successfully !\nJSON :")
                print(json.dumps(txt2json(values=value2, keys=key2)))
            except:
                print("Error, please try again.")
        else:
            print(json.dumps(txt2json(values=value2, keys=key2)))
    else:
        print("Invalid arguments were given.")