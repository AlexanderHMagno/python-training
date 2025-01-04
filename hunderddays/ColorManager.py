import colorgram
import random

class ColorManager:
    def __init__(self, path_to_image):
        self.path_to_image = path_to_image
        self.colors = self._extract_colors()
        self.list_of_colors = self._process_colors()
        
    def _extract_colors(self):
        # Extract 6 colors from an image
        return colorgram.extract(self.path_to_image, 6)
        
    def _process_colors(self):
        colors_list = []
        for color in self.colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            colors_list.append((r, g, b))
        return colors_list
    
    def get_random_color(self):
        return random.choice(self.list_of_colors)
