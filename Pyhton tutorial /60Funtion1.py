# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:29:27 2018

@author: narendra
"""

def tax(bill):
  """Adds 8% tax to a restaurant bill."""
  bill *= 1.08
  print ("With tax: %f" % bill)
  return bill

def tip(bill):
  """Adds 15% tip to a restaurant bill."""
  bill *= 1.15
  print ("With tip: %f" % bill)
  return bill
  
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)