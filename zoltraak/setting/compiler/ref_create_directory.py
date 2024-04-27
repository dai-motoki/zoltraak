
import os

# Root directory
root = './'

# Files to be created at each directory
dir_files = {
    'docs': ['getting-started.md', 'installation.md', 'configuration.md', 'usage.md', 'troubleshooting.md', 'faq.md'],
    'docs/examples': ['example1.md', 'example2.md'],
    'src': []
}

# Create directories and files
for dir, files in dir_files.items():
    os.makedirs(os.path.join(root, dir), exist_ok=True)
    for file in files:
        open(os.path.join(root, dir, file), 'w').close()

# Create file at root directory
with open(os.path.join(root, 'README.md'), 'w') as f:
    f.close()

# Check if directories and files are created
for dir, files in dir_files.items():
    print('Directory:', dir)
    print('Contains files:', os.listdir(os.path.join(root, dir)))
    