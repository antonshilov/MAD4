import calc
import graph
from ui import Ui_Form


class MainWindowSlots(Ui_Form):
    sample = calc.Sample()

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
        self.sample = res["sample"]
        model_res = []
        for i in self.sample.input_values:
            model_res.append(calc.calc_function(i, model))
        self.sample.model_vals = model_res
        return None

    def graph(self):
        graph.graph(self.sample.input_values, self.sample.true_values, self.sample.object_values,
                    self.sample.model_vals)
        return None
