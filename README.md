# Setup_provide

### Tool to automatically configure or reconfigure an assignment for Comp 15.

Type ./setup_provide -h to display the following usage information:

    usage: setup_provide [-h] -a ASSIGN -d DUEDATE -t DUETIME
                         [--minfiles MINFILES | --numfiles FILES]
                         [--status {on,off}] [-ns SUBMISSIONS]
                         [files [files ...]]

    Helps you set up an assignment

    positional arguments:
      files                Names of required files.

    optional arguments:
      -h, --help           show this help message and exit
      --minfiles MINFILES  Minimum number of files required
      --numfiles FILES     Number of files required
      --status {on,off}    Status of assignment. Default is 'off'
      -ns SUBMISSIONS      Number of submissions allowed per student. Default: 5.

    required arguments:
      -a ASSIGN            Assignment name e.g. hw1
      -d DUEDATE           Date in form of MM/DD e.g. 12/25
      -t DUETIME           Time in form of HH:MM e.g. 15:00
  
  
Essentially, the program does the following

  1. Creates an assignment configuration with user arguments
  
  2. Attempts to find an existing configuration of the same name. If one is
     found, updates the existing config with the new data passed by user.
     Note: In all cases, we prefer user data to existing data.
     
  3. Add the new/updated config into assignments.conf.  
  
  4. Sets up a new assignment on Gradescope.
  
  5. Creates/updates the testset file specific to the assignment.
  
  6. Runs Prozac.  (See Prozac for documentation)
  
  7. Sets up some legacy folders as a fallback.
  
  8. Adds an exception into the assignments 'exceptions.conf' file for
     quick and easy testing.
  
At all steps, the user is notified which part of the process above is running. 
There are two crucial steps in this process at which the program will open
a text editor for you to confirm/edit the changes the program has made.  
Conveniently, if you use vscode, we launch that!  Otherwise we launch vim.

The editor launches:
  a. After the new configuration has been added to assingments.conf
  b. After the new testset has been created or updated.


  
  
  
  
  
