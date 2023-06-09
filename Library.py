from DatabaseManager import DatabaseManager

class Library:
    def __init__(self, library_id: int,
                 name: str,
                 phone: str = None,
                 address: str = None) -> None:
        self.library_id: int = library_id
        self.name: str = name
        self.phone: str = phone
        self.address: str = address

    @classmethod
    def get_info(cls, lib_id: int = 3) -> 'Library':
        cursor = DatabaseManager.get_cursor()
        cursor.execute("""
            SELECT * FROM library WHERE library_id = ?
        """, lib_id)
        lib = cursor.fetchone()
        if not lib:
            return None
        return Library(int(lib[0]), lib[1], lib[2], lib[3])