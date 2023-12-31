﻿Wlan-Guide

Overview

This Python program is designed to extract the SSID (Service Set Identifier) and password of Wi-Fi profiles stored on a Windows computer. It automates the retrieval of Wi-Fi credentials by leveraging the Windows netsh command-line tool, writing the details into a text file for the user's reference.

Pre-requisites

The script must be run with Administrator privileges.
The Wi-Fi service (wlansvc) must be running on the computer.

Detailed Explanation:

1.Starting the Wi-Fi Service (wlansvc)

The start_wlansvc function attempts to start the WLAN AutoConfig service (wlansvc) if it's not already running. This service is essential for managing Wi-Fi profiles on a Windows system.

2.Extracting Wi-Fi Credentials

The extract_wifi_credentials function is where the main logic resides.

Creating a Password File:
The function begins by creating (or clearing, if it already exists) a file named passwords.txt, where it will write the Wi-Fi credentials.

Running the netsh Command:
It then executes a netsh command to export the profiles of all Wi-Fi networks stored on the system to XML files with their passwords in clear text (only if the user has previously connected to the Wi-Fi and the password was saved).

Parsing the XML Files:
The program iterates over all the generated XML files, which start with "Wi-Fi" and end with ".xml", to find the SSID and passwords contained within.

Writing Credentials to File:
For each Wi-Fi profile, the SSID and password are extracted from the XML file and written into the passwords.txt file in a readable format.

3.Main Execution

The script is executed if it's the main program that's running. It starts by calling the extract_wifi_credentials function