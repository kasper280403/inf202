# Oil spill simulator

Software to simulate an oil spill in the ocean at the coast of a fictional town.  




---

## 📥 Download & Run

### Requirements

Python 3.11.14

###  Download

Download the latest release from [GitHub](https://github.com/kasper280403/inf202)  
Or clone with ssh `git@github.com:kasper280403/inf202.git`

###  Run the program
*Works on **Windows, macOS, and Linux**.*

The setup is recommended, if you do not want to, or have 
already done it skip ahead to the run part.

### Setup (recommended)

#### 1) Create venv
```bash
   python -m venv .venv
```

#### 2) Activate the virtual environment:

   macOS / Linux:
   ```bash
     source .venv/bin/activate
   ```
   
   Windows:
   ```powershell
      .venv\Scripts\Activate.ps1
   ```

#### 3) Install dependencies:
```bash
   python -m pip install -r requirements.txt
```

### Run

macOS / Linux (bash)
```bash
    python3 main.py
```

Windows (PowerShell)
```powershell
  python main.py
```

### How to use command tools


The project has 3 built in commands to choose which folders and files are used in simulation.  
To accsess the help sheet in the terminal type: --h or --help  
To look for config filesin  a specific folder use the command -f or --folder  
Example: --folder example_folder
To run all config files in a folder use the command --find_all  
Example: -f example_folder --find_all, runs all config files in example_folder
To run a single config file use -c or --config_file  
Example: -c config file.toml
---
## 🛠️ Development

### Clone the Repository

```
git clone git@github.com:kasper280403/inf202.git
cd inf202
```
### Git commands
```
git pull (takes changes from github into your current branch, always do when changing branch or when starting to code, do often)  

git fetch (retrieves new branches and notifys of changes to branches, does NOT update locally, use git pull to update)

git add . (adds all changes made)  
git commit -m "Message her in correct format" (commits everything added, see guide for writing messages correct)  
git push (pushes to github)  

```

---

## 🧪 Run Tests

#### macOS / Linux (bash)
```bash
  pytest tests/
```

#### Windows (PowerShell)
```powershell
  python -m pytest tests/
```



---

## 🧹 Code Style  

The project uses google dock style rules.  
See chapter 3 in the [styleguide](https://google.github.io/styleguide/pyguide.html).  
The project also aims to follow the rest of the style guide.  

The most important styling is summarised below:  
* Use docstring ("""  """) to comment classes and methods not #
* All classes should have a short description and the attributes written in the comments at the top of the class. Example below:
```
class User:
    """Represent a system user.

    Attributes:
        name (str): User's full name.
        age (int): User's age.
    """ 
```
* All methods should contain a short description, args, returns and exceptions. Example below:
````
def calculate_average(values):
    """Calculate the average of a list of numbers.

    Args:
        values (list[float]): List of numeric values.

    Returns:
        float: The average value.
    """
````

---

## 🧱 Project Structure

```
inf202
├── main.py
├── README.md
├── requirements.in
├── requirements.txt
├── results/
│   └── simulation1/
│       ├── final_image.png
│       ├── oil_simulation.mp4
│       └── simulation1.log
├── src/
│   ├── controller.py
│   ├── model/
│   │   ├── border/
│   │   │   └── border.py
│   │   ├── cells/
│   │   │   ├── cell.py
│   │   │   ├── edge.py
│   │   │   └── triangle.py
│   │   ├── factory/
│   │   │   └── factory.py
│   │   ├── point/
│   │   │   └── point.py
│   │   └── view/
│   │       └── view.py
│   └── resources/
│       ├── bay.msh
│       └── output/
│           ├── image0.png
│           ├── image1.png
│           └── image2.png
├── tests/
│   ├── test_border/
│   │   └── test_border.py
│   ├── test_cells/
│   │   ├── test_edge.py
│   │   └── test_triangle.py
│   ├── test_factory/
│   │   └── test_factory.py
│   └── test_point/
│       └── test_point.py
└── toml_files/
    ├── config.toml
    └── input.toml



```

---

## 👤 Authors

**Kasper S. Karlsen**  [GitHub Profile](https://github.com/kasper280403)  
**Harald A. Søvde**    [GitHub Profile](https://github.com/haraldsovde-crypto)  
**Fredrik Tveter**    [GitHub Profile](https://github.com/fredriktvet)  

_Developed for NMBU/inf202 at NMBU_

---

