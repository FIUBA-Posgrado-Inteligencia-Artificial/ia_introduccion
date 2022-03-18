# Example 1

# import Ejemplos.clase_2.estructura_proyecto.modules.utils_example
# utils_example.printer(utils_example.default_shape)
# shape = utils_example.Shape('circle')
# utils_example.printer(shape)

# Example 2

# from Ejemplos.clase_2.estructura_proyecto.modules.utils_example import *
# printer(default_shape)
# shape = Shape('circle')
# printer(shape)

# Example 3
from Ejemplos.clase_2.estructura_proyecto.modules.utils_example import Shape, printer as myfunc

s = Shape('oval')
myfunc(s)

# Example 4
# from Ejemplos.clase_2.estructura_proyecto.modules.utils_example import *
# _special_function()
