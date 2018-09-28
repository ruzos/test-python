#-*- coding: utf8 -*-

"""
kalkulator BMI
"""

print("Podaj wage w kg: ")
weight = float(input())
print("Podaj wzrost w m: ")
height = float(input())
BMI = weight / (height ** 2)
print("Twoje BMI wynosi: ", round(BMI,3))

