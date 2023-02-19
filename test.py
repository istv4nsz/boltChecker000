import sys
import m_axisvm_connect as ac
from m_bolt_checker import BoltCheckInputData
from m_globs import Globs
import dataclasses
import json
import webbrowser

with open("control.json", "r") as infile:
  json_object = json.load(infile)
linkelements = {}
linkelements[0]=BoltCheckInputData()
for le in json_object:
  #linkelements[le] = type("BoltCheckInputData", (), json_object[le])
  linkelements[le] = BoltCheckInputData(**json_object[le])
print(linkelements[0].bolt_dia_mm)
print(linkelements['2'].bolt_dia_mm)

