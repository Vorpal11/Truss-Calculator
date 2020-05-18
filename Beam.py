class Beam:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.force = None

    def draw(self, canvas):
        # Implement later

        # Blue = inward
        # Red = outward
        # Compression
        canvas.create_line(self.start[0], self.start[1], self.end[0], self.end[1])
