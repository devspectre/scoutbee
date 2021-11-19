# Scoutbees OnPremise

The app is used to configure Active Directory of domain.

## Getting Started

The app is written in python with a dozen of python libraries and with PyQt5 for GUI.
Since the app is specified for Windows, we only have instructions for Windows.

### Prerequisites

Assuming that you've already installed python and pip on your machine.

```
pip install -r requirements.txt
```

### Installing

The project includes a couple of .bat script files to simplify running and deploying the app

To run the app simply
```
run.bat
```

If you want to see GUI only with no interaction with backend, then
```
python sbgui.py
```

### Deploying the app

PyInstaller is used to build a single-file standalone executable from python code.
Also simplified the process for convenience.
All you have to do is just:
```
deploy.bat
```

This will create an executable in ./dist

The app requires ls.db, .favicon.ico and /images along with itself.

### Authors

Gadi Feldman

## License
