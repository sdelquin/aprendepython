smb_path = '//1.1.1.1/eoi/python'

smb_path = smb_path[2:]
slash_position = smb_path.index('/')
host = smb_path[:slash_position]
path = smb_path[slash_position:]
print(f'host={host}; path={path}')
