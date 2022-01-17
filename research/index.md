---
layout: page
title: Research
---

In December 2021, I joined a group at [The Alan Turing
Institute](https://www.turing.ac.uk) that's studying **ecosystems of digital
twins**. From my software engineering perspective, this means making sure that
research projects don't start from scratch -- intermediate datasets are
re-used, common code is cleaned up and published with a clear API, and
interoperability between software is prioritized. That way, we can more quickly
build simulations of transportation, land use, health, energy use, and other
domains.

I have drafted a tentative "top-down" plan of how this ecosystem could all fit
together, but much more concretely, the "bottom-up" approach is already
yielding fruit. This is similar to my earlier dream of detangling A/B Street
into more modular pieces. We've already succeeded at building different tools
on a common platform -- for traffic simulation, 15-minute cities, low-traffic
neighborhoods, planning cycling networks, mapping OpenStreetMap parking data,
etc. The next step is to extract the generally useful pieces of A/B Street's
extensive OpenStreetMap importing process.

In progress:

- [osm2lanes](https://github.com/a-b-street/osm2lanes): Transform OpenStreetMap
  tags to lanes, with a clear schema
- [odjitter](https://github.com/dabreegster/odjitter): Disaggregate
  origin/destination travel demand data into individual trips

Up next (many of these particularly helpful for travel demand models):

- osm2polygons: Transform road center-lines to road and intersection polygons,
  using
  [A/B Street's current approach](https://a-b-street.github.io/docs/tech/map/geometry/index.html)
- Detect OpenStreetMap areas with missing buildings and procedurally generate
  houses
- Easily get an up-to-date OpenStreetMap extract for an arbitrary boundary
  - Possibly using Geofabrik and existing merging/clipping tools
  - Also keeping an eye on [Protomaps](https://protomaps.com)
- Extract weighted points-of-interest from OpenStreetMap
  - Many travel demand models send more trips to buildings tagged as
    supermarkets than cafes. Can we refactor that process and share some common
    weighting profiles used?
- osm2turns: At a single intersection, calculate all vehicle and pedestrian
  movements possible, accounting for restrictions
- Routing: ensure researchers are able to easily run vehicle and pedestrian
  pathfinding on their local machines at city and natonal scales
  - This will likely just be a short guide pointing to OSRM, GraphHopper,
    Valhalla, etc
  - Also have some ideas for auto-tuning routing profiles based on traffic
    counts and jittered OD datasets

The goal for all of these components will be cross-platform compatibility (with
most pieces also working directly in a browser using WebAssembly), great
performance, and being language agnostic -- many colleagues work in R, Python,
and Java. So not unsurprisingly, I'll lean heavily towards Rust for most of
these -- but in osm2lanes, for example, we've also got a Kotlin and Python
implementation going, and the processes set up to keep the 3 codebases in sync.

Other ideas on my radar:

- Idempotent pipelines that download external sources, run a directed acyclic
  graph of tasks, and manage output under some form of version control
  - This will probably be evaluating and recommending some
    [awesome pipeline](https://github.com/pditommaso/awesome-pipeline)
- Exploring data formats with strict schemas for interoperability -- GeoJSON
  with a specification, [flatgeobuf](https://flatgeobuf.org), protocol buffers,
  etc
- Exploring a transportation network representation with much more detailed
  geometry -- based on partitioning 2D space into polygons, rather than road
  center-lines

If you'd like to discuss any of these ideas or collaborate, get in touch:
<dcarlino@turing.ac.uk>
