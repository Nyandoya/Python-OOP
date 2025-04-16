# 🚀Python OOP Assignment: Vehicles & Polymorphism

**📚 Overview**
This project demonstrates Object-Oriented Programming (OOP) concepts in Python using a custom-designed class hierarchy. The main focus is on class creation, inheritance, constructors, and polymorphism through method overriding.

# 🧱 Assignment 1: Design Your Own Class

I designed a base class called Vehicle with attributes like make, model, and year, and a method display_info() to print basic details.

**🔧 Features:**<br>
* Base Class: Vehicle

* Subclasses: Car, Plane, Boat

**Each subclass:**

* Inherits from Vehicle

* Adds specific attributes (num_doors, wingspan, length)

Overrides the move() method

## 🎭 Activity 2:<br>
Polymorphism Challenge
The program uses polymorphism by having multiple subclasses define their own version of the move() method.

**For example:**

Car.move() → "Driving on the road 🚗"

Plane.move() → "Flying in the sky ✈️"

Boat.move() → "Sailing on the water 🚤"

A function vehicle_moves_demo() accepts a list of Vehicle objects and calls their move() method, demonstrating how the same method name can behave differently depending on the object.

📂 Files
1. oop.py: Contains the class definitions and demo function

2. README.md: This file 😊



▶️ How to Run
Make sure you have Python installed. Run the script with:
[oop.py](https://github.com/Nyandoya/Python-OOP/blob/main/oop.py)<br>
You’ll see each vehicle’s info and its specific movement behavior printed to the console.



