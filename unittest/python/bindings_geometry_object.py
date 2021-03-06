import unittest
import pinocchio as pin
import numpy as np

@unittest.skipUnless(pin.WITH_FCL_SUPPORT(),"Needs FCL")
class TestGeometryObjectBindings(unittest.TestCase):

    def setUp(self):
        model = pin.buildSampleModelHumanoid()
        self.collision_model = pin.buildSampleGeometryModelHumanoid(model)

    def test_name_get_set(self):
        col = self.collision_model.geometryObjects[0]
        self.assertTrue(col.name == 'rlegshoulder_object')
        col.name = 'new_collision_name'
        self.assertTrue(col.name == 'new_collision_name')

    def test_parent_get_set(self):
        col = self.collision_model.geometryObjects[0]
        self.assertTrue(col.parentJoint == 2)
        col.parentJoint = 3
        self.assertTrue(col.parentJoint == 3)

    def test_placement_get_set(self):
        m = pin.SE3.Identity()
        new_m = pin.SE3.Random()
        col = self.collision_model.geometryObjects[0]
        self.assertTrue(np.allclose(col.placement.homogeneous,m.homogeneous))
        col.placement = new_m
        self.assertTrue(np.allclose(col.placement.homogeneous , new_m.homogeneous))

    def test_meshpath_get(self):
        col = self.collision_model.geometryObjects[0]
        self.assertTrue(col.meshPath == "")

if __name__ == '__main__':
    unittest.main()
