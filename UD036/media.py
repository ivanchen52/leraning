#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:33:14 2017

@author: ivanchen

This class provides a way to store movie related information
"""
import webbrowser

class Movie():
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self,movie_title,movie_sotryline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_sotryline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)