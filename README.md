# ute_reservation
# extend_a_reservation
A script that extends a reservation with given reservation number

Giving a reservation number is mandatory.

There are different ways to get a password from user:
1. asking user to type it in command line; 
    - using getpass module; 
    - user needs to type their password in order to login to UTE;
    - password is not visible in command line
2. importing it from python module;
    - user needs to first create a .py file with a variable storing their password(i.e. my_password = 'pass');
    - then, using py_compile module, compile .py file to .pyc one(i.e. py_compile.compile(foo.py));
    - delete previous .py file;
    - finally, import the .pyc module to ute_reservation script and you can refer to your password variable as name_of_pyc_file.name_of_variable
      (i.e. foo.my_password)

Username is obtained from already existing enviromental variables, therefore there's no need to create new ones.

To schedule the script to execute automatically, you can use Windows Task Scheduler:
- firstly, create a .bat file: 
      start path_to_python.exe path_to_script.py number_of_reservation
      i.e.:
      start C:\Python27\python.exe C:\ute_reservation.py 1234567
- open Task Scheduler, choose 'Task Scheduler Library' from the left, then 'Create Task' on the right;
- in General tab: choose a name for your task, check options 'Run whether user is logged on or not', 'Run with highest privileges' 
  and configure to run for your operating system;
- in Triggers tab: choose 'New' and configure parametres as you like (for when and how often the script runs);
- in Actions tab: choose 'New', Action: Start a program; under 'Program/script' choose the path of command line app of your choice 
  (i.e. C:\cmder\cmder.exe), under 'Add arguments' type the path of your .bat file(i.e. C:\scripts\ute.bat), under 'Start in' choose path 
  to the folder your bat file is in (i.e. C:\scripts) 
  
  


