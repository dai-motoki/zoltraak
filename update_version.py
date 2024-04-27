#!/usr/bin/env python

with open('setup.py', 'r') as file:
    content = file.read()
start = content.find('version="') + 9
end = content.find('",', start)
current_version = content[start:end]

parts = current_version.split('.')
parts[-1] = str(int(parts[-1]) + 1)
new_version = '.'.join(parts)

updated_content = content.replace(current_version, new_version)

with open('setup.py', 'w') as file:
    file.write(updated_content)
