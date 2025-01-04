![Demo](demo.gif)
---

# **ASCII Animator**

ASCII Animator is a command-line tool for creating and playing frame-by-frame traditional animations using ASCII art. It is written and structured as a python package.

---

## **Features**
- Create new ASCII animation projects.
- Load and edit existing projects.
- Play animations directly from the CLI.
- Delete projects with ease.

---

## **Installation**
Currently, `ascii_animator` is Windows compatible only. I will make it Linux compatible soon. To install the tool:

1. Clone the repository:
   ```bash
   git clone https://github.com/manasauriz/ASCII_Animator.git
   cd ascii_animator
   ```
2. Run the following command:
    ```bash
    pip install .
    ```
    If you want to contribute to the project or make changes locally, Install in development mode:
   ```bash
   pip install -e .
   ```

---

## **Usage**
After installation, you can use the `ascii_animator` command directly from your terminal.

### **Commands**
- Open the main menu:
  ```bash
  ascii_animator
  ```
- Start a new project:
  ```bash
  ascii_animator -n
  ```
- Load an existing project:
  ```bash
  ascii_animator -l
  ```
- Play an animation:
  ```bash
  ascii_animator -p
  ```
- Delete a project:
  ```bash
  ascii_animator -d
  ```

### **Help Command**
To view available commands and options, use:
```bash
ascii_animator -h
```

### **Animator Controls**
- `esc` -> save and quit program
- `arrow keys` -> move cursor around frame
- `character key` -> add character on screen and move cursor forward
- `shift + character key` -> add alternate version of character on screen and move cursor forward
- `space` -> add whitespace character on screen and move cursor forward
- `backspace` -> remove previous character and move cursor backward
- `delete` -> remove character on current cursor
- `ctrl + v` -> add copied characters on screen, as much as a line can fit
- `alt` -> display all controls in frame for some time
- `tab + s` -> save current progress in file
- `tab + p` -> play animation of current progress
- `tab + f` -> go to frame
- `tab + right or >` -> load next frame
- `tab + left or <`-> load previous frame
- `tab + n` -> add new frame next to current frame
- `tab + m` -> copy current frame and add copied frame next to current frame
- `tab + backspace` -> wipes current frame
- `tab + d or delete` -> delete current frame data
- `tab + c` -> copy current frame data
- `tab + v` -> paste copied frame data onto current frame

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.