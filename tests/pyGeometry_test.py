import unittest
import os
import sys

CS_FOLDER = os.getcwd()
SDK_PATH = os.path.join(CS_FOLDER, "install", "bin")
sys.path.append(SDK_PATH)

import pyprt

def asset_file(filename):
    return os.path.join(CS_FOLDER, "data", filename)


def combine_reports(model):
    combined_dict = {}
    combined_dict.update(model.get_float_report())
    combined_dict.update(model.get_string_report())
    combined_dict.update(model.get_bool_report())
    return combined_dict

class GeometryTest(unittest.TestCase):
    def test_verticesNber_candler(self):
        rpk = asset_file("candler.rpk")
        attrs = {'ruleFile' : "bin/candler.cgb", 'startRule' : "Default$Footprint"}
        shape_geo_from_obj = asset_file("candler_footprint.obj")
        m = pyprt.ModelGenerator(shape_geo_from_obj)
        model = m.generate_model(rpk, attrs, {'emitReports' : False, 'emitGeometry' : True})
        self.assertEqual(len(model[0].get_vertices()), 97050)

    def test_facesNber_candler(self):
        rpk = asset_file("candler.rpk")
        attrs = {'ruleFile' : "bin/candler.cgb", 'startRule' : "Default$Footprint"}
        shape_geo_from_obj = asset_file("candler_footprint.obj")
        m = pyprt.ModelGenerator(shape_geo_from_obj)
        model = m.generate_model(rpk, attrs, {'emitReports' : False, 'emitGeometry' : True})
        self.assertEqual(len(model[0].get_faces()), 47202)

    def test_report_green(self):
        rpk = asset_file("envelope1806.rpk")
        attrs = {'ruleFile' : "rules/typology/envelope.cgb", 'startRule' : "Default$Lot", 'report_but_not_display_green' : True}
        shape_geo_from_obj = asset_file("bigFootprint_0.obj")
        m = pyprt.ModelGenerator(shape_geo_from_obj)
        model = m.generate_model(rpk, attrs, {'emitReports' : True, 'emitGeometry' : False})
        ground_truth_dict = {'Number of trees_avg': 1.0, 'Number of trees_max': 1.0, 'Number of trees_min': 1.0, 'Number of trees_n': 168.0, 'Number of trees_sum': 168.0, 'green area_avg': 3.9, 'green area_max': 1049.11, 'green area_min': 0.49, 'green area_n': 750.0, 'green area_sum': 2925.84, 'total report for optimisation_avg': 5.02, 'total report for optimisation_max': 1049.11, 'total report for optimisation_min': 0.49, 'total report for optimisation_n': 918.0, 'total report for optimisation_sum': 4605.84}
        rep = model[0].get_float_report()
        rep_round = { x : round(z, 2) for x,z in rep.items()}
        self.assertEqual(rep_round, ground_truth_dict)

    def test_noReport(self):
        rpk = asset_file("simple_rule0819.rpk")
        attrs = {'ruleFile' : "bin/simple_rule2019.cgb", 'startRule' : "Default$Footprint"}
        shape_geo = pyprt.Geometry([-10.0, 0.0, 5.0, -5.0, 0.0, 6.0, 20.0, 0.0, 5.0, 15.0, 0.0, 3.0])
        m = pyprt.ModelGenerator([shape_geo])
        model = m.generate_model(rpk, attrs, {'emitReports' : False})
        self.assertDictEqual(combine_reports(model[0]),{})

    def test_noGeometry(self):
        rpk = asset_file("simple_rule0819.rpk")
        attrs = {'ruleFile' : "bin/simple_rule2019.cgb", 'startRule' : "Default$Footprint"}
        shape_geo = pyprt.Geometry([-10.0, 0.0, 5.0, -5.0, 0.0, 6.0, 20.0, 0.0, 5.0, 15.0, 0.0, 3.0])
        m = pyprt.ModelGenerator([shape_geo])
        model = m.generate_model(rpk, attrs, {'emitGeometry' : False})
        self.assertListEqual(model[0].get_vertices(),[])

    def test_buildingheight(self):
        rpk = asset_file("simple_rule0819.rpk")
        attrs = {'ruleFile' : "bin/simple_rule2019.cgb", 'startRule' : "Default$Footprint"}
        attrs2 = {'ruleFile' : "bin/simple_rule2019.cgb", 'startRule' : "Default$Footprint", 'minBuildingHeight' : 23.0, 'maxBuildingHeight' : 23.0}
        shape_geo = pyprt.Geometry([-10.0, 0.0, 10.0, -10.0, 0.0, 0.0, 10.0, 0.0, 0.0, 10.0, 0.0, 10.0])
        m = pyprt.ModelGenerator([shape_geo])
        model1 = m.generate_model(rpk, attrs)
        model2 = m.generate_another_model(attrs2, {'emitReports' : False})
        z_coord = [round(b,1) for a,b,c in model2[0].get_vertices()]
        for z in z_coord:
            if z:
                self.assertAlmostEqual(abs(z), 23.0)



if __name__ == '__main__':
    unittest.main()