person = {
    'gender': 'male',
    'name': 'Jonny'
}

# He went to the store

print(f"{'He' if person.get('gender') == 'male' else 'She'} went to the store.")