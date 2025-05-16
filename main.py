
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.inputs = {}
        fields = [
            ("Dioptria esférica", "esferica"),
            ("Cilindro", "cilindro"),
            ("Índice do molde", "indice_molde"),
            ("Índice do material", "indice_material"),
            ("Curva externa", "curva_externa")
        ]

        for label_text, key in fields:
            input_box = TextInput(hint_text=label_text, multiline=False, input_filter='float')
            self.inputs[key] = input_box
            layout.add_widget(input_box)

        self.result_label = Label(text="Resultado:")

        calcular_btn = Button(text="Calcular", on_press=self.calcular)
        layout.add_widget(calcular_btn)
        layout.add_widget(self.result_label)

        return layout

    def calcular(self, instance):
        try:
            E = float(self.inputs["esferica"].text)
            C = float(self.inputs["cilindro"].text)
            im = float(self.inputs["indice_molde"].text)
            ir = float(self.inputs["indice_material"].text)
            CE = float(self.inputs["curva_externa"].text)

            # Dioptria real
            DR_esf = abs(E) * im / ir
            DR_cil = abs(C) * im / ir

            # Curva interna
            if E >= 0:
                CI = CE - DR_esf
            else:
                CI = CE + DR_esf

            # Molde
            molde_cil = CI + DR_cil
            resultado = (
               
                f"Molde: {CI:.2f} / {molde_cil:.2f}"
            )

            self.result_label.text = resultado
        except Exception as e:
            self.result_label.text = "Erro no cálculo. Verifique os valores."

if __name__ == '__main__':
    MainApp().run()
