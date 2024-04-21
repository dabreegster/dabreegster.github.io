not including things I did interning at FB or working for Google

# Axes

- tech stack / language?
- status?
- audience?
- git repo
- link to docs / homepage maybe
- image / video
- description

# Modern

- route snapper
	- A MapLibre plugin to draw routes and areas that snap to an existing road network from OpenStreetMap.
	- status: ready
	- audience: web developers
- Bus spotting
	- View GTFS data interactively and match real GPS traces and bus ticketing events to the schedule.
	- status: abandoned prototype
	- audience: eventually transit agencies, but not useful yet
- odjitter
	- Generate specific origin/destination data from zone-based summaries
	- status: Usable, but abandonded -- use od2net instead
	- audience: data scientists
- A/B Street platform
	- A/B Street traffic simulator
		- Simulate individual cars, pedestrians, cyclists, and buses anywhere in the world with OpenStreetMap. Edit lane configuration and traffic signal timing. Run A/B tests with those edits and measure effects on individual agents and aggregate groups. Includes a gamified tutorial mode to teach the controls.
		- audience: the general public, to explore and propose ideas. gov agencies and campaign groups, to communicate proposals interactively.
		- status: Unmaintained, with no future plans. Very buggy; getting a "realistic" baseline simulation that doesn't crash or gridlock is nearly impossible.
	- Ungap the map
		- Quickly sketch improvements to a bike network and evaluate the benefits
		- audience: general public and planners
		- status: Usable, in maintenance mode. od2net is the spiritual successor
	- 15m neighbourhood
		- Use isochrones to explore what shops are a short walk away from where people live.
		- audience: general public and planners
		- status: Usable, in maintenance mode. There are big limits with the pedestrian pathfinding; Severance Snape is a newer project focusing on those.
	- 15m santa
		- An arcade game where Santa delivers presents and uses the Christmas magic of upzoning to improve land use patterns.
		- audience: anybody -- I've heard happy things particularly from younger children, and middle/high school teachers using this in class to introduce problems with land use
		- status: pretty much the only thing I consider DONE
	- LTN tool
		- Explore how modal filters can solve the problem of drivers cutting through residential areas
		- audience: general public and planners. this is my most-used project; over 30 councils and consultants in the UK and other countries are using it.
		- status: Usable, but with some big limitations around neighbourhood boundaries. Development is continuing with an experimental rewrite.
	- Parking mapper
		- A tool to more quickly update OSM with street parking
		- audience: OSM mappers
		- status: Usable, but abandoned. Use zlant instead.
	- OSM viewer
		- A tool to view OSM data
		- audience: OSM mappers
		- status: Usable, but abandoned. Web viewers, QGIS, osm2streets Street Explorer, etc are probably nicer.
	- widgetry
		- A 2D drawing and UI Rust library for native and web that powers all of the A/B Street apps
		- audience: Rust developers
		- status: Used in all A/B Street apps, but abandoned. All of my current projects are targeting web only, using Svelte and MapLibre instead.
	- osm2streets
		- Transform OSM data to a detailed geometric and semantic representation of streets, intersections, and turns. Primarily a library callable in Rust, JS, or Java. Powers A/B Street. Also has a Street Explorer web app to quickly view, and a lane editor to fix OSM tagging.
		- audience: OSM mappers and software developers
		- status: Maintenance mode. Many limitations, but no active work. Some big experiments in canvas_geometry, but far from results.
- ATIP scheme sketcher
	- Sketch proposed walking/cycling infrastructure on a map and fill out forms to describe it
	- audience: gov agencies, but easy enough for anyone
	- status: active development, my day job
- ATIP scheme browser
	- View ATIP scheme data alongside over 30 contextual layers, to help evaluate the proposed schemes
	- audience: internal gov (though public version is available without scheme data or all layers)
	- status: active development, my day job
- country-geocoder
	- Look up

- atip data prep
- lines2pmtiles


- od2net

- severance snape
- canvas_geometry
- ltn 2.0
- elevation
- osm-reader
- temporal city
- svg face


- geojson-viewer
- geodiffr

# Projects I'm involved in, but not leading

- SPC
- popgetter

# Half-baked experiment...

- odviz
- nolli
- glitch city

and TODO: calculate road width

# Apocrypha (before 2018)

- AORTA
- mnemonicrl
- jmd
	- i use this every single day of my life and have since i wrote it. so...
	- sqlite, perl, mpg321 api, ncurses UI (hexedui)
- hexedui
	- before widgetry, a much more cursed UI lib...
- 3d scala osm viewer
- campus map
- maybe some stuff with TGF / MMF... i got started with that
