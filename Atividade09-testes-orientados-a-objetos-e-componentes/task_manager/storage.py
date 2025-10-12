"""Armazenamento em memória para tarefas."""

class InMemoryStorage:
    def __init__(self):
        self._data = {}

    def add(self, id, item):
        self._data[id] = item

    def get(self, id):
        return self._data.get(id)

    def get_all(self):
        return list(self._data.values())

    def update(self, id, item):
        self._data[id] = item

    def remove(self, id):
        if id in self._data:
            del self._data[id]
            return True
        return False

    def delete(self, id):
        return self.remove(id)

    def clear(self):
        self._data.clear()
