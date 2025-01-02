# Linear Equation Solver Using Cramer's Rule

This Python application solves systems of linear equations using **Cramer's Rule**. The app features an interactive GUI built with Kivy, allowing users to input equations dynamically and compute solutions efficiently.

---

## Features

- **User-Friendly Interface**: Intuitive fields for entering coefficients and constants.
- **Cramer's Rule Implementation**: Solves equations step-by-step using determinants.
- **Error Handling**: Detects invalid inputs or unsolvable systems (e.g., determinant = 0).
- **Scrollable Input Fields**: Supports large systems of equations.
- **Popup Results**: Displays solutions or error messages interactively.
- **Clear Button**: Resets inputs for new calculations.

---

## Installation Instructions

### Prerequisites

Ensure you have Python (3.8 or later) installed. Install Kivy for GUI support.

### Steps to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/ArunKumarMohanta/LinearEquationSolver-with-GUI
    cd LinearEquationSolver-with-GUI
    ```
2. Install dependencies:
    ```bash
    pip install kivy
    ```
3. Run the application:
    ```bash
    python main.py
    ```

---

## Usage

1. Launch the application.
2. Enter the number of equations.
3. Input coefficients and constants for each equation.
4. Click **Solve** to calculate the solutions.
5. View results in the popup window.
6. Use the **Clear** button to reset the fields.

---

## Screenshots

### Initial Interface

The main interface allows you to specify the number of equations.

![image](https://github.com/user-attachments/assets/d159894d-115a-435a-9fc0-1587bd3f7429)


### Dynamic Input Fields

Based on the number of equations, dynamic fields appear for coefficients and constants.

![image](https://github.com/user-attachments/assets/d3f11eb4-32ba-4f26-8c65-bdde1affbd03)


### Results Popup

The solutions or any error messages (e.g., no solution) are displayed in a popup window.

![image](https://github.com/user-attachments/assets/684514dd-bc6e-4cea-99be-e23f0521d5cc)


---

## Code Explanation

### Core Functions

1. **`det(matrix)`**:
    - Computes the determinant of a matrix recursively.
2. **`replace_column(matrix, constants, column_index)`**:
    - Replaces a column in the coefficient matrix with the constants column.
3. **`solve_equations(coefficients, constants)`**:
    - Solves the equations using **Cramer's Rule**.

### Kivy GUI

- **`TextInput`**: Fields for coefficients and constants.
- **`Label`**: Provides descriptions for each row.
- **`Button`**: Triggers actions like solving or clearing.
- **`Popup`**: Displays results or errors.

### Code Structure

- **Main Class (`SolverApp`)**:
    - Handles GUI elements like input layout, equation setup, and result display.
- **Helper Functions**:
    - Determinant calculation.
    - Matrix manipulation for Cramer's Rule.

---

## Future Enhancements

- Add support for alternate solving methods (e.g., Gaussian Elimination).
- Provide graphical representations of the equations.
- Implement a dark mode for improved user experience.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for bugs or suggestions.

---

## Contact

If you have any questions or feedback, feel free to reach out:

- **Developer**: Arun Kumar Mohanta
- **Email**: mahantarunkumar809@gmail.com
- **GitHub Profile**: [Arun Kumar Mohanta](https://github.com/ArunKumarMohanta)

---

Happy Coding!
