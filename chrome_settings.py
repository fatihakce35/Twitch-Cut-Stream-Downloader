
def chrome_settings():
    with open('driver//chrome_information.txt', 'r') as f:
        info_list=f.read()

        if len(info_list)!=0:
            info_list=info_list.split("\n")
            chrome_info={"version":info_list[0],"location":info_list[1]}
            return chrome_info
        else:
            chrome_version=int(input("Please enter your chrome version (99,100 or 101): "))
            chrome_location=input("Please enter your chrome profile location: ")
            chrome_info=[chrome_version,chrome_location]
            with open('driver//chrome_information.txt', 'w') as f:
                f.write(str(chrome_info[0]) +"\n" + chrome_info[1])
            print("Thank you. Now you can restart the program.")
            exit()
