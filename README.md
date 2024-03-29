![GitHub Dark](https://github.com/github-dark.png#gh-light-mode-only)
# PY-passwordtest <small class='version_passwordtest'>V.1.3</small>
<p>This script is to measure password security from Brute Force and Dictionary (worldlist) attacks, by calculating the number, location, and character level. the longer and more varied the character of the password, the harder it is to crack</p>
<img align='center' src="https://github.com/LcfherShell/passwordtest/blob/main/logiccracking.png" height="260" width="380">


### Installation

- Pip

  ```python -V```

  - Windows:
  
    `python -m pip install passwordtest`
  
  - Unix or Mac:
  
    `pip install passwordtest`
  
- GIT

  - Windows, Unix and Mac:
  
    ````
       git clone https://github.com/LcfherShell/passwordtest
       cd passwordtest
       python -m pip install . or python setup.py
    ````
### Usage Example
````Python hl_lines="4  9-12  25-27"
    1. from passwordtest.main import PasswordTest
    
    2. password = 'Hello'
    
    3. passwordtest = PasswordTest(active=True, sites=True)#call class
    
    4. required_time = passwordtest.__time__(text=password) #getting time
    
    5. sorttime = passwordtest.Sort_Pw(text=[required_time[0], required_time[1]]) #sorttime by min and max
    
    6. badtime = sorttime[1] #time late
    
    7. goodtime = sorttime[0] #fastest time
    
    8. goodtime = passwordtest.Convert_Date(goodtime)#covert to time
    
    9. security = passwordtest._Score_Point(password)##get score point
    
    10.Precent =passwordtest.Precent_Safe(security, badtime, password)#get percent security
    
    11.print(goodtime, security, Precent)
    
    ``Output: 0:00:13 Horrible 36``
````
### Usage Mini Example 
````Python hl_lines="4  9-12  25-27"
    1. from main import PasswordStrength
    
    2. password = 'Hello'
    
    3. passwordtest = PasswordStrength(active=True, sites=True)#call class
    
    4. passwordtest.inputs(password) #getting time
    
    5. gettime = passwordtest.get_longtime
    
    6. badtime = passwordtest.predict[1] #time late
    
    7. goodtime = passwordtest.predict[0] #fastest time
    
    8. security = passwordtest.score(password)##get score point
    
    9. Precent = Precent =passwordtest.precent(security, goodtime, password)#get percent security
    
    10.print(gettime.get("goodtime"), security, Precent
    
    ``Output: 0:00:13 Horrible 36``
    11.##if you want online time
    12.timeout = passwordtest.calcul_online(goodtime, passwordtest.sites(sitename="http://example.com"))
    13.print(passwordtest.Convert_Date(round(timeout, 2))#print end get timeou post <cracking>
````

### Shell Demo

``open commandprompt and type
  passwordtest
``

<img align='center' src="https://github.com/LcfherShell/passwordtest/blob/main/images1.png" height="260" width="380">


## 
📫Bug reports: **LCFHERSHELL@TUTANOTA.COM**
<h3 align="left">Sociall Media:</h3>
<p align="left">
  <small>
    <a href="https://twitter.com/lcfershell" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="lcfershell" height="30" width="40" /></a>
    <a href="https://stackoverflow.com/users/18267661" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="18267661" height="30" width="40" /></a>
    <a href="https://instagram.com/@lcfhershell" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="@lcfhershell" height="30" width="40" /></a>
    <a href="https://medium.com/@alfiandecker2" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@alfiandecker2" height="30" width="40" /></a>
    <a href="https://www.hackerrank.com/@alfiandecker2" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="@alfiandecker2" height="30" width="40" /></a>
    <a href="https://github.com/LcfherShell" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="LcfherShell" height="40" width="40"/></a>
 </small>
</p>
