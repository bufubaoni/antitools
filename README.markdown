# antitools

antitools

1. random_food 
------------------------------------------------------
you should change foodlist , and run this script ,

    random_food/random_food.py
you  will get food without thinking.

2. auto_supervisor_controller
------------------------------------------------------
you should install requests 
it will send supervisor signal for restart task
install requests

    sudo pip install requests

the supervisor config file in 

    /etc/supervisor/supervisor.conf

set

    [inet_http_server]
	port=0.0.0.0:9001  ;url for mange
	username=user      ; base auth
	password=pass      ;
opt you shuold copy then
modify username  and password for pass auth
script 

    script.py taskname taskaction
	
task action opt
    start
	stop
	restart

3. struct_template
-------------------------------------------------------
if you have 2 list A and B
and there are the same number of elements
You will get the same as the structure of B and A
ex.

    A------> [1, [2, 3, [2, 3]], [4, 5, 6], 7]
    B------> [2, 3, 4, 5, 6, 7, 8, 2, 3]
    B2A----> [2, [3, 4, [5, 6]], [7, 8, 2], 3]

4. consoledict
-------------------------------------------------------
translate en to zh in console 
ex.

    input your words:hand                                                                                                
    hand---/hænd/                                                                                                        
    0-pos:n. def:手；手工；帮助；指针                                                                                    
    1-pos:v. def:交；递；给                                                                                              
    2-pos:Web def:汉德；人手；手形

when you input your words your will get translate, also you can input sentence.
in windows cmd charset will only display half,shuold minimize and then restore the windows.

5.jfinal model generate
-------------------------------------------------------
translate sql table to java class for framwork jfinal
you should put .sql in 

    /tables

and modify generate.py file 

    api("your table name", "package")

then you will get the 

    tablenameContraller.java
    tablenameModel.java
    tablename.java

copy these to your project! Ation,the package will not correct ,becouse my project diff from yours.

6. server test
---------------------------------------------------------
just test the server is running

just the server down time.

3min heart bit about.

7. proxy list
---------------------------------------------------------
long time ago write some spider for proxy,it have a default url,you should edit it if need.

8. Decorator learn
---------------------------------------------------------
edit a block code for decorator copy and newer learning.
