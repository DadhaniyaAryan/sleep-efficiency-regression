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

This project requires Python 3.11–3.14. Follow the commands for your operating system, from top to bottom. They create a virtual environment and use its Python directly, so activation is not required.

### Windows (PowerShell)

Open PowerShell and run:

```powershell
git clone https://github.com/DadhaniyaAryan/sleep-efficiency-regression.git
cd sleep-efficiency-regression
python --version
python -m pip install -r requirements.txt
python -m jupyter nbconvert --to notebook --execute --inplace main.ipynb
python -m jupyter notebook main.ipynb
```

### macOS (Terminal)

Open Terminal and run:

```bash
git clone https://github.com/DadhaniyaAryan/sleep-efficiency-regression.git
cd sleep-efficiency-regression
python3 --version
python3 -m pip install -r requirements.txt
python3 -m jupyter nbconvert --to notebook --execute --inplace main.ipynb
python3 -m jupyter notebook main.ipynb
```

The version-check command should show Python 3.11, 3.12, 3.13, or 3.14. The notebook reads `data/Sleep_Efficiency.csv` using a relative path. The execution command runs all cells and saves their results in `main.ipynb`; the final command opens the notebook so the results and code can be viewed.