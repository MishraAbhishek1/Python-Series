# 12️⃣ Role-Based Access Control

def has_permission(role, action):
    permissions = {
        'admin' : ['create', 'read', 'update', 'delete'],
        'user' : ['read']
    }
    return action in permissions.get(role, [])

print(has_permission('admin', 'delete'))
print(has_permission('user', 'delete'))