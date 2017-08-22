#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 21:49:54 2017

@author: ivanchen
"""

import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_Triangle(some_turtle):
    for i in range(3):
        some_turtle.forward(100)
        some_turtle.right(120)
    
def draw_art():        
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a sqaure
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)
    for i in range(36):
        draw_square(brad)
        brad.right(10)
    #Create the turtle Angie = Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
        
    window.exitonclick()
    
def draw_test():
    window = turtle.Screen()
    window.bgcolor("black")
    
    daniel = turtle.Turtle()
    daniel.shape("turtle")
    daniel.color("white")
    #daniel.speed(200)
    #for i in range(120):
    draw_Triangle(daniel)
        #daniel.right(3)
    
    window.exitonclick()
    
def draw_house():
    window = turtle.Screen()
    window.bgcolor("black")
    
    daniel = turtle.Turtle()
    daniel.shape("turtle")
    daniel.color("white")
    
    daniel.left(60)
    draw_Triangle(daniel)
    daniel.right(60)
    draw_square(daniel)
    
    window.exitonclick()
    
#draw_art()
#draw_test()
draw_house()