class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def transform(self, change, operation):
        match operation:
            case "add":
                self.x += change.x
                self.y += change.y
            case "multiply":
                self.x = self.x * change.x
                self.y = self.y * change.y
