# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc, random
from copy import copy
from GlyphsApp import *
from GlyphsApp.plugins import *

class COLRCPALJuggler(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'COLR/CPAL Juggler',
			'de': 'COLR/CPAL-Jongleur',
			'fr': 'Jongleur COLR/CPAL',
			})

	@objc.python_method
	def filter(self, masterLayer, inEditView, customParameters):
		if masterLayer.isMasterLayer:
			print("master:", masterLayer)
			thisGlyph = masterLayer.parent
			thisMaster = masterLayer.master
			if thisMaster:
				mID = thisMaster.id
				print("mID", mID)
				availableColorLayers = [l for l in thisGlyph.layers if l.associatedMasterId==mID and l.attributes and "colorPalette" in l.attributes.keys()]
				if availableColorLayers:
					for colorLayer in availableColorLayers:
						colorLayer.clear()
					for thisShape in masterLayer.shapes:
						targetLayer = random.choice(availableColorLayers)
						targetLayer.shapes.append(copy(thisShape))
			else:
				print("no master ID")

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
