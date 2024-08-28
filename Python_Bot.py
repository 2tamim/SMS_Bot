from datetime import datetime
import sys
from colorama import Fore
import xlrd
import time
import warnings
import requests
from xml.etree import ElementTree as ET

warnings.filterwarnings("ignore", category=DeprecationWarning)

logf = open("sms.log", "w")

sms_list = ("Numbers.xls")



def send_sms(domain, username, password, phone, message, link):
    try:

        url = f"http://www.test.ir/sms.aspx?&action=send&domainname={domain}&username={username}&password={password}&mobilenos={phone}&body={message}\n\n{link}"
        # print(url)
        headers = ""

        response = requests.request("POST", url)
        # Parse XML response
        root = ET.fromstring(response.text)
        status_code = response.status_code
        message = root.find('Message').text.strip()  # Get the text inside <Message>

        return status_code, message

        time.sleep(4)
    except Exception as e:
        logf.write(str(e))
    finally:
        pass


def sms():
    try:
        # Get user input for dc, user, and password
        dc = input("Enter DC: ")
        user = input("Enter User: ")
        password = input("Enter Password: ")
        message = input("Enter message: ")

        print("\n")
        print(Fore.YELLOW + "[" + str(
            datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + "Start Sending")

        wb = xlrd.open_workbook(sms_list)  # Assuming sms_list is defined somewhere in your code
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)

        for i in range(sheet.nrows):
            if not i == 0:
                number = sheet.cell_value(i, 0)
                print(Fore.YELLOW + "[" + str(
                    datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + "Number: " + number)
                link = sheet.cell_value(i, 1)
                # print(link)

                main_func = send_sms(dc, user, password, number, message, link)  # Assuming send_sms function exists
                print(main_func)

    except Exception as e:
        # Handle exceptions or log them appropriately
        logf.write(str(e))
    finally:
        # Clean up or finalize operations if needed
        pass

def bye():
    print(Fore.BLUE + "[" + str(datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + "Bye my friend")
    exit()


def sched():
    try:
        start_time = str(input(Fore.YELLOW + "["+str(datetime.now().replace(second=0, microsecond=0))+"] " + "[inf] " + "When to start the program? "))
        end_time = str(input(Fore.YELLOW + "["+str(datetime.now().replace(second=0, microsecond=0))+"] " + "[inf] " + "When to end the program? "))
        print(Fore.RED + "["+str(datetime.now().replace(second=0, microsecond=0))+"] "+ "[inf] " +"app running between "+ start_time+" and  "+ end_time+" ...")



        done = 'false'

        # here is the animation
        def animate():
            inp_time = start_time
            h = inp_time.split(":", 1)[0]
            m = inp_time.split(":", 1)[1]
            inp = datetime.now().replace(hour=int(h), minute=int(m) - 1)
            while done == 'false':
                sys.stdout.write(Fore.BLUE + "\r[" + str(datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + 'loading |')
                time.sleep(0.1)
                sys.stdout.write(Fore.BLUE + "\r[" + str(datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + 'loading /')

                time.sleep(0.1)
                sys.stdout.write(Fore.BLUE + "\r[" + str(datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + 'loading -')
                time.sleep(0.1)
                sys.stdout.write(Fore.BLUE + "\r[" + str(datetime.now().replace(second=0, microsecond=0)) + "] " + "[inf] " + 'loading \\')
                time.sleep(0.1)
                if inp < datetime.now():
                    break
        animate()
        done = 'false'



        while True:
            time.sleep(1)
    except Exception as e:
        logf.write(str(e))
    finally:
        pass


if __name__ == "__main__":
    print(Fore.BLUE +"""
    ███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ████████╗
    ██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
    ███████╗██╔████╔██║███████╗    ██████╔╝██║   ██║   ██║   
    ╚════██║██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║   ██║   
    ███████║██║ ╚═╝ ██║███████║    ██████╔╝╚██████╔╝   ██║   
    ╚══════╝╚═╝     ╚═╝╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                         
                           version : 1.0.0
    --------------------------------------------------------------
    
    --------------------------------------------------------------

    """)
    sms()
    time.sleep(10)