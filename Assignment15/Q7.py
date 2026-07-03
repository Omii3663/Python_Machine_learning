String_length = lambda s : len(s) > 5

def main():
    list_str = ['Apple','banana','chiku','watermelon','orange']

    FData = list(filter(String_length,list_str))
    print("List of String with length is grater then 5 :",FData )

if __name__ == "__main__":
    main()