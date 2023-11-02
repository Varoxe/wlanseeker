import subprocess
import sys

def start_wlansvc():
    try:
        # Trying to start the wlan service
        print("Try, to start wlansvc...")
        subprocess.run(["sc", "start", "wlansvc"], check=True)
        print("wlansvc started....")
    except subprocess.CalledProcessError:
        print("Problems with starting wlansvc. Try starting it manually.")
        sys.exit(1)

def extract_wifi_credentials():
    # Looking if the wlan service is running
    start_wlansvc()


def extract_wifi_credentials():
    # Create or overwrite the file with the initial text
    with open("passwords.txt", "w") as password_file:
        password_file.write("Hello Sir! Here are your passwords:\n\n")

    # Try to execute the command
    try:
        # You need to ensure that this script is being run as an administrator
        subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

    # Extracting the credentials from the .xml files
    path = os.getcwd()
    for filename in os.listdir(path):
        if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
            with open(filename, "r", errors='ignore') as file:
                ssid, password = None, None
                for line in file:
                    if "<name>" in line:
                        ssid = line.split("<name>")[1].split("</name>")[0]
                    if "<keyMaterial>" in line:
                        password = line.split("<keyMaterial>")[1].split("</keyMaterial>")[0]
                        break  # No need to continue reading the file

                # Writing credentials to file
                if ssid and password:
                    with open("passwords.txt", "a") as password_file:
                        password_file.write(f"SSID: {ssid}\nPassword: {password}\n\n")

    print("Wi-Fi credentials have been extracted to passwords.txt.")


if __name__ == "__main__":
    extract_wifi_credentials()