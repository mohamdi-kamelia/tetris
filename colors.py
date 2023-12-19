class colors :
    dark_grey = (26, 31, 40)
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
    @classmethod
    def get_cell_colors(cls):
        return [cls.modern_teal, cls.modern_pink, cls.red, cls.purple, cls.modern_violet, cls.modern_light_blue, cls.green, cls.modern_yellow]
