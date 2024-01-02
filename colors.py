class Colors:
    #dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    modern_yellow = (255, 255, 0)
    modern_red = (255, 0, 0)
    modern_pink = (255, 105, 180)
    modern_light_blue = (173, 216, 230)
    modern_violet = (138, 43, 226)
    modern_teal = (0, 128, 128)
    dark_blue = (44, 44, 127)
    white = (255, 255, 255)
    

    @classmethod
    def get_cell_colors(cls):
        return [cls.modern_teal, cls.modern_pink, cls.red, cls.purple, cls.modern_violet, cls.cyan, cls.green, cls.modern_yellow]
