DIALOGS = {
	'Open1': [
		["An intrepid explorer",
		 "left home in search of",
		 "a better life for all",
		 "squirrelkind."],
		
		["Bearing the hopes and",
		 "dreams of her people,",
		 "the squirrel set course",
		 "for a nearby moon."],
	],
	
	'Open2': [
		["Her vessel reaches the",
		 "moon laden with large",
		 "supply stores as well as",
		 "terraforming equipment"],
		
		["...including the very",
		 "latest in hydration",
		 "technology:"],
		
		["Giant water balloons."],
	],
	
	'Open3': [
		["As she gazes upon the",
		 "barren waste of the",
		 "desolate moon, she",
		 "says to herself:"],
		
		["`I've got a lot of",
		 "work to do.\""]
	],

	'Volcano': [
		["That's the last of the",
		 "volcanos."],
		 
		["Now that the magnetic",
		 "field is back, the",
		 "atmosphere will",
		 "re-accumulate."]
	],
	
	'T1': [
		["Hello explorer! We trust",
		"your journey was a",
		"pleasant one."],

		["Your first task is to",
		"normalize the gravity on",
		"the moon."],
	
		["Place the gravity",
		"emitter within the",
		"moon's core."],
	
		["Remember we're relying",
		"on you; don't forget the",
		'`gravity" of our',
		"situation!"]
	],
	
	
	'T2': [
		["Now in order to restore",
		"the moon's magnetic",
		"field, you'll need some",
		"specialized equipment."],

		["Take your packet of",
		"Acme Instant Lava and",
		"sprinkle a little into",
		"inactive volcanoes."],
		
		["Presto, lava! And as",
		"everyone knows, lava",
		"creates magnetic fields."],

		["SCIENCE!"]
	],

	'T3': [
		["When you landed, your",
		"H2O reservoirs should",
		"have been released."],
		
		["You will need to break",
		"the rubber coating on",
		"the reservoirs to",
		"release the water."]
	],
	
	'T4': [
		["We have a small hiccup;",
		"the seeds intended to",
		"provide vegetation were",
		"accidentally left here."],

		["Fortunately, a vanguard",
		"of our sworn enemies is",
		"heading to your location",
		"bearing their own seeds."],

		["You can simultaneously",
		"stop their invasion and",
		"steal their seeds for",
		"our own purposes."],

		["It's a case of killing",
		"two birds with one",
		"stone! Or anything else",
		"you might prefer."]
	],
	
	'CloseDialog': [
		["Congratulations!",
		 "The Space Squirrel has",
		 "managed to bring life",
		 "to this once dead moon."],
		 
		["Now her people have a",
		 "beautiful new home, and",
		 "it's all thanks to you!"]
	]
}

tooBig = False
for key in DIALOGS.keys():
	for stanza in DIALOGS[key]:
		for line in stanza:
			if len(line) > 24:
				print("The following line is too long in conversation '" + key + "':")
				print('    >',line)
				tooBig = True

if tooBig:
	print("Will divide by zero and crash until Satyrane fixes it.")
	z = 1 / 0 # error
				
