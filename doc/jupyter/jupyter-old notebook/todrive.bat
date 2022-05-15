@echo off
cd C:\Users\kushn\Dropbox\software\projects\books\CFTM-intro-to-programming\doc\jupyter
echo copy *.jpg *.ipynb "G:\My Drive\shared\python\jupyter"
FOR %%F IN (*.jpg *.ipynb) DO (
  rem echo file is %%F
  echo copy %%F "G:\My Drive\shared\python\jupyter"
  copy %%F "G:\My Drive\shared\python\jupyter"
)
rem echo copy *.jpg *.ipynb "G:\My Drive\shared\python\jupyter"
set /p done="done? "
