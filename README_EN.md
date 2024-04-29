# Creative Magic Zoltraak
Zoltraak is the name of a powerful creative magic that symbolizes the beginning of a true magical era.

It is a system that elevates the invocation of techniques from unstructured spells to a grammatical system of magic, enabling faster and more powerful technique deployment and magic invocation.

![](assets/images/dai4697_A_digital_painting_of_a_female_wizard_casting_a_powerfu_84046a02-5831-48c1-b8e3-c8b5a49d69e8.png)

Zoltraak adopts a prompt compiler system that converts natural language into an execution language. It takes a few words of incantation, expands them into complex techniques, and compiles them into an immediately executable ancient system language. This allows the magician's few words of incantation to pass through a magic circle woven with powerful words of power, greatly enhancing the range and power of the magic. It also enables high-speed creative magic with or without chanting. This makes it possible to invoke techniques overwhelmingly faster and more flexibly than the opposing enemy.

TODO in the future:
There is no need to worry about the spells being extracted and reverse-engineered by others, as it is possible to compile them into unique language spells and encrypted spells. After fine-tuning, it can be compressed into an ancient language to conceal the spells. Also, by using a unique language and making minor modifications to a few words, the execution language changes instantly and the technique is invoked.

# Table of Contents

- [Research](docs/research.md)
- [Configuration](docs/configuration.md) 
- [FAQ](docs/faq.md)
- [Getting Started](docs/getting-started.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Examples](docs/examples)  
- [Troubleshooting](docs/troubleshooting.md)
- [Video](docs/video.md)
- [Contributing](docs/contributing.md)

![Last frame of video](assets/images/last_frame.png)

## Usage

1. Install Zoltraak
   ```sh
   pip install --upgrade zoltraak
   ```

## Usage 

1. How to use
   1. Set the following environment variables in the `.env` file.
      ```
      ANTHROPIC_API_KEY={Anthropic key}
      ```
   2. Install Zoltraak with the following command:
      ```
      pip install zoltraak
      ```
   3. Run the following command and enter a prompt:
      ```
      zoltraak "I want to create a Pokemon-like game system where you can learn the latest large language models" -c dev_obj
      ```

   This will generate a requirements document based on the entered prompt. The generated requirements document serves as a draft, so modify and expand the content as needed.

2. Specifying the prompt compiler (invocation formula)
   The prompt compiler (invocation formula) that can be changed according to the purpose is specified after the `-c` option. Running without this option will present you a search result that shows the top 5 most-suited compiler for your request.

   | Compiler Name | Description |
   | --- | --- |
   | dev_func | A compiler that generates requirements documents for development tasks using functional programming |
   | dev_obj | A compiler that generates requirements documents for development tasks using object-oriented design |
   | biz_consult | A compiler that generates documents related to business consulting |
   | general_def | A compiler that generates requirements documents for general development tasks |
   | general_reqdef | A compiler that generates requirements documents for general requirements |
   | dev_react_fastapi | A compiler that generates requirements documents for development tasks using React + FastAPI |

3. Specific examples
   ```sh
   zoltraak "Develop a program to visualize the MoE (Mixture of Experts) model using Manim" -c dev_func
   zoltraak "Develop a multifunctional inventory management system using object-oriented design by the end of this month" -c dev_obj
   zoltraak "Create a business consulting document for small and medium-sized enterprises by the end of this month. Specifically, it should include advice on marketing strategies, financial management, and human resource development" -c biz_consult
   zoltraak "Develop an educational augmented reality (AR) application by the end of this month" -c general_def
   zoltraak "Write a proposal document for the government by the end of this month as a measure against the declining birthrate, including specific measures and budget proposals" -c general_reqdef
   ```

2. Create a file named `test_dev_obj.md` and copy and paste the content of the subsequent thread into it. Place this file at the same level as the directory where you run zoltraak.

3. Rewrite `test_dev_obj.md` into your own definition document generation program according to the following rules:
   - Do not delete `{prompt}` as it is where the prompt (spell) after zoltraak will be inserted.
   - Do not delete `## 2. File/Folder Structure` either.
   - Everything else can be freely modified.

4. Run the following command to use your custom compiler:
   ```sh
   zoltraak prompt -cc custom_compiler
   zoltraak "I want to create a coffee shop customer management system" -cc test_dev_obj.md
   ```

5. You should now be able to paste `zoltraak requirements/~~~.md`, so please execute it.

