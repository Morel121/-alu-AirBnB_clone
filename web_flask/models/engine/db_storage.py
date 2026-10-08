def close(self):
        """Call remove() on the private session attribute (self.__session)."""
        self.__session.remove()
