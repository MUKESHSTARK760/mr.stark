import subprocess

def get_saved_wifi_passwords():
    # Get a list of all saved Wi-Fi profiles
    profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    
    profiles = [line.split(":")[1].strip() for line in profiles_data if "All User Profile" in line]
    
    wifi_passwords = {}

    for profile in profiles:
        # Extract the password for each Wi-Fi profile
        profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password_line = [line.split(":")[1].strip() for line in profile_info if "Key Content" in line]

        wifi_passwords[profile] = password_line[0] if password_line else None

    return wifi_passwords

if __name__ == "__main__":
    passwords = get_saved_wifi_passwords()

    if passwords:
        for profile, password in passwords.items():
            print(f"Wi-Fi Profile: {profile}")
            if password:
                print(f"Password: {password}")
            else:
                print("Password: No password set or hidden")
            print("-" * 30)
    else:
        print("No Wi-Fi profiles found on this device.")