6. A directory will be built. For those who cannot launch the open command in Cursor or VSCode, please refer to the following:
   https://note.com/88gram/n/n4ead3a677b83

Note: Everything is executed by Claude3 Haiku (a fee of about 1 yen per time is charged. Please check for yourself).

```
zoltraak book.md -p "I want to write a book"
```

After creating the file, you can rewrite it as many times as you like as follows:
```
zoltraak book.md -p "I want to increase the volume"
```

```sh
# Specify the files to put into RAG
zoltraak aaaa.md -f ./input.md (planned)
# Batch modification
zoltraak dir/*.md (planned)
```

![llmcomment.png](assets/images/llmcomment.png)

### Optional Arguments
- ``-f``: Format specification. Located in the grimoires folder.
- ``-l``: Generic language specification. The language name can be in the local name such as "Español", in English like "Spanish", or in Japanese like "スペイン語" (Spanish).
  - If a generic language formatter (a file ending with "``_lang.md``") exists for the specified format, the processing will be based on that file.
  - If it doesn't exist, the default language set compiler will be triggered. However, since the effect is relatively less stable, it is highly recommended to create a generic language formatter.

```
zoltraak "Develop a multi-functional inventory management system using object-oriented design within this month" -c dev_obj -l English
zoltraak "Develop a multi-functional inventory management system using object-oriented design within this month" -c dev_obj -f md_comment -l CSharp
zoltraak "Develop a multi-functional inventory management system using object-oriented design within this month" -c dev_obj -l Georgian
```

## Joining the Project

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Zoltraak.git
   ```

2. Navigate to the project directory:
   ```
   cd Zoltraak
   ```

3. Install the necessary dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set your Anthropic API key:
   - Create a `.env` file in the project's root directory.
   - Add the following line to the `.env` file, replacing `YOUR_API_KEY` with your actual Anthropic API key:
     ```
     ANTHROPIC_API_KEY=YOUR_API_KEY
     ```

# Here are the general steps for developing a PyPI package in a local environment:

1. Creating a virtual environment
First, create an isolated virtual environment for package development. This allows you to develop in an environment separate from the system-wide Python.

```bash
python -m venv zoltraak-dev
source zoltraak-dev/bin/activate  # For Linux
mypackage-env\Scripts\activate.bat  # For Windows
```

2. Installing necessary packages
Install the packages required for development. For example, `setuptools` and `wheel` are the bare minimum.

```bash
pip install setuptools wheel
```

3. Package directory structure
Create the package with the following basic directory structure:

```
mypackage/
    mypackage/
        __init__.py
        module1.py
        module2.py
    tests/
        test_module1.py
        test_module2.py
    setup.py
    README.md
```

4. Creating `setup.py`
Create a `setup.py` file that describes the package's metadata and dependencies. For example:

```python
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # Dependencies
    ],
)
```

5. Installing the package
Install the package being developed into the virtual environment.

```bash
pip install -e .
```

Now you can use and make changes to the package within the virtual environment.

6. Using and testing the package
Proceed with development by using the package's functionality and running unit tests.

7. Building and distribution
Once completed, the package can be built and published to PyPI using the following commands:

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

This is the basic flow of PyPI package development in a local environment. The key points are to use a virtual environment and prepare an appropriate directory structure and `setup.py`.

### Additional Commands

update_and_upload.sh
```sh
echo "Updating version..."
python update_version.py

echo "Building package..."
python setup.py sdist bdist_wheel

