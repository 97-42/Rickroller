import os
import shutil
import webbrowser

def add_startup_entry():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    shortcut_name = "Google.lnk"
    target_path = os.path.join(startup_folder, shortcut_name)

    try:
        # Create a shortcut file in the Startup folder
        with open(target_path, 'w') as shortcut_file:
            shortcut_file.write("[InternetShortcut]\n")
            shortcut_file.write("URL=https://www.youtube.com/watch?v=dQw4w9WgXcQ\n")

        print("Google.com added to startup successfully.")

    except Exception as e:
        print("Error adding Google.com to startup:", str(e))

# Call the function to add the startup entry
add_startup_entry()

# Open the default browser with Google.com
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
