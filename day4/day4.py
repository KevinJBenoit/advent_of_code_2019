
def valid_passwords(start, end):
    count = 0
    for password in range(start, end):
        list_password = [int(digit) for digit in str(password)]

        #make a sorted copy of the password
        sorted_list = sorted(list_password.copy())

        if list_password == sorted_list:
            for num in list_password:
                if list_password.count(num) == 2:
                    count += 1
                    break

    return count

def main():
    """
    main
    """
    print(valid_passwords(134792, 675810))



if __name__ == "__main__":
    main()
