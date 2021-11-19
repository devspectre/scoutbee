@echo off
IF EXIST ".\env" (
    CALL .\env\Scripts\activate.bat
    ECHO Dependencies already installed
) ELSE (
    ECHO Installing Dependencies! This may take a few minutes...
    CALL python -m venv env
    ECHO Virtual environment successfully created
    CALL .\env\Scripts\activate.bat
    ECHO Virtual environment activated
    CALL pip install -r requirements.txt
    ECHO Dependencies successfully installed
)
CALL pyinstaller --onefile deploy.spec
ECHO Standalone executable successfully created
