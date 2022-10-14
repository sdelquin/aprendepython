import sys

number = int(sys.argv[1])
tobase = int(sys.argv[2])

match tobase:
    case 2:
        result = f'{number:b}'
    case 8:
        result = f'{number:o}'
    case 16:
        result = f'{number:x}'
    case _:
        result = None

if result is None:
    print(f'Base {tobase} not implemented!')
else:
    print(result)
