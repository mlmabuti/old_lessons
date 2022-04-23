def recursion(sub_string, main_string):
    if len(sub_string) > len(main_string):
        return False  # because substring should always be bigger

    if sub_string == main_string[0:len(sub_string)]:
        return True  # because substring has been found

    # else continue trimming the main string
    return recursion(sub_string, main_string[1:])


def main():
    print(recursion("abcd", "aksdjaklsdjaklsdjasbcbcd"))


if __name__ == "__main__":
    main()
