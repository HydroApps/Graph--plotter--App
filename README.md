## Graph--plotter--App V 0.1.0

### Table of contents: 

 1.[About](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#about)
 
 2.[Installation](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#installation)
  
 3.[User guide](https://github.com/HydroApps/Graph--plotter--App/edit/main/README.md#userguide)
  
#### 📝About
 Graph plotter App helps you to plot graph easily and that too through a terminal😺. It is lightweight and also fully portable.
 Since the application runs in a bat file please make sure your operating system supports it.  
 
#### 📦Installation
  Since the app is portable it doesn't recquire any installation. Do the following steps to run the application. 

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
 --The file will run successfully. If its not working refer 'common issues' for solutions.
 
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
        
* Tada!! 🥳 Your graph is ready!!🙂


 
