import dispersing

ts = dispersing.TheSummoning("/home/matthewturk/the-summoning/")

for i, level in enumerate(ts.levels[:10]):
    image = level.create_map()
    image.save(f"levels/level_{i:02}.png")