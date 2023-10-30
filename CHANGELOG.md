# Changelog

## 0.1.0
First release <br>
Added main class <br>
Added function to get earned points <br>
Added login functionality <br>
Added logout functionality

## 0.2.0
Added classes for some function returns <br>
Added some more exception handling <br>
Added function to get giftshop items <br>
Added function to get history of points collected, earned or spent <br>
Added function to get information about the current user <br>
Added function to change information about the current user <br>
Removed option to login when creating an instance of the APISession class, use APISession.login() after creating an instance. <br>
Removed APISession.earned_points property, use APISession.get_earned_points() instead.