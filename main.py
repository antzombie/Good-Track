# # # # # # # # # # # # #
# # #  GOOD - TRACK # # #
# # # # # # # # # # # # #
import json
import os
import webbrowser
import requests
import banner
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def main():
    clear()
    banner.banner1()
    print('[01] Track IP')
    print('[02] Track Self IP')
    print('[03] Open Github Page')
    print('[04] Exit')
    print('')
    command = input("TRACK> ")
    if str(command) == "03" or str(command) == "3":
        print("Opening Github...")
        webbrowser.open("https://github.com/ase3p")
        main()
    if str(command) == "02" or str(command) == "2":
        api_ip_url = "http://ip-api.com/json/"
        api_ip_response = requests.get(api_ip_url)
        ip_info = json.loads(api_ip_response.text)
        if str(ip_info['status']) == "success":
            print("IP FOUND")
            clear()
            banner.banner2()
            print("\n")
            print(f"Country: {ip_info['country']}")
            print(f"Country Code: {ip_info['countryCode']}")
            print(f"Region: {ip_info['region']}")
            print(f"Region Name: {ip_info['regionName']}")
            print(f"City: {ip_info['city']}")
            print(f"Zip Code: {ip_info['zip']}")
            print(f"Latitude: {ip_info['lat']}")
            print(f"Longitude: {ip_info['lon']}")
            print(f"Timezone: {ip_info['timezone']}")
            print(f"Internet Service Provider: {ip_info['isp']}")
            print(f"Organization: {ip_info['org']}")
            print(f"AS: {ip_info['as']}")
            print(f"IP-Adress: {ip_info['query']}")
            print(f"Google Maps URL: https://www.google.com/maps?q={ip_info['lat']},{ip_info['lon']}\n")
            again = input("TRACK AGAIN? [Y/n]> ")
            if again == "Y" or again == "y":
                main()
            else:
                print("Quiting...")
                exit
        else:
            print("Self Search UnSuccessful.\nQuitting...")
    if str(command) == "01" or str(command) == "1":
        ip = input("Input Victims IP adress: ")
        if str(ip) == "" or str(ip) == " ":
            print("No IP Provided.\nQuitting...")
            exit
        else:
            api_ip_url = str(f"http://ip-api.com/json/{ip}")
            api_ip_response = requests.get(api_ip_url)
            ip_info = json.loads(api_ip_response.text)
            if str(ip_info['status']) == "success":
                print("IP FOUND")
                clear()
                banner.banner2()
                print("\n")
                print(f"Country: {ip_info['country']}")
                print(f"Country Code: {ip_info['countryCode']}")
                print(f"Region: {ip_info['region']}")
                print(f"Region Name: {ip_info['regionName']}")
                print(f"City: {ip_info['city']}")
                print(f"Zip Code: {ip_info['zip']}")
                print(f"Latitude: {ip_info['lat']}")
                print(f"Longitude: {ip_info['lon']}")
                print(f"Timezone: {ip_info['timezone']}")
                print(f"Internet Service Provider: {ip_info['isp']}")
                print(f"Organization: {ip_info['org']}")
                print(f"AS: {ip_info['as']}")
                print(f"IP-Adress: {ip_info['query']}")
                print(f"Google Maps URL: https://www.google.com/maps?q={ip_info['lat']},{ip_info['lon']}\n")
                again = input("TRACK AGAIN? [Y/n]> ")
                if again == "Y" or again == "y":
                    main()
                else:
                    print("Quiting...")
                    exit
            else:
                print("IP Search UnSuccessful. Double Check if its the correct IP\nQuitting...")
    if str(command) == "04" or str(command) == "4":
        print('Quitting...')
        exit
main()
