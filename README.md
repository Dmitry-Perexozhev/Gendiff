[![Test Coverage](https://api.codeclimate.com/v1/badges/2093802b1c775182c27b/test_coverage)](https://codeclimate.com/github/Dmitry-Perexozhev/python-project-50/test_coverage)
### Gendiff

Gendiff is CLI utility for comparing configuration files in JSON and YAML formats.

### Key Features:

- Find differences between files
- Two comparison formats - flat and recursive (stylish)

### Installation requirements

- Python 
- Poetry

1) Clone the project repository to your local device:
```
git clone git@github.com:Dmitry-Perexozhev/Gendiff.git
```
2) Go to the project directory:
```
cd Gendiff
```
3) Configure Poetry to create virtual environments in the .venv folder at the root of the project:
```
poetry config virtualenvs.in-project true
```
4) Installing dependencies:
```
poetry install
```

#### Usage

- Comparison of two files in flat format 
```
gendiff -f plain path_to_file_1 path_to_file_2
```
- Comparison of two files in stylish format 
```
gendiff -f stylish path_to_file_1 path_to_file_2
```
or (stylish default)
```
gendiff path_to_file_1 path_to_file_2
```
- Help information
```
gendiff -h
```
