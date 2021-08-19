squared = lambda x: x**2

print(squared(8))

squares = list(map(lambda x: x**2, range(10)))

print(squares)

sum = lambda x, y:   x + y   #  def sum(x,y): return x + y; used for fairly simple functions, and used only once!

g = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(g("   leonhard  "," Euler"))

scifi_list = ["Isaac Asimov", "Douglas Adams", "Orson Scott Card", "Ray Bradburry"]

scifi_list.sort(key=lambda name: name.split(" ")[-1].lower()) #.lower: sroting now not case sensitive

print(scifi_list)

def get_last(word):
    return word[-1]

locations = ["spain", "indonesia", "germany"]

locations.sort(key=lambda x: x[-1])
print(locations)
print(sorted(locations, key=lambda x: x[-1]))
print(sorted(locations, key=get_last))
