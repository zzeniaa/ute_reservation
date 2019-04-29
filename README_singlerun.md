# single_run
  
  A simple script to create a UTE Cloud single-run
  
   **Note:** In order for script to work, you need to install Selenium python module (pip install selenium) and chromium web driver (or use Firefox/IE) 
  
## Usage
  
 `python single_run.py  test_directory test_name.robot` 
      
  **Mandatory arguments**:
  * test directory (the script starts in /robotlte/testsuite/WMP/DevWro1L2/LTE)
  * full test file name
    
  **Optional arguments**:
  * -s eNB state (choose from: ssh_only, configured, commissioned, enb_configured, enb_commissioned)
  * -tl testline type (default value is CLOUD_R4P)
  * -e eNB build (default is latest trunk build for chosen testline type i.e. for CLOUD_R4P, default would be latest FL00_FSM4 build)
  * -s eNB state (default is *configured*)
  * -ute UTE build (default is the latest one)
  * -r repository revision (default is HEAD)
    
  ### Password policy
  check out [extend_a_reservation.py README file](https://github.com/zzeniaa/ute_reservation/blob/master/README.md)
  
## Useful links:
- [Chromium Web Driver](http://chromedriver.chromium.org/) 
- Get Selenium module from [PyPi](https://pypi.org/project/selenium/) or [NSN](http://pypi.ute.inside.nsn.com/selenium/)
- [Cmder](https://cmder.net/)
