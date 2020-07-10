# Setup Guide

## Prerequisite
This project and its setup instructions is based on a user using a Windows operating system. Any deviation from this might need other installation steps.

## Technologies used
- Python
- Selenium
- Pytest
- Pip
- Windows

## Install Python 3:
1. Download the latest version from: https://www.python.org/downloads
2. Run the downloaded .exe file

**NB:** Ensure you tick **_Add Python to PATH_** during installation

## Install Pip
1. Download **get-pip.py** from: https://bootstrap.pypa.io/
2. From cmd navigate to location of downloaded file and run this command: **python get-pip.py**

## Verify Python and pip installation
From _cmd_ execute:

    python --version
        Output example: Python {and_the_version_number}
    pip --version
        Output example: {location}/site-packages/pip (python {and_the_version_number})

If you experience any problems see section _Python and pip path tips for windows_

## NB: Python and pip path tips for windows
If you have issues executing python and/or pip in git bash prompt then use windows native cmd.

If pip application can't still not be found, add pip path to the environment variables.

Find python 3 installation folder and under it you should find the scripts folder, add this scripts path to environment variables, see below possible path:

    C:\Users\{UserAccountName}\AppData\Local\Programs\Python\Python37-32\Scripts
    
## Upgrade PIP(_Python package manager_)
From _cmd_, execute:

    python -m pip install --upgrade pip

## Install GIT(_If not installed_)
1. Download from here: https://git-scm.com/download/win
2. Run the downloaded .exe file
    
## Clone WEB UI Test GIT Repository:
    git clone https://github.com/garthbosch/travel-diaries-assessment.git
    
## Install Required Python Packages:
From the root of the repository run:
 
    pip install -r requirements.txt
    
## Executing Tests:
From the root of the repository, run:

    pytest

## Viewing Test Report:            
  Screenshots and a report called **_travel-diaries-assessment.html_** will be created in the reports folder of the repository after test execution.
 