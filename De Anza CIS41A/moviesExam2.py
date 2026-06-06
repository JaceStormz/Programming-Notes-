class Movie:

    def __init__(self, line):
        parts = line.split(",")

        self.title = parts[0]

        self.number = float(parts[1])

    def __lt__(self, other):
        return self.number < other.number

    def __str__(self):
        return f"{self.title} ({self.number})"

line = "Star Wars,2.23"
movie1 = Movie(line)

line = "The Lego Movie 2,9.16"
movie2 = Movie(line)


if movie1 < movie2:
    print("first movie came out earlier")

line = "Top Gun: Maverick,eleven"
movie3 = Movie(line)