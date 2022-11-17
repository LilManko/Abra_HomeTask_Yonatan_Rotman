# Abra_HomeTask_Yonatan_Rotman 


# Important Notes:


i have prepared a Postman collection to properly operate the API 
please import the file to your postman use it to your convenient


# User credentials:

superuser - admin

users - test1, test3, Yossi, David

password - 12345 (same password for all the users)

# User email:

to send we will use the email as the key, 
admin - yonirotman159@gmail.com (not a real email)

test1 - c@c

test3 - d@d

Yossi - y@y

David - E@e


# To run the app follow the steps (command line): 

1) git clone https://github.com/LilManko/Abra_HomeTask_Yonatan_Rotman.git

2) cd Abra_HomeTask_Yonatan_Rotman

3) install virtual environment:

   pip install virtualenv
   
  4) py -m virtualenv myenv

5) activate the virtual environment: 

    myenv\Scripts\activate
 
6) install dependencies:

    pip install -r requirements.txt

7) cd ChatAPI

8) python manage.py runserver

9) open local hold with your web browser (http://127.0.0.1:8000/)


# Endpoints:


[
    
    "/register",
    
    "/login",
    
    "/logout",
    
    "/send_message",
    
    "/read_message",
    
    "/get_user_messages",
    
    "/get_unread_user_messages",
    
    "/delete_message"
]



# screenshots


register:
https://i.gyazo.com/5e1fb9818b70f7c8c22600b37ae53733.png

Login:
https://i.gyazo.com/62b160e2665d56c1c7c565adc9d9005d.png

Logout(need token):
https://i.gyazo.com/6ff10518d69a76d294e8a46860b8b230.png

Write Message(need token):
https://i.gyazo.com/d48823eff4f3e9ec8a38cdc937d321b1.png

Get User Messages(need token):
https://i.gyazo.com/4f8f06b28678f1e3a02bdd44ea6c17cc.png

Get Unread User Messages(need token):
https://i.gyazo.com/4792cb74919664db4eff9d4e36f4e15b.png

Read Message(need token):
https://i.gyazo.com/efcd75554ce978fce46ffba764858fe1.png

Delete Message(need token):
https://i.gyazo.com/f72b882a381785cab7cd774ab5ed070b.png














