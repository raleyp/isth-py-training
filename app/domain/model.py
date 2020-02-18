from related import to_model, to_dict, from_json
import related


@related.mutable
class Usuario:
    Username = related.StringField(required=False)
    Nombre = related.StringField(required=False)
    Apellido = related.StringField(required=False)

    @staticmethod
    def load(dictionary):
        return to_model(Usuario, dictionary)

    def provide(self):
        d = to_dict(self)
        return d
