from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


# Function to calculate determinant
def det(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    result = 0
    for i in range(len(matrix)):
        minor = [row[:i] + row[i + 1:] for row in matrix[1:]]
        result += (-1) ** i * matrix[0][i] * det(minor)
    return result


# Function to replace a column in a matrix
def replace_column(matrix, constants, column_index):
    new_matrix = [row[:] for row in matrix]
    for i in range(len(constants)):
        new_matrix[i][column_index] = constants[i]
    return new_matrix


# Function to solve equations using Cramer's Rule
def solve_equations(coefficients, constants):
    determinant = det(coefficients)
    if determinant == 0:
        return "No solution (determinant is zero)"
    solutions = []
    for i in range(len(coefficients)):
        modified_matrix = replace_column(coefficients, constants, i)
        solutions.append(det(modified_matrix) / determinant)
    return solutions


class SolverApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)
        self.equation_count = 0
        self.coefficients = []
        self.constants = []

        # Layout for entering the number of equations
        self.input_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.05), spacing=10)  # Reduced height
        self.add_widget(self.input_layout)

        self.input_label = Label(text="Number of equations:", size_hint=(0.4, 1))
        self.input_layout.add_widget(self.input_label)

        self.input_field = TextInput(multiline=False, input_filter="int", size_hint=(0.2, 1))
        self.input_layout.add_widget(self.input_field)

        self.start_button = Button(text="Start", size_hint=(0.2, 1))
        self.start_button.bind(on_press=self.setup_equations)
        self.input_layout.add_widget(self.start_button)

        # Scrollable layout for equation inputs
        self.scroll = ScrollView(size_hint=(1, 0.7))
        self.equation_layout = GridLayout(cols=3, size_hint_y=None, spacing=10, padding=10)
        self.equation_layout.bind(minimum_height=self.equation_layout.setter("height"))
        self.scroll.add_widget(self.equation_layout)
        self.add_widget(self.scroll)

        # Solve and Clear buttons
        self.button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.2), spacing=10)
        self.solve_button = Button(text="Solve", size_hint=(0.5, 1))
        self.solve_button.bind(on_press=self.solve)
        self.button_layout.add_widget(self.solve_button)

        self.clear_button = Button(text="Clear", size_hint=(0.5, 1))
        self.clear_button.bind(on_press=self.clear_inputs)
        self.button_layout.add_widget(self.clear_button)

        self.add_widget(self.button_layout)

    def setup_equations(self, instance):
        try:
            self.equation_count = int(self.input_field.text)
        except ValueError:
            self.input_label.text = "Invalid input. Enter a number."
            return

        self.equation_layout.clear_widgets()
        self.coefficients = []
        self.constants = []

        # Header Row: Coefficients and Constants
        self.equation_layout.add_widget(Label(text="", size_hint_y=None, height=40))  # Empty cell
        self.equation_layout.add_widget(Label(text="Coefficients", size_hint_y=None, height=40))
        self.equation_layout.add_widget(Label(text="Constant", size_hint_y=None, height=40))

        # Rows for equations
        for i in range(self.equation_count):
            eq_label = Label(text=f"Eq {i + 1}", size_hint_y=None, height=100)  # Increased height for symmetry
            self.equation_layout.add_widget(eq_label)

            coefficient_input = TextInput(multiline=False, hint_text="e.g., 1 2 -3", size_hint_y=None, height=100)
            self.coefficients.append(coefficient_input)
            self.equation_layout.add_widget(coefficient_input)

            constant_input = TextInput(multiline=False, hint_text="e.g., 4", size_hint_y=None, height=100)
            self.constants.append(constant_input)
            self.equation_layout.add_widget(constant_input)

    def solve(self, instance):
        try:
            coefficients = [
                list(map(float, coeff.text.split()))
                for coeff in self.coefficients
            ]
            constants = [float(const.text) for const in self.constants]
            solutions = solve_equations(coefficients, constants)
            if isinstance(solutions, str):
                result_text = solutions
            else:
                result_text = "Solutions:\n" + "\n".join(
                    [f"x{i + 1} = {val:.2f}" for i, val in enumerate(solutions)]
                )
        except ValueError:
            result_text = "Invalid input. Please check your coefficients and constants."

        self.show_result(result_text)

    def show_result(self, result_text):
        # Popup to display results
        popup_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        result_label = Label(text=result_text, halign="center", valign="middle")
        result_label.text_size = (400, None)

        close_button = Button(text="Close", size_hint=(1, 0.2))
        close_button.bind(on_press=lambda x: self.dismiss_popup())

        popup_layout.add_widget(result_label)
        popup_layout.add_widget(close_button)

        self.result_popup = Popup(
            title="Result",
            content=popup_layout,
            size_hint=(0.8, 0.5),
            auto_dismiss=False,
        )
        self.result_popup.open()

    def dismiss_popup(self):
        self.result_popup.dismiss()

    def clear_inputs(self, instance):
        self.input_field.text = ""
        self.equation_layout.clear_widgets()


class LinearEquationSolverApp(App):
    def build(self):
        return SolverApp()


if __name__ == "__main__":
    LinearEquationSolverApp().run()
