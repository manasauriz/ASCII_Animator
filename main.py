from animation import Animation
import animator
import ansi
import os

LOGO = '''
 █████╗ ███████╗ ██████╗██╗██╗    █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██║██║   ██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████║███████╗██║     ██║██║   ███████║██╔██╗ ██║██║██╔████╔██║███████║   ██║   ██║   ██║██████╔╝
██╔══██║╚════██║██║     ██║██║   ██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██╔══██╗
██║  ██║███████║╚██████╗██║██║   ██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
'''


def main_menu() -> None:
    ansi.clear()
    ansi.place(1, 1, LOGO)
    print("Create a new project | Load an existing project | Play animation from saved projects\n")

    ans = input("Create Project? (y/N) ").strip().lower()
    yes = ['yes', 'y']
    no = ['no', 'n']

    if ans in yes:
        new_project()
    elif ans in no:
        ans = input("Load Project? (y/N) ").strip().lower()
        if ans in yes:
            load_project()
        elif ans in no:
            ans = input("Play Animation? (y/N) ").strip().lower()
            if ans in yes:
                play_animation()


def new_project() -> None:
    while True:
        try:    
            name = input("Enter Project Name: ")
            if not name or name == "":
                raise ValueError
            width = int(input("Enter Frame Width: "))
            length = int(input("Enter Frame Length: "))
            break
        except ValueError:
            print("Error: Enter a valid name and number!")

    movie = Animation(name.strip().lower(), width, length)
    animator.run(movie)


def load_project():
    all_files = {}
    for i, file in enumerate(os.listdir("."), start=1):
        if file.endswith(".txt"):
            print(f"{i}. {file.capitalize()[:-4]}")
            all_files[i] = file

    file_name = input("Enter File Name: ").strip().lower()
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    if file_name in all_files.values():
        movie = Animation.load(file_name)
        animator.run(movie)


def play_animation():
    ...


if __name__ == "__main__":
    main_menu()