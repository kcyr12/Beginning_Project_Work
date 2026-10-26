
# Folder Storage Project

class Folder:
    
    def __init__(self, name, depth=0, parent=None):
        self.name = name
        self.files = []
        self.subfolders = []
        self.depth = depth
        self.parent = parent

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return False

    def add_file(self, filename):
        if filename in self.files:
            print(f"File '{filename}' already exists in '{self.name}'.")
            return
        
        self.files.append(filename)
        print(f"File '{filename}' added to '{self.name}'.")

    def add_subfolder(self, name):
        if self.depth >= 3:
            print("Cannot add more subfolders.")
            return
        
        for sf in self.subfolders:
            if sf == name:
                print(f"Subfolder '{name}' already exists in '{self.name}'.")
                return

        new_folder = Folder(name, depth=self.depth + 1, parent=self)
        self.subfolders.append(new_folder)
        print(f"Subfolder '{name}' added to '{self.name}'.")

    def select_folder(self, name):
        if self == name:
            return self

        for sf in self.subfolders:
            result = sf.select_folder(name)
            if result is not None:
                return result

        return None

    def __count_files(self):
        total = len(self.files)
        for sf in self.subfolders:
            total += sf.__count_files()
        return total

    def __len__(self):
        return self.__count_files()

    def __str__(self, level=0):
        indent = "    " * level
        result = f"{indent}Folder: {self.name}\n"
        
        for f in self.files:
            result += f"{indent}    File: {f}\n"
        
        for sf in self.subfolders:
            result += sf.__str__(level + 1)
        return result


def main():
    
    StartFolder = Folder("Start Folder", depth=0)
    current = StartFolder

    while True:
        print("\n" + "=" * 50)
        print(f" CURRENT FOLDER: {current.name} ")
        print("=" * 50)
        print("1) Add File")
        print("2) Add Folder")
        print("3) Select Folder")
        print("4) Print Folder")
        print("5) Exit")
        print("=" * 50)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            filename = input("Enter file name: ").strip()
            current.add_file(filename)

        elif choice == "2":
            name = input("Enter subfolder name: ").strip()
            current.add_subfolder(name)

        elif choice == "3":
            name = input("Enter folder name to select: ").strip()
            found = StartFolder.select_folder(name)
            if found is not None:
                current = found
                print(f"Now in folder '{current.name}'.")
            else:
                print(f"Folder '{name}' not found.")

        elif choice == "4":
            print("\nFolder Structure:")
            print(StartFolder)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

main()