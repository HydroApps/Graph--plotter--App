## Graph--plotter--App V 0.1.0

### Table of contents: 

 1.[About](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#about)
 
 2.[Installation](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#installation)
  
 3.[User guide](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#userguide)
 
 4.[Known issues](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#known-issues)
 
 5.[Screenshots](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#-screenshots-v-010)
 
 6.[All versions](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#-all-version-gdrive-folder)
 
 7.[License](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#license-)
 
 8.[Contact me](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#contact-me-)
  
#### 📝About
 Graph plotter App helps you to plot graph easily and that too through a terminal😺. It is lightweight and also fully portable.
 Since the application runs in a bat file please make sure your operating system supports it.  
 
#### 📦Installation
  <mark> Installation of Python 3.9 is recommended.If you are using low end pc download portable python; Winpython from https://winpython.github.io </mark>
  
  You can also download setup file by clicking the below link: 
 
 --Download the files as zip or use the following command 
 ```
 $ git clone https://github.com/HydroApps/Graph--plotter--App.git 
 ```
 --Go to the cloned or downloaded folder and edit the bat file as follows
 ```
 @echo off
"give the path of python.exe in 'venv' folder " "give the path of graph_plotter.py" 
 pause
 ```
 --Open your termial and change directory using the following command
 ```
 $ cd ../path/to/the/folder
 ```
 --Run the batch file
 ```
 .\graph_plotter
 ```
 --The file will run successfully. If its not working refer 'Known issues ' for solutions.
 
 #### 🕹️User guide 
   Step by step instructions for using the app. These will be displayed in your terminal too.
   
   * Give the graphsize/ width and height of the graph[in inches]. NOTE:By default they are 6.4 and 4.8 respectively
   
   * The space for entering the width will be displayed first then enter the height.

    *Example:
          Enter width:12
          Enter height:13
          
   * Enter the X values[min 5 values]
   
    *Example:
   
          input:
          1
          2
          3
          4
          5
          stop #Enter stop for exiting from the loop
    output: [1,2,3,4,5] 
    
   * Now enter the Y values[min 5 values] 
        
    *Example:
    input:
          9
          8
          7
          6
          4
          stop 
    output: [9,8,7,6,4]
    
   * Your X- values and Y-values will be displayed
   
   * Enter names for your graph's x and y axis
 
    *Example:
           Name of x axis: X--axis
           Name of y axis: Y--axis
           
* Enter your graph's x and y variable-fontsize

      *Example:
          Enter fontsize of x variables: 10
          Enter fontsize of y variables: 10
          
* Enter a relevant title for the graph
     
      Example:
          Title: Graph-xyz
          
* Now Enter the degree of rotation of x and y labels of your graph
  
      Example:
           Input: 30
           Output: #The x or y label will rotate 30 degree
        Note: Enter zero for no rotation
        
* Tada!! 🥳 Your graph is ready!!🙂. You can save your graph now.

#### 📌Known issues
  --ValueError: invalid literal for int() with base 10: 'd' ['d' or any other string value]
    
    Solution: Make sure you insert an integer in place of width,height,x and y values [expect 'stop'], fontsize and degree of rotation.
   
  --Virus Warning :
  
     Solution: This application is not a virus. Make it exception from start > Settings > Update & Security > Windows Security > Virus & threat protection or the settings of your antivirus. 
   
  --Dll missing :
       
       Solution: Update your pc or refer any of the below links:
       https://answers.microsoft.com/en-us/windows/forum/all/api-ms-win-crt-runtime-l1-1-0dll-is-missing/b593b94e-6691-423b-a586-0b7f10131e35
       https://youtu.be/TQ2XAmGDLmU 
       If you want to download the dll refer: https://www.dll-files.com
           
  --Bat file not working :
      
       Solution : Please make sure your os supports batch files
       
  --Module missing error :
      
       Solution :Run the following command: 
       python -m pip install -r requirements.txt
       
       Alternate solution: Run the following command:
       python -m pip install colorama
       python -m pip install matplotlib
       
  --Bat file not running :
      No Python at 'F:\USB drive--portable apps\WinPython64\WPy64-39100\python-3.9.10.amd64\python.exe'
      
      Solution: Do the following: 
      Delete the venv folder . Edit the bat file and link graph_plotter.py to main python.exe in your programs folder. Now run the batch file.
       
#### 📸 Screenshots [V 0.1.0] in cmder console 

1. ![Screenshot (142)](https://user-images.githubusercontent.com/101416024/160813392-bb47ad3e-6a23-40ee-935b-4cd1d10531c8.png)
2. ![Screenshot (143)](https://user-images.githubusercontent.com/101416024/160813919-09666bda-cdc7-481f-b804-00ad76668b93.png)
3. ![Screenshot (144)](https://user-images.githubusercontent.com/101416024/160813940-719ffe47-276c-43da-b42a-4a48ab77cac4.png)



#### 📂 All versions/Releases 
        
   For all releases refer Releases in Github :  [📂](https://github.com/HydroApps/Graph--plotter--App/releases)
   
   or the Gdrive folder link:  [💾](https://drive.google.com/drive/folders/1A32aw4WDE972QZqB89wT6JDSQQpCkzwk?usp=sharing)
   
   
  Version will be given in Version file [open in browser]
        
#### 📌License : 

    
     📃Licensed as Open Source under GNU General Public License v3.0. 
       For more info refer LICENSE.md
    

#### 📞Contact me : 
  You are free👍 to contact me regarding any issues/problems in any of my apps 🔥: 
  
  --Telegram: https://t.me/Loki_Laufeyson_2473  

  --Discord: Loki_Laufeyson#2473

  --Join our Telegram Channel for news of new updates. [https://t.me/HydroApps616]

 
