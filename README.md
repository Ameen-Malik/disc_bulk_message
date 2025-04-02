# discord-bulk-message
automate processing and sending discord messages, to work with bots such as Unbelivabot

install guide:
## --windows--
1. Install Python: https://www.python.org/downloads/
- (Make sure to check the box that says "Add Python X.X to PATH" before you click "Install Now".)

### Verify install:
2. run following commands in cmd:
<pre> python --version  </pre>
<pre> pip --version  </pre>

###  Install Necessary Python Packages:
3. run following command in cmd
<pre> pip install pyautogui pyperclip </pre>

###  clone Project folder to desired location:
4. after placing the folder at desired location edit **List_of_names.txt**
5. open terminal at this folder, your path should look like  ../../folder name> 
6. run this command
<pre> python cmd_gen.py </pre>
* this will generate a list of commands in comands.txt *
<pre> python send2discord.py </pre>
* now press enter when promted and click on discord input, within 5 seconds. it will begin sending commands at a delay of 5 seconds

## --Mac-- 
1. Install Homebrew:
   <pre>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</pre>

2. Install Python:
   <pre>brew install python3</pre>
3. Install Pip:
   <pre>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py </pre>
   <pre>python3 get-pip.py</pre>
###  Install Necessary Python Packages:
4. run following command in cmd
<pre> pip install pyautogui pyperclip </pre>
###  clone Project folder to desired location:
4. after placing the folder at desired location edit **List_of_names.txt**
5. open terminal at this folder, your path should look like  ../../folder name> 
6. run this command
<pre> python3 cmd_gen.py </pre>
* this will generate a list of commands in comands.txt *
<pre> python3 send2discord.py </pre>
* now press enter when promted and click on discord input, within 2.5 seconds. it will begin sending commands at a delay of 2.5 seconds

