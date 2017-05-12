__author__ = 'kaushik'


class Building:

        def __init__(self,construct):
               self.construction_type = construct

        material = 'Concrete'
        builder_a = ['abc corp','def corp']

        def start_build(self, buildtype,height):
            return 'A building of type ' + buildtype + ' with height ' + str(height)



c1 = Building('School')

print (c1.material)
print (c1.start_build(c1.construction_type,6))