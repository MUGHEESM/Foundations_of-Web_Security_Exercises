def search_users(cursor, term):
    sql = f"SELECT id, username FROM users WHERE username LIKE '%{term}%'"
    cursor.execute(sql)
    return cursor.fetchall()
