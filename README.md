# Pranav_Camino_Backend_Challenge

This application has been deployed to heroku as a container,the docker image has been released at the links specified below , please find the below appropriate links for  loan application and check loan status.

# URLS:

 1. URL to apply for loan  : https://floating-mountain-95644.herokuapp.com/loanapp/

 2. URL check status : https://floating-mountain-95644.herokuapp.com/status?id=897079



Note: Follow the exact format of the links above to test on postman.

# Steps to Test on Postman :

* Change URL Request type to Post enter the url no. 1 from above .
* Switch to body tab and enter json file as value with **key name 'file' which is the json file , this is essntial for the post request.
* Send api request and wait for response . 
* After you recive Status : 200 ok open a new tab for a new request
* Switch to get request and enter url 2 from above.
* Hit send and wait for status : 200 ok response


Note : 
* Test request for non existent id by replacing /status?id=897079 with  /status?id=4567 to see message 
* Test  post request for duplicate entry with minor details like number/address updated to see message.

# Assumptions:

1. Each different loan application has a unique id , which is used to identify the application.
2. Duplicate entries are checked by id , and updates are made to the entry for that id , the algorithm checks for same id and updates accordingly.
