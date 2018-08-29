class AnimalShelter:
    def __init__(self):
        self.animals = []

    def isEmpty(self):
        return self.animals == []

    def enqueue(self, animal):
        self.animals.insert(0, animal)

    def dequeue(self, pref):
        if pref in self.animals:
            self.animals.remove(pref)
            return pref
        else:
            return self.animals.pop()

    def size(self):
        return len(self.animals)
    
    def get(self):
        return self.animals


q = AnimalShelter()
q.enqueue('cat')
q.enqueue('cat')
q.enqueue('dog')
q.enqueue('dog')

print(q.get())
print(q.dequeue('pref'))
print(q.get())
