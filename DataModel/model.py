from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)

class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')

if __name__ == '__main__':
    #---------Create, Update, Delete operations
    config.DATABASE_URL = 'bolt://neo4j:123@localhost:11004'

    jim = Person(name='Jim', age=3).save() # Create
    jim.age = 4
    jim.save() # Update, (with validation)
    #jim.delete()
    #jim.refresh() # reload properties from the database
    print(jim.id) # neo4j internal id

    #-------- Retrieving nodes
    # Return all nodes
    all_nodes = Person.nodes.all()
    print(all_nodes)
    # Returns Person by Person.name=='Jim' or raises neomodel.DoesNotExist if no match
    jim = Person.nodes.first(name='Jim')
    print(jim)
    # # Will return None unless "bob" exists
    someone = Person.nodes.get_or_none(name='bob')


    #---------- Relationships
    germany = Country(code='DE').save()
    jim.country.connect(germany)

    if jim.country.is_connected(germany):
        print("Jim's from Germany")

    for p in germany.inhabitant.all():
        print(p.name)  # Jim

    len(germany.inhabitant)  # 1

    # Find people called 'Jim' in germany
    germany.inhabitant.search(name='Jim')

    # Find all the people called in germany except 'Jim'
    germany.inhabitant.exclude(name='Jim')

    # Remove Jim's country relationship with Germany
    jim.country.disconnect(germany)

    usa = Country(code='US').save()
    jim.country.connect(usa)
    jim.country.connect(germany)

    # Remove all of Jim's country relationships
    jim.country.disconnect_all()

    jim.country.connect(usa)
    # Replace Jim's country relationship with a new one
    jim.country.replace(germany)

    # Will return the first Person node with the name bob or None if there's no match
    someone = Person.nodes.first_or_none(name='bob')

    # Return set of nodes
    people = Person.nodes.filter(age__gt=3)