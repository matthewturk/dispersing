import dispersing

ts = dispersing.TheSummoning("the-summoning/")

for i, level in enumerate(ts.levels[:1]):
    image = level.create_map()
    image.save(f"levels/level_{i:02}.png")