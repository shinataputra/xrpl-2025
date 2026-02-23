
print('What meal are you having?')
meal = input().lower()


if meal == 'pizza':
    print('A cold soda would be great with that!')
elif meal == 'pasta':
    print('Perhaps a glass of red wine would complement the dish.')
elif meal == 'sushi':
    print('Green tea is the classic choice.')
else:

    print(f'I do not have a specific drink recommendation for {meal}, but enjoy your meal!')
