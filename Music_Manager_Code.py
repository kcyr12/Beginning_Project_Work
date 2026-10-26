
## Music Collection Manager in Python ##

#Create a program that can organize a music collection in Python. The program must use classes, attributes and methods as needed to provide the following functionality:
# Add a new user: Prompt the user to enter a new username, and create a new user with that name. Each user must have their own distinct music collection.
# Change users: Allow a different user to take over as the active user, with further changes happening on this user's collection.
# Add a song: Prompt the user to enter the song title and artist, and add it to the music collection.
# Retrieve song details: Prompt the user to enter a song title, and display the corresponding artist from the music collection.
# Update song details: Prompt the user to enter a song title, and update the artist information in the music collection.
# Delete a song: Prompt the user to enter a song title, and remove the corresponding song from the music collection.
# Display all songs: Display the titles of all songs in the music collection.
# Exit: Allow the user to exit the program.
# Include a driver block that provides a simple menu asking the user to select from the above options or quit.

# Begin creating user class 

class User:
   
    def __init__(self, username):
        self.username = username
        self.collection = {}   

    
    def add_song(self, title, artist):
        self.collection[title] = artist
        print(f"Added '{title}' by {artist}.")

    
    def retrieve_song(self, title):
        if title in self.collection:
            print(f"'{title}' is by {self.collection[title]}.")

        else:
            print(f"Song '{title}' not found.")

    
    def update_song(self, title, new_artist):
        if title in self.collection:
            self.collection[title] = new_artist
            print(f"Updated '{title}' to new artist: {new_artist}.")

        else:
            print(f"Song '{title}' not found.")

    
    def delete_song(self, title):
        if title in self.collection:
            del self.collection[title]
            print(f"Deleted '{title}'.")

        else:
            print(f"Song '{title}' not found.")

    
    def display_songs(self):
        if not self.collection:
            print("No songs in this collection.")

        else:
            print("Songs in collection:")
            for title in self.collection:
                print(f" - {title}")


# Begin MusicManager class


class MusicManager:


    def __init__(self):
        self.users = {}
        self.active_user = None
    

    def show_users(self):
        if not self.users:
            print("No users currently exist.")

        else:
            print("Current users:")
            for username in self.users:
                print(f" - {username}")
    
    
    def add_user(self):
        username = input("Enter new username: ").strip()
        if username in self.users:
            print("User already exists.")

        else:
            self.users[username] = User(username)
            print(f"User '{username}' created.")
            print("\nUpdated user list:")
            self.show_users()

    
    def change_user(self):
        username = input("Enter username to switch to: ").strip()
        if username in self.users:
            self.active_user = self.users[username]
            print(f"Active user changed to '{username}'.")

        else:
            print("User not found.")

    
    def require_active_user(self):
        if self.active_user is None:
            print("No active user. Please add or switch to a user first.")
            return False
        
        return True
    

# Begin main function


def main():
    manager = MusicManager()

    print("\n" + "=" * 40)
    print("     WELCOME TO THE MUSIC MANAGER")
    print("=" * 40)

    manager.show_users()

    while True:
        print("\n" + "=" * 40)
        print("        MUSIC COLLECTION MENU")
        print("=" * 40)


# Show if no users exist yet


        if not manager.users:
            print("1) Add a new user")
            print("2) Exit")
            print("=" * 40)
            choice = input("Select an option (1-2): ").strip()

            if choice == "1":
                manager.add_user()

            elif choice == "2":
                print("Exiting program. Goodbye.")
                break

            else:
                print("Invalid option.")
            continue


# Show if users exist, but no active user selected


        if manager.active_user is None:
            print("1) Add a new user")
            print("2) Change active user")
            print("3) Exit")
            print("=" * 40)
            choice = input("Select an option (1-3): ").strip()

            if choice == "1":
                manager.add_user()

            elif choice == "2":
                manager.change_user()

            elif choice == "3":
                print("Exiting program. Goodbye.")
                break
            
            else:
                print("Invalid option.")
            continue


# Active user selected — show full menu


        print(f"Active user: {manager.active_user.username}")
        print("1) Add a song")
        print("2) Retrieve song details")
        print("3) Update song details")
        print("4) Delete a song")
        print("5) Display all songs")
        print("6) Change active user")
        print("7) Add a new user")
        print("8) Exit")
        print("=" * 40)

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            title = input("Enter song title: ").strip()
            artist = input("Enter artist: ").strip()
            manager.active_user.add_song(title, artist)

        elif choice == "2":
            title = input("Enter song title: ").strip()
            manager.active_user.retrieve_song(title)

        elif choice == "3":
            title = input("Enter song title: ").strip()
            new_artist = input("Enter new artist: ").strip()
            manager.active_user.update_song(title, new_artist)

        elif choice == "4":
            title = input("Enter song title: ").strip()
            manager.active_user.delete_song(title)

        elif choice == "5":
            manager.active_user.display_songs()

        elif choice == "6":
            manager.change_user()

        elif choice == "7":
            manager.add_user()

        elif choice == "8":
            print("Exiting program. Goodbye.")
            break

        else:
            print("Invalid option.")


main()