input_file_path = 'README.md'
output_file_path = 'output.html'

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        markdown_text = f.read()

    html_content = parse_markdown_to_html(markdown_text)

    with open(output_file, 'w') as f:
        f.write(html_content)

def parse_markdown_to_html(markdown_text):
    lines = markdown_text.split('\n')
    html_lines = []
    in_list = False

    for line in lines:
        if line.startswith('###'):
            # Heading 3
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('##'):
            # Heading 2
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('#'):
            # Heading 1
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif '**' in line:
            # bold
            line = line.replace('**', '<b>',1)
            line = line.replace('**', '</b>', 1)
            html_lines.append(line)
        elif '*' in line:
            # italic
            line = line.replace('*', '<i>',1)
            line = line.replace('*', '</i>', 1)
            html_lines.append(line)
        elif line.startswith('1. '):
            # Ordered list
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            html_lines.append(f'  <li>{line[3:]}</li>')
        elif not line.strip() and in_list:
            # End of list
            html_lines.append('</ol>')
            in_list = False
        elif in_list:
            html_lines.append(f'  <li>{line[3:]}</li>')
        elif '![' in line and ']' in line and '(' in line and ')' in line:
            # image
            img_text = line[line.find('![') + 2:line.find(']')]
            img_path = line[line.find('(') + 1:line.find(')')]
            html_lines.append(f'<img src="{img_path}" alt="{img_text}"/>')
        elif '[' in line and ']' in line and '(' in line and ')' in line:
            # Link
            link_text = line[line.find('[') + 1:line.find(']')]
            link_url = line[line.find('(') + 1:line.find(')')]
            html_lines.append(f'<a href="{link_url}">{link_text}</a>')
        else:
            # Paragraph
            html_lines.append(f'<p>{line}</p>')

    return '\n'.join(html_lines)

convert_markdown_to_html(input_file_path, output_file_path)