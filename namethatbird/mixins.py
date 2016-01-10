from mongoengine import EmbeddedDocumentField, ObjectIdField


class NameThatBirdMixin(object):

    def as_dict(self):
        """ Convert MongoEngine documents to dict representation

        EmbeddedDocumentField's are recursively converted to dict's, as well

        :return:
        """
        out = {}
        for field, field_type in self._fields.iteritems():

            if isinstance(field_type, EmbeddedDocumentField):
                out[field] = getattr(self, field).as_dict()
            elif isinstance(field_type, ObjectIdField):
                out[field] = str(getattr(self, field))
            else:
                out[field] = getattr(self, field)

        return out