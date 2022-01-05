import sys, json

global value2, key2, file_arg
value2, key2, file_arg = "", "", 0
js = {}
keys = []
values = []

if "--help" in sys.argv:
    print("In order to run the convertor with arguments two arguments are required, --key & --value.")
    print("Example : python text2json --key Error number 3 --value unrecognized file name\n")
    print("Or simply run the script without arguments for infinity convert ;)")
    quit()


def validate():
    try:
        if sys.argv[1] == "--help":
            return True
    except IndexError:
        print("No arguments were given !")
        return False
    if "--key" not in sys.argv or "--value" not in sys.argv:
        print("Wrong arguments were given !")
        return False
    else:
        return True


def txt2json(valued, keyed):
    js[keyed] = valued
    return js


if __name__ == "__main__":
    if validate():
        args = {}
        for i in range(1, 100):
            try:
                if sys.argv[i].lower() == '--key':
                    x = i + 1
                    args["Key"] = i
                elif sys.argv[i].lower() == '--value':
                    y = i + 1
                    args["Value"] = i
                elif sys.argv[i].lower() == '--file':
                    file_arg = i + 1
                elif sys.argv[i].upper().isupper():
                    z = i + 1
                    args["Last"] = i
            except:
                continue
        if x > y:
            print("Wrong order, please use :\npython Text2Json.py --key <key> --value <value>")
            quit()
        if file_arg != 0:
            for i in range(y, file_arg - 1):
                key2 = key2 + sys.argv[i] + " "
        else:
            for i in range(y, z):
                key2 = key2 + sys.argv[i] + " "
        for i in range(x, y - 1):
            value2 = value2 + sys.argv[i] + " "
        if "--file" in sys.argv:
            with open(sys.argv[file_arg], "a+") as file:
                file.write(json.dumps(txt2json(valued=value2, keyed=key2)) + "\n")
            print("Json was wrote into " + sys.argv[file_arg] + " successfully !\nJSON :")
            print(json.dumps(txt2json(valued=value2, keyed=key2)))
        else:
            print(json.dumps(txt2json(valued=value2, keyed=key2)))
    else:
        manual = input("Start manual converting ?\n[Yes/.../Help] : ")
        if manual.lower() == "yes":
            file = input("Append JSON into a file ?\n[Yes/...] : ")
            if file.lower() == "yes":
                file = input("File Name : ")
                filed = True
            else:
                filed = False
            try:
                while input("PRESS ENTER TO CONTINUE OR PRESS CTRL + C TO STOP !") == "":
                    print(keys, values)
                    key = input("\nEnter Key : ")
                    keys.append(key)
                    value = input("Enter Value : ")
                    values.append(value)
            except KeyboardInterrupt:
                for i in range(len(keys)):
                    txt2json(keyed=keys[i], valued=values[i])
                if filed:
                    with open(file, "a+") as file1:
                        file1.write(json.dumps(js) + "\n")
                    print("Json was wrote into " + file + " successfully !\nJSON :")
                    print(json.dumps(js))
                else:
                    print("JSON : \n")
                    print(json.dumps(js))
                print("\nThank you for using !")
                quit()
        elif manual.lower() == "help":
            print("In order to run the convertor with arguments two arguments are required, --key & --value.")
            print("Example : python text2json --key Error number 3 --value unrecognized file name\n")
            print("Or simply run the script without arguments for infinity convert ;)")
            quit()
        else:
            print("Please try again with the arguments --key <key> --value <value>")
