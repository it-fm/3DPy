# myMenuContents.py
#Copyright (c) 2016, Logan Power
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
#1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
#2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
#THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
#IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# I'm just using this class as a container for variables, more or less.
class main:
    mainChars = ['q', 'm', 'x']
    mainOpts = ["Quick Calculate", "Select/Edit Material", "Exit"]
    mainComposite = [mainChars, mainOpts]

class quickCalcMenu:
    mainChars = ['q', 't', 'h', 'c', 'x']
    mainOpts = ["Set length used", "Set Time Spent", "Toggle flat handling charge", "Calculate", "Return to Main Menu"]
    mainComposite = [mainChars, mainOpts]

class editMaterialMenu:
    mainChars = ['n', 'd', 'g', 'k', 'h', 'c', 's', 'w', 'q']
    mainOpts = ["Name", "Diameter", "Density", "Cost per kilo", "Cost per Hour", "Handling Charge", "Select / Create New Material".upper(), "SAVE MATERIAL TO FILE", "Return to main menu"]
    mainComposite = [mainChars, mainOpts]