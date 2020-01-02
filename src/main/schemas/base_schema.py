from graphene import Interface, UUID


class ID(Interface):
    id = UUID(required=True)
