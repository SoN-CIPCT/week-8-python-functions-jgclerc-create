def sandwich_maker(*ingredients):
     """Display ingredients"""
     print('Making a sandwich with the following ingredients:')
     for ingredient in ingredients:
          print(f'-{ingredient}')

sandwich_maker('tomato', 'mayo')
sandwich_maker('ham','mustard','pepperjack cheese')


