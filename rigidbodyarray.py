import bpy





size1=.5             #size of the object
inbetween_dist=1     #distance between two objects






def makerbd():                                                     #makes the object a ridgid body
    bpy.ops.rigidbody.object_add()
    bpy.context.object.rigid_body.collision_shape = 'BOX'          #sets the rigid body collision shape
    bpy.context.object.rigid_body.use_deactivation = True          #enable or disable deactivation
    bpy.context.object.rigid_body.use_start_deactivated  = True   #enable or disable start deactivated
    


class MESH_OT_rigidrody_array(bpy.types.Operator):
     """ Add A RigidBody array"""
     bl_idname="mesh.rigidbody_array"
     bl_label="RigidBody array"
     bl_options ={'REGISTER','UNDO'}
     
     x: bpy.props.IntProperty(          #no of objs in the x axis
        name="x",
        description="Number Of Cubes In The X Direction",
        default=2,
        min=1 , soft_max =5
     )
     
     y: bpy.props.IntProperty(          #no of objs in the y axis
        name="y",
        description="Number Of Cubes In The Y Direction",
        default=3,
        min=1 , soft_max =5
     )
     
     z: bpy.props.IntProperty(          #no of objs in the z axis
        name="z",
        description="Number Of Cubes In The Z Direction",
        default=4,
        min=0 , soft_max =5
     )
     
     size1: bpy.props.FloatProperty(          #no of objs in the z axis
        name="Size",
        description="Size Of The Individual Objects",
        default=2,
        min=0.1 , soft_max =10
     )
     
     
     inbetween_dist: bpy.props.FloatProperty(
        name="Inbetween Distance",
        description="distance between objects",
        default=1,
        min=1 
     )
     
     x_offset: bpy.props.FloatProperty(
        name="X Offset",
        description="Offset Along The X Axis",
        default=0,
        
     )
     
     y_offset: bpy.props.FloatProperty(
        name="Y Offset",
        description="Offset Along The Y Axis",
        default=0,
        
     )
     
     z_offset: bpy.props.FloatProperty(
        name="Z Offset",
        description="Offset Along The Z Axis",
        default=0,
        
     )
     
     rbd_density: bpy.props.FloatProperty(
        name="RigidBody Density",
        description="Density Of Each Object",
        default=100,
        min=0.01 
        
     )
     
     isdeactivated: bpy.props.BoolProperty(
        name="Rigid Body Deactivated",
        description="enable or disable deactivation",
        default=True,
     )
     
     startdeactivated: bpy.props.BoolProperty(
        name="Start Deactivated",
        description="enable or disable start deactivated",
        default=True,
     )
        
     on_floor: bpy.props.BoolProperty(
        name="On Floor",
        description="Spawn On The Floor Or At The World Origin",
        default=True,
        
     )
        
    
     def execute(self, context):
         
         
        def makerbd():                                                     #makes the object a ridgid body
            bpy.ops.rigidbody.object_add()
            bpy.context.object.rigid_body.collision_shape = 'BOX'          #sets the rigid body collision shape
            bpy.context.object.rigid_body.use_deactivation = self.isdeactivated          #enable or disable deactivation
            bpy.context.object.rigid_body.use_start_deactivated  = self.startdeactivated  #enable or disable start deactivated
            bpy.ops.rigidbody.mass_calculate(material='Custom', density=self.rbd_density)



        if self.on_floor == True:
            z_floor_offset=(self.size1/2)+self.z_offset
        else:
            z__floor_offset=0+self.z_offset
            
        
            
     
     

        for idx in range(self.x):
                    lx=idx*self.size1*self.inbetween_dist
                            
                    for idy in range(self.y):
                            
                        ly=idy*self.size1*self.inbetween_dist
                        bpy.ops.mesh.primitive_cube_add(
                        size=self.size1,
                        location=(lx+self.x_offset,ly+self.y_offset,z_floor_offset))
                        makerbd()

                                        
                        for idz in range(self.z-1):
                            bpy.ops.mesh.primitive_cube_add(
                            size=self.size1,
                            location=(lx+self.x_offset,ly+self.y_offset,((idz+1)*self.size1*self.inbetween_dist)+z_floor_offset)                     ) 
                            makerbd()
                            
                            
        return {"FINISHED"}
    

def register():
    bpy.utils.register_class(MESH_OT_rigidrody_array)

         
def unregister():
    bpy.utils.unregister_class(MESH_OT_rigidrody_array)       
    

if __name__ =='__main__':
    register()
    