echo "Uploading built package to PyPI..."
twine upload dist/*
```

## Directory Structure

```
zoltraak/grimoires/
├── compiler: Converter from incantation to natural language
│   ├── akirapp.md
│   ├── func.md
│   ├── lisp.md
│   ├── obj.md
│   ├── obj_mermaid.md
│   ├── obj_lisp.md
│   ├── obj_lisp_g.md
│   ├── obj_lisp_g_base64.md
│   └── reqdef.md
├── encryption: Encryption tools
│   └── emoji.md
├── formatter: Prompt formatters
│   ├── md_comment.md
│   ├── md_comment_xx.md (md_comment that can specify some languages including but not limited to en and zh. Try running it first with the abbreviated form of your target language. If it doesn't work, please wait for the further support)
│   └── py_comment.md
├── interpretspec: Interpreter-type LLM enhancement prompts
│   └── hirokichi.md
└── softdb: Soft DB

memo: Want to include an experimental system to benchmark all items in the grimoires directory

```

## Usage

To convert a Markdown file to Python code, use the following command:

## Caching

Zoltraak implements a caching mechanism to avoid unnecessary conversions of unchanged Markdown files. It calculates the hash value of each Markdown file and saves it in the `hashes.txt` file. When the conversion command is executed, Zoltraak compares the current hash value with the saved one. If the hash values match, indicating that the Markdown file has not been modified, the conversion is skipped, and the previously generated Python code is used.

## Integration with CI/CD

Zoltraak can be integrated into CI/CD workflows to automate the conversion process. The `run_tests.sh` script is provided to facilitate this integration. It performs the following steps:

1. Creates and activates a virtual environment.

2. Installs the necessary dependencies.

3. Converts the Markdown files to Python code.

4. Executes the generated Python code.

5. Runs the corresponding unit tests.

To use the `run_tests.sh` script in your CI/CD pipeline, configure your CI/CD system to execute the script as part of the build process.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

## TODO

### Urgent

- [ ] https://x.com/ai_syacho/status/1782956863912649114
- [ ] zoltraak "slkajfka" -c file_path (make it possible to use self-made compilers)

```
ModuleNotFoundError can be resolved by
pip install ~~~~

In this case,
pip install anthropic
will resolve the issue.

↓
pip install zoltraak
will be adjusted to install all dependencies in one go.
```

### CLI Command-related
- [ ] zoltraak -p "I want to create a manim video" - This generates a requirements document and a program
  
  -

### Document Generation
- [ ] Want documents of the generated Python files and detailed design documents.
  - Want to generate documents from Python files
    - Example: Specify a Python file like `Zoltraakgenerated/calc.py` to generate or update the corresponding markdown document for that file
    - Automatically generate documents from docstrings and comments in the Python file
    - Output the generated documents in markdown format

### Testing
- [ ] Test files should be created separately and executed at necessary timings, such as git push.

### Issue Management
- [ ] Want to describe issues.

### File Management
- [x] When using repeatedly, automatically associate Markdown files with Python files. (Recompile only if there are changes)

### Requirements Definition-related
- [ ] Implement a program to generate a requirements document from a read-aloud text in Akira-san's project.
  - It seems better to mix declarative and procedural styles together
- [ ] ZoltraakAAA.md ~want to modify the requirements document
- [ ] It would be nice to have a prompt document for deciding requirements definition
  - Want to select the compiler file
- [ ] Need a flow to go back from a program to requirements definition.

### Others
- [ ] It is good to prepare an intermediate file in advance to eliminate strange quirks of various high-level languages.
- [ ] Please tell me the number of lines of the prompt that correspond to the color in this file.
- [ ] Want to communicate the diff as a prompt.
- [ ] Rebuild everything from scratch. From md file
![image](assets/images//graph.png)

## Overall Flow

- ① Ambiguous and abstract: The initial prompt corresponds to this. A vague requirement like "I want to do something."

shell
```
zoltraak "I want to write a book"
```
↓

md file
gen_def_{goal}.md

```
# Goal: I want to write a book
Requirements Document:
{def}
```
↓

- ② Precise and abstract: Requirements documents, etc. By creating a definition document from the prompt, ambiguity is eliminated, and it becomes an abstract state.
def_{goal}.md
```
Book Writing Requirements Document:
import {def}
import {def}
import {def}

~~~~~~~
~~~~~~~
~~~~~~~
~~~~~~~
~~~~~~~
```
↓

- ③ Ambiguous and concrete: Accompanied by concrete actions but still in the trial-and-error stage. It can also be called interactive (interpreter).
exe_{goal}.py
```
program # comment
program # comment
program # comment
program # comment
```
- ④ Precise and concrete: Narrowed down to a single concrete action and manualized (document type, compiled).

exe_{goal}.md
```
Detailed procedure (encrypt, abstract, make it easy for users to understand)

```

zoltraak book.md

### Genealogy of Natural Language Programming

```
*Emergence of ChatGPT
    |→ Prompt Engineering
        *Need for system development application of prompts
            |→ Prompt Programming
                *Emergence of Claude3 Opus
                |→ Document Programming
                    |→ Natural Language Programming
                            motoki → arbor → zoltraak
                                        *Groq x Llama3's fast text output control without interaction
                                                |→ Natural Language Framework zoltraak
                                                |→ Unified Programming Language babel
                                                                        ↑ Current Stage
```

### How to Upload

Here are the steps to upload a package to PyPI:

1. Preparing the package:
   - Set up the appropriate directory structure for your project.
   - Create a `setup.py` file and describe the package information (name, version, dependencies, etc.).
   - Create a `README.md` file and provide a description and usage instructions for the package.

2. Creating an account and obtaining an API token:
   - Access the PyPI website (https://pypi.org/).
   - Create a new account or log in to an existing account.
   - Generate an API token on the account settings page.

3. Installing build and upload tools:
   - Install `twine` and `setuptools`.
     ```
     pip install twine setuptools
     ```

4. Building the package:
   - Execute the following command in the project's root directory to build the package:
     ```
     python setup.py sdist bdist_wheel
     ```
   - This will generate the distribution files for the package in the `dist` directory.

5. Uploading to PyPI:
   - Execute the following command to upload the package to PyPI:
     ```
     twine upload dist/*
     ```
   - Use the obtained API token instead of the username and password.

6. Verifying the upload:
   - Access the PyPI website and confirm that the uploaded package is displayed correctly.

Now the `zoltraak` package is published on PyPI. Users can install the package using the `pip install zoltraak` command.

Notes:
- The package name must be unique. You cannot use a name that already exists.
- The version number needs to be incremented each time you upload a new version.
- Ensure that the `setup.py` file includes the appropriate metadata and dependencies.
- Clearly describe the package's description and usage instructions in the `README.md` file.

This covers the steps for uploading a package to PyPI. If you encounter any issues, refer to the PyPI documentation or seek help from the community.

## Executing in a Virtual Environment

`pyenv` is a Python version management tool, but it does not have a direct feature to create virtual environments. To create a virtual environment, you need to use a plugin called `pyenv-virtualenv`.

Here are the steps to create a virtual environment using `pyenv-virtualenv`:

1. **Installing pyenv-virtualenv**

   First, install the `pyenv-virtualenv` plugin. This assumes that `pyenv` is already installed.

   ```bash
   git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
   ```

   After installation, add the following to your shell configuration file (e.g., `.bashrc` or `.zshrc`) and restart your shell.

   ```bash
   eval "$(pyenv init --path)"
   eval "$(pyenv virtualenv-init -)"
   ```

2. **Installing Python**

   Use `pyenv` to install the Python version for the virtual environment.

   ```bash
   pyenv install 3.8.5  # Example: Install Python 3.8.5
   ```

3. **Creating a Virtual Environment**

   Next, create a virtual environment with the specified Python version.

   ```bash
   pyenv virtualenv 3.8.5 my-virtual-env-3.8.5
   ```

   Here, `my-virtual-env-3.8.5` is the name of the virtual environment.

4. **Activating the Virtual Environment**

   Activate the created virtual environment.

   ```bash
   pyenv activate my-virtual-env-3.8.5
   ```

   This activates the specified virtual environment.

5. **Deactivating the Virtual Environment**

   To deactivate the virtual environment, use the following command:

   ```bash
   pyenv deactivate
   ```

This explains how to create and manage Python virtual environments using `pyenv` and `pyenv-virtualenv`.

Local Environment

Running `pip install -e .` seems to install the package in `Users/motokidaisuke/.pyenv/versions/3.11.5`.

python setup.py sdist bdist_wheel
twine upload --verbose dist/*

Virtual Environment
deactivate
rm -rf /Users/motokidaisuke/aaaaa/zoltraak-env
python3 -m venv /Users/motokidaisuke/aaaaa/zoltraak-env
source /Users/motokidaisuke/aaaaa/zoltraak-env/bin/activate

# Idea (Important)

Incantation → Document → Structure → Information Structure → Execution
              |→ Natural Language     |→ Natural Language
                                          |→ Programming Language

# Memo

```
import compiler.dev.obj
import writer.book.lecture
```

# TODO

- [ ] Make the directory construction not pasted but asked to be built from the system
- [ ] Functionalize the Python file retrieval part and externalize it
- [ ] Introduce designers and developers.

# Contributors

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-0-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## How to add a contributor

To add a contributor, follow these steps:

1. Leave a comment on an issue or pull request in the following format:
@all-contributors please add @username for <contributions>
Replace `@username` with the GitHub username of the contributor and `<contributions>` with the type of contributions they made. Contribution types can be found in the [Emoji Key](https://allcontributors.org/docs/en/emoji-key).

2. The bot will then create a pull request to add the contributor to the project.

3. Once the pull request is merged, the contributor will be added to the README.
