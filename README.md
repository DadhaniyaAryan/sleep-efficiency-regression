# Sleep Efficiency Regression

Multiple linear regression analysis that predicts sleep efficiency from sleep and lifestyle features in the supplied dataset.

## Team and roles


| Member | GitHub handle | Role |
|---|---|---|
| SHISTI UPENDRA | ShistiUpendra | Documentation |
| DADHANIYA ARYAN KETANBHAI | DadhaniyaAryan  | Execution |
| PRATEEK | Prateek | PPT |
| VIRAJ AMIT BAPAT | virajiitrpr | Video |


## Project structure

```text
sleep_efficiency_project/
├── README.md
├── requirements.txt
├── data/
│   └── Sleep_Efficiency.csv
├── main.ipynb
├──.gitignore

```
### Group number: 37

## Dataset



## Setup and run

### This project requires Python 3.11–3.14.(make sure you have one of these installed)

 Follow the commands for your operating system, from top to bottom. They create a virtual environment and use its Python directly.

### Windows (PowerShell)

Open PowerShell and run:

```powershell
git clone https://github.com/DadhaniyaAryan/sleep-efficiency-regression.git
cd sleep-efficiency-regression
python --version
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute --inplace main.ipynb
.\.venv\Scripts\python.exe -m jupyter trust main.ipynb
.\.venv\Scripts\python.exe -m notebook main.ipynb --ServerApp.open_browser=True
```

### macOS (Terminal)

Open Terminal and run:

```bash
git clone https://github.com/DadhaniyaAryan/sleep-efficiency-regression.git
cd sleep-efficiency-regression
python3 --version
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m jupyter nbconvert --to notebook --execute --inplace main.ipynb
.venv/bin/python -m jupyter trust main.ipynb
.venv/bin/python -m notebook main.ipynb --ServerApp.open_browser=True
```
#### possible error and fix

**Browser doesn’t open:** Copy the one of the local http://127.0.0.1:...  out of three links from Terminal and paste it into your browser.Then open main.ipynb. (Keep terminal open).

**nbconvert or notebook not found:**Reinstall requirements with .venv/bin/python -m pip install -r requirements.txt, then retry the failed command.

**Notebook says Not Trusted:**	Run .venv/bin/python -m jupyter trust main.ipynb. Trust only code you’ve reviewed.

**No module named venv:**Reinstall Python with its standard library components, then retry that command.

