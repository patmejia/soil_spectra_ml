# integrate cookiecutter data science into an existing project

1. **clone repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
   
2. **create new branch**:
   ```bash
   cd your-repo
   git checkout -b restructuring
   ```

3. **install cookiecutter** (if not already installed):
   ```bash
    python3 -m pip install cookiecutter    
   ```

4. **generate cookiecutter structure**:
   ```bash
   cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
   ```
   **note**: `-c v1` is to use the v1 version of the template. the v2 version is not yet released.

   be prepared to provide the followings:
   - `project_name`
   - `repo_name`
   - `author_name`
   - `description`
   - `open_source_license`: mit (options: 1 - mit, 2 - bsd-3-clause, 3 - no license file)
   - `s3_bucket`: [optional] your-bucket-for-syncing-data (if you want to use aws s3)
   - `aws_profile`: default
   - `python_interpreter`: python3 (options: 1 - python3, 2 - python)

5. **migrate existing files**:
   - manually copy or move files from your existing repository to the corresponding directories in the new cookiecutter structure.

6. **test the setup**:
   - ensure your project operates as expected in the new structure.

7. **commit and push changes**:
   ```bash
   git add .
   git commit -m "restructured project to adhere to cookiecutter data science template"
   git push origin restructuring
   ```

8. **open a pull request and merge**:
   - create a pull request for the `restructuring` branch, review the changes, and merge it into the `main` or `master` branch.

9. **update documentation**:
   - update `readme.md` and other documentation to reflect the new project structure.
