🚀 Python OOP Assignment: Vehicles & Polymorphism
📚 Overview
This project demonstrates Object-Oriented Programming (OOP) concepts in Python using a custom-designed class hierarchy. The main focus is on class creation, inheritance, constructors, and polymorphism through method overriding.

🧱 Assignment 1: Design Your Own Class
We designed a base class called Vehicle with attributes like make, model, and year, and a method display_info() to print basic details.

🔧 Features:
Base Class: Vehicle

Subclasses: Car, Plane, Boat

Each subclass:

Inherits from Vehicle

Adds specific attributes (num_doors, wingspan, length)

Overrides the move() method

🎭 Activity 2: Polymorphism Challenge
The program uses polymorphism by having multiple subclasses define their own version of the move() method.

For example:

Car.move() → "Driving on the road 🚗"

Plane.move() → "Flying in the sky ✈️"

Boat.move() → "Sailing on the water 🚤"

A function vehicle_moves_demo() accepts a list of Vehicle objects and calls their move() method, demonstrating how the same method name can behave differently depending on the object.

📂 Files
main.py: Contains the class definitions and demo function

README.md: This file 😊

🧠 Key Concepts Covered
✅ Class & Object creation

✅ Constructors (__init__)

✅ Inheritance

✅ Method Overriding

✅ Polymorphism

▶️ How to Run
Make sure you have Python installed. Run the script with:

bash
Copy code
python main.py
You’ll see each vehicle’s info and its specific movement behavior printed to the console.

🚀 Bonus Ideas
Add a Motorcycle or Helicopter class

Include encapsulation with private attributes

Track total number of vehicles using a class variable

