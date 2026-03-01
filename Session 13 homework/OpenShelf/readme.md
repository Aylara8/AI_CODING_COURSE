I used TEXT for fields like username, email, and title. Since these values vary in length and consist of alphanumeric characters, TEXT is the standard choice. Even though some fields like password look like a mix of characters and numbers, they are stored as TEXT because we do not perform mathematical operations on them.
Currently, I do not have any list fields in my models. However, if I wanted to add a "Tags" feature (e.g., marking a resource as both "Python" and "Backend"), I cannot store a Python list directly in a standard SQL cell.
To handle this, I would use a Many-to-Many relationship. This involves creating a separate Tags table and a "Join Table" that contains pairs of resource_id and tag_id. This keeps the data organized and searchable.
My project already uses multiple tables: User, Profile, and Resource. This structure is beneficial for several reasons:
RI don't have to save a user's email and password every time they upload a new file. I just save their user_id.
It separates account logic from content logic.
I used AJAX in app_route delete_resource.