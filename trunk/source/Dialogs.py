DIALOGS = {
	'Open1': [
		["Lorem ipsum dolar sit",
		 "consecutor."],
		
		["Jackdaws love my",
		 "sphinx of qwartz"]
	],
	
	'Open2': [
		["The quick brown fox",
		 "Jumped over the lazy",
		 "dogs."],
		
		["And the cow jumped",
		 "over the moon."],
		
		["...because the theme",
		 "is `Moon\"."]
	],
	
	'Open3': [
		["And he says to",
		 "himself..."],
		
		["`I've made a huge",
		 "mistake.\""]
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
				
