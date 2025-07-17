# 🌻Summer Fun with LLMs 🌻

## Python Virtual Environment Documentation

## Why We Need Virtual Environments

Virtual environments are isolated Python environments that allow you to manage dependencies separately for different projects. Here's why they're essential:

**Problem Without Virtual Environments:**
- Different projects may require different versions of the same package
- Installing packages globally can lead to version conflicts
- System Python packages might get corrupted
- Difficult to replicate project environments on other machines

**Benefits of Virtual Environments:**
- Each project has its own isolated set of dependencies
- No version conflicts between projects
- Easy to share exact package requirements with others
- Clean separation between project dependencies and system Python

## How to Create and Use Virtual Environments

### 1. Check if venv is Available
First, ensure you have Python 3.3+ installed (venv comes built-in):

```bash
python3 --version
```

### 2. Create a Virtual Environment
Navigate to your project directory and create the virtual environment:

```bash
# Create virtual environment named 'mychat_env'
python3 -m venv mychat_env
```

This creates a new directory `mychat_env` containing the isolated Python environment.

### 3. Activate the Virtual Environment
```bash
# Activate the environment
source mychat_env/bin/activate
```

When activated, your terminal prompt will show `(mychat_env)` at the beginning, indicating you're working inside the virtual environment.

### 4. Verify Activation
```bash
# Check which Python is being used
which python
# Should show: /path/to/your/project/mychat_env/bin/python

# Check installed packages (should be minimal)
pip list
```

### 5. Deactivate the Environment
When you're done working on your project:

```bash
deactivate
```

The `(mychat_env)` prefix will disappear from your prompt.

## Installing Packages with pip

### Basic pip Usage
With your virtual environment activated, you can install packages:

```bash
# Make sure environment is activated
source mychat_env/bin/activate

# Install a package
pip install package_name

# Install specific version
pip install package_name==1.2.3

# Upgrade a package
pip install --upgrade package_name

# Uninstall a package
pip uninstall package_name
```

### Example: Installing Streamlit

Let's install Streamlit as an example:

```bash
# 1. Activate your environment
source mychat_env/bin/activate

# 2. Install Streamlit
pip install streamlit

# 3. Verify installation
pip list | grep streamlit

# 4. Check Streamlit version
streamlit --version
```

### Create a Simple Streamlit App
Create a file called `app.py`:

```python
import streamlit as st

st.title("My Chat App")
st.write("Hello from my virtual environment!")

user_input = st.text_input("Enter your message:")
if user_input:
    st.write(f"You said: {user_input}")
```

Run the app:
```bash
streamlit run app.py
```

## Managing Dependencies

### Save Current Environment
Create a requirements file to share your environment:

```bash
# Generate requirements.txt
pip freeze > requirements.txt
```

### Recreate Environment from Requirements
On another machine or for a teammate:

```bash
# Create new environment
python3 -m venv mychat_env

# Activate it
source mychat_env/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

## Complete Workflow Example

Here's a complete workflow for starting a new project:

```bash
# 1. Create project directory
mkdir my_streamlit_project
cd my_streamlit_project

# 2. Create virtual environment
python3 -m venv mychat_env

# 3. Activate environment
source mychat_env/bin/activate

# 4. Install dependencies
pip install streamlit pandas numpy

# 5. Create your Python files
touch app.py

# 6. Save dependencies
pip freeze > requirements.txt

# 7. When done working
deactivate
```

## Best Practices

1. **Always activate** your virtual environment before working on a project
2. **One environment per project** - don't share environments between unrelated projects
3. **Keep requirements.txt updated** whenever you install new packages
4. **Add virtual environment folder to .gitignore** - don't commit the `mychat_env` directory
5. **Use descriptive names** for your environments related to your project

## Common Commands Summary

```bash
# Create environment
python3 -m venv mychat_env

# Activate (must do this each time you start working)
source mychat_env/bin/activate

# Install packages
pip install streamlit

# Save requirements
pip freeze > requirements.txt

# Deactivate
deactivate

# Remove environment (delete the folder)
rm -rf mychat_env
```

This approach gives you complete control over your Python project dependencies while keeping your system Python clean and organized.