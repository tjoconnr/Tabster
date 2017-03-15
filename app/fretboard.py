#!/usr/bin/env python
import logging
from google.appengine.api import memcache

NOTES = {
	0: "C",
	1: "Db",
	2: "D",
	3: "Eb",
	4: "E",
	5: "F",
	6: "Gb",
	7: "G",
	8: "Ab",
	9: "A",
	10: "Bb",
	11: "B"
}
SCALES = {		
	1: {
		"name": "Major (Ionian)",
		"notes": [2,2,1,2,2,2,1]
	},
	2: {
		"name": "Dorian",
		"notes": [2,1,2,2,2,1,2]
	},
	3: {
		"name": "Phygrian",
		"notes": [1,2,2,2,1,2,2]
	},
	4: {
		"name": "Lydian",
		"notes": [2,2,2,1,2,2,1]
	},
	5: {
		"name": "Myxolydian",
		"notes": [2,2,1,2,2,1,2]
	},
	6: {
		"name": "Natural Minor (Aeolian)",
		"notes": [2,1,2,2,1,2,2]		
	},
	7: {
		"name": "Locrian",
		"notes": [1,2,2,1,2,2,2]		
	},
	8: {
		"name": "Chromatic",
		"notes": [1,1,1,1,1,1,1,1,1,1,1]
	}
}
TUNINGS = {
	0: {
		"name": "Guitar - Standard Tuning",
		"tuning": [0,5,5,5,4,5],
		"root": 4
	}	
}

def get_fretboard_cached(cache_seconds=60*60*24*30):    
        cache_key = "get_fretboard_cached"
        data = memcache.get(cache_key)        
        if data is None:            
            data = get_fretboard()
            if data:
                memcache.add(cache_key, data, cache_seconds)       
        return data

def get_fretboard():
	return {
		"notes": NOTES,		
		"scales": SCALES,
		"tunings": TUNINGS
	}