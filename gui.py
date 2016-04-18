import calc
import graph
from ui import Ui_Form


class MainWindowSlots(Ui_Form):
    def calc(self):
        function = self.object_function.text()
        model_type = self.function_type.currentIndex()
        disp = float(self.hid_disp.text())
        is_eq = self.is_eq_acc.isChecked()
        iterations = self.iter_count.value()
        inter = self.interval_len.value()
        res = calc.calc(inter, iterations, disp, function, is_eq, 1, model_type)
        model = res['model']
        self.model_function.setText(model)
        sample = res["sample"]
        model_res = []
        for i in sample.input_values:
            model_res.append(calc.calc_function(i, model))
        graph.graph(sample.input_values, sample.true_values, sample.object_values, model_res)
        return None
