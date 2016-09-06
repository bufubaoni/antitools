# antitools

antitools

1.random_food 
------------------------------------------------------
you should change foodlist , and run this script ,

    random_food/random_food.py
you  will get food without thinking.

2.auto_supervisor_controller
------------------------------------------------------
you should install requests 
it will send supervisor signal for restart task
the supervisor config file in 
    /etc/supervisor/supervisor.conf

set
    [inet_http_server]
	port=0.0.0.0:9001  ;url for mange
	username=user      ; base auth
	password=pass      ;

3.struct_template
-------------------------------------------------------
if you have 2 list A and B
and there are the same number of elements
You will get the same as the structure of B and A
ex.
    A------> [1, [2, 3, [2, 3]], [4, 5, 6], 7]
    B------> [2, 3, 4, 5, 6, 7, 8, 2, 3]
    B2A----> [2, [3, 4, [5, 6]], [7, 8, 2], 3]

