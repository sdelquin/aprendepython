HTAG_SIZE = 3
MD_HEADING_SYMBOL = '#'

html = '<h3>Cadenas de texto</h3>'

start_tag_index1 = html.find('<h')
start_tag_index2 = start_tag_index1 + HTAG_SIZE

end_tag_index1 = html.find('</h')
end_tag_index2 = end_tag_index1 + HTAG_SIZE + 1

heading_level = html[start_tag_index2 - 1]
heading_title = html[start_tag_index2 + 1 : end_tag_index1]

heading_rep = '#' * int(heading_level)

markdown = f'{heading_rep} {heading_title}'
print(markdown)
