---
layout: page
title: Projects
---

WIP. Running Jekyll locally is hitting dependency hell, so deploying is the way to test for now.

## A/B Street platform, first generation

### A/B Street traffic simulator

The project that started it all.

- Simulate individual cars, pedestrians, cyclists, and buses anywhere in the world with OpenStreetMap
- Edit lane configuration and traffic signal timing
- Run A/B tests with those edits and measure effects on individual agents and aggregate groups
- Includes a gamified tutorial mode to teach the controls

![](traffic_sim.gif)
TODO: the poundbury animation
TODO: youtube trailer

![](edit_roads.gif)
![](edit_signals.gif)

- [Site](https://traffic.abstreet.org)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/game)
- Audience: The general public, to explore and propose changes to their city. Government agencies and campaign groups, to communicate proposals more interactively.
- Status: Unmaintained, with no future plans. Very buggy; getting a "realistic" baseline simulation that doesn't crash or gridlock is challenging.

### Ungap the Map

Quickly sketch improvements to a bike network and evaluate the benefits

![](ungap_the_map.gif)

- [Site](https://bike.abstreet.org)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/game/src/ungap)
- Audience: The general public and transport professionals
- Status: Usable, but in maintenance mode. od2net is the spiritual successor.

### The 15 minute neighbourhood tool

Use isochrones to explore what shops are a short walk away from where people live.

- [Site](https://15m.abstreet.org)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/fifteen_min)
- Status: Usable, but in maintenance mode. Likely to be revived as a web-first project. There are big limits with the pedestrian pathfinding; Severance Snape is a newer project focusing on those.

### 15-minute Santa

An arcade game where Santa delivers presents and uses the Christmas magic of upzoning to improve land use patterns.

![](santa.gif)

- [Site](https://santa.abstreet.org)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/santa)
- Audience: Anybody! I've heard happy things particularly from younger children, and middle/high school teachers using this in class
- Status: Done! (The only project I consider truly complete.)

### The low-traffic neighbourhood (LTN) tool

Explore how modal filters can solve the problem of drivers cutting through residential areas

- [Site](https://ltn.abstreet.org)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/ltn)
- Audience: The general public and transport professionals. This is my most-used project; over 30 councils, consultants, and individuals in the UK and other countries are using it.
- Status: Usable, but with some big limitations around neighbourhood boundaries. A new version is "nearly" ready to replace this.

### Parking mapper

A tool to more quickly update OSM with street parking

- [Site](https://a-b-street.github.io/docs/software/parking_mapper.html)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/parking_mapper)
- Audience: OSM mappers
- Status: Usable, but abandoned. Use [zlant's tool](https://zlant.github.io/parking-lanes) instead.

### OSM viewer

An OSM data exploration tool

- [Site](https://a-b-street.github.io/docs/software/osm_viewer.html)
- [Code](https://github.com/a-b-street/abstreet/tree/main/apps/osm_viewer)
- Audience: OSM mappers
- Status: Usable, but abandoned. [Overpass](https://overpass-turbo.eu), QGIS, [osm2streets Street Explorer](https://osm2streets.org), etc are better.

### widgetry

A 2D drawing and UI Rust library for native and web that powers all of the A/B Street apps

- [Code](https://github.com/a-b-street/abstreet/tree/main/widgetry)
- Audience: Rust developers
- Status: Used in all A/B Street apps, but abandoned. All of my current projects are targeting web only, using Svelte and MapLibre instead.

### osm2streets

- Transform OSM data to a detailed geometric and semantic representation of streets, intersections, and turns.
- Primarily a library callable in Rust, JS, or Java
- Has a Street Explorer web app to visualize results
- Has a lane editor app to fix OSM tagging

![](osm2streets.png)

- [Street Explorer](https://osm2streets.org)
- [Lane editor](https://a-b-street.github.io/osm2streets/lane_editor.html)
- [Code](https://github.com/a-b-street/osm2streets)
- Audience: OSM mappers and software developers
- Status: Active development. Powers all A/B Street apps.
