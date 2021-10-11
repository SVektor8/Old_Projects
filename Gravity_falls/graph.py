def trans(height, width, box_height, box_width, *args):  # преобразование для интерпретатора из удобной
    x0 = args[0][0]
    y0 = args[0][1]
    return int(width + x0 - box_width / 2), int(height - box_height / 2 - y0)


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def collide(self, body):
    if round(distance(self.x, self.y,
                      body.x, body.y), 5) <= \
            round(distance(self.speed_x, self.speed_y,
                           body.speed_x, body.speed_y), 5) * 2:
        if self.elasticity + body.elasticity == 2:
            self.speed_x = (2 * body.mass * body.speed_x +
                            (self.mass - body.mass) * self.speed_x) / \
                           (self.mass + body.mass)
            self.speed_y = (2 * body.mass * body.speed_y +
                            (self.mass - body.mass) * self.speed_y) / \
                           (self.mass + body.mass)
            body.speed_x = (2 * self.mass * self.speed_x +
                            (body.mass - self.mass) * body.speed_x) / \
                           (self.mass + body.mass)
            body.speed_y = (2 * self.mass * self.speed_y +
                            (body.mass - self.mass) * body.speed_y) / \
                           (self.mass + body.mass)
