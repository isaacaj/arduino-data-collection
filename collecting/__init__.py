from collecting import collect

thing = []
thing = collect.collect_raw_data(3)
thing = collect.scrub_data(thing)
print(str(thing))
