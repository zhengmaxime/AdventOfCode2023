l = open('f2').readlines()
times = l[0].split(':')[1].split()
distances = l[1].split(':')[1].split()
print(times, distances)
res = 1
for duration, max_distance in zip(times, distances):
    duration = int(duration)
    max_distance = int(max_distance)
    t = 0
    nb_ways = 0
    while t < duration:
        distance = t * (duration - t)
        if distance > max_distance:
            nb_ways += 1
        t += 1
    res *= nb_ways
print(res)
