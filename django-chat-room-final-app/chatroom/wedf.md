## ?q=something
- Q query set for and /or command over database
- pagination , indexing
# indexing is used generally when ek col ke liye you generally search for
- also you can use / see django query (what is actually being sent in the database)
```python
from django.paginator import Paginator
rooms = Room.objects.all().order_by('id')  # Doesn't fetch yet(lazy load)
paginator = Paginator(rooms, 20)  # Creates a paginator 
page_number = 1  # Assume first page
page_obj = paginator.get_page(page_number)
```
'''
We can also see SQL query of what is being sent like
'''
print(str(rooms.query)) using this
'''
It actually generates 
```SQL
SELECT * from room ORDER BY id LIMIT 20 OFFSET 0;
