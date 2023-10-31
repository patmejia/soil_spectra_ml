### Steps to Run the Script

1. **Create a New `conda` Environment**: Create an isolated environment for your project.

    ```bash
    conda create --name soil_spectra_ml python=3.8
    ```

2. **Activate the Environment**: Activate your newly created environment.

    ```bash
    conda activate soil_spectra_ml
    ```

3. **Install Required Packages**: As the script uses Pandas and pathlib, let's install them.

    ```bash
    pip install pandas matplotlib seaborn
    ```

    Note: `pathlib` is part of Python’s standard utility modules, so you don't need to install it separately.

4. **Save the Script**: Save the provided Python script into a file, let's say named `read_and_explore_data.py`.

5. **Run the Script**: Run the script from the command line. Replace `path/to/data/directory` with the appropriate path to your data.

    ```bash
    python src/data_exploration.py --directory .
    ```