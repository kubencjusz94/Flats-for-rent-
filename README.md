# Rentals - app for renting apartments
Simple rental app created with Django.
<p align="center">
  <img  src = "https://github.com/kubencjusz94/Flats-for-rent-/blob/master/rentals/static/img/logo.png" alt = "Flat Hunters Logo" width="250"/>
</p>

## Table of Contents:

1. [ About App ](#desc) 
2. [ Technologies ](#tech)
3. [ Setup ](#setup)
4. [ Usage ](#details)


<a name="desc"></a>
### 1. About App
App allows user to reserve a flat from database. The aim of project was to use my knowladge of Python Django to build a first real no-commercial app. Project shows how to manage data from mySQL by Django and exchange information between frontend-backend sides. 

<a name="tech"></a>
### 2. Technologies

* Python 3.6
* Django 2.1.1
* jQuery 3.2.1
* Bootstrap 4
* CSS 3
* HTML 5

<a name="setup"></a>
### 3. Setup 

#### Installing Python 3 

You can easy download python from Python website [here](https://www.python.org/downloads/). I chose Python 3.6 because had a problem with integrate mySQL with Python 3.7.

#### Installing pip( Python Packet Index tool)
##### Ubuntu
```
$ sudo apt install python3-pip
```
##### Windows 
Windows installer incorporates pip3 by default.

#### Installing virtual environment
##### Ubuntu
```
$ sudo pip3 install virtualenv
```
##### Windows 
```
pip3 install virtualenv
```
#### Creating virtual environment
##### Ubuntu
```
$ sudo pip3 virtualenv mydjangoenvironment
```
##### Windows
```
mkvirtualenv mydjangoenvironment
```
#### Working on evironment
##### Ubuntu
```
$ sudo . mydjangoenvironment/bin/activate
```
##### Windows
```
workon mydjangoenviroment
```
#### Installing django 
##### Ubuntu
```
(mydjangoenviroment) $ sudo pip install django
```
##### #Windows
'''
(mydjangoenviroment) pip3 install django
'''
#### Installing mySQL
##### Ubuntu
```
$ sudo pip install mysqlclient
```
##### Windows
```
pip install mysqlclient
```
<a name="details"></a>
### Usage
App have four views:
* Index page(#index)
* City Panel page(#citypanels)
* Searching flat list page(#searching)
* Detail flat page(#detail)

<a name="index"></a>
#### Index page
It's a simple welcome page containing number of available flats from data base.
<p align="center">
  <img  src = "https://github.com/kubencjusz94/Flats-for-rent-/blob/master/rentals/static/img/logo.png" alt = "Flat Hunters Logo" width="250"/>

