
class Client:
    CIF = 1
    Name = 'Default'
    LastName = 'Default'
    Link = 'Default'
    age = 18
    isAdult = True

    @staticmethod
    def load(objeto):
        return related.from_json(objeto, Client)

    def provide(self):
        return related.to_json(self)
