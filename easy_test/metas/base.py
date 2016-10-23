from easy_test.metas.options import Options


class BaseMeta(type):
    """
    Metaclass for all tests
    """
    def __new__(cls, name, bases, attrs):
        super_new = super(BaseMeta, cls).__new__

        # Ensure initialization is only performed for subclasses of Meta
        parents = [b for b in bases if isinstance(b, BaseMeta)]
        if not parents:
            new_class = super_new(cls, name, bases, attrs)
            setattr(new_class, '_concrete', False)
            return new_class

        # Create the class.
        module = attrs.pop('__module__')
        new_class = super_new(cls, name, bases, {'__module__': module})
        attr_meta = attrs.pop('Meta', None)
        if not attr_meta:
            meta = getattr(new_class, 'Meta', None)
        else:
            meta = attr_meta
        setattr(new_class, '_concrete', True)
        setattr(new_class, '_meta', Options(meta))

        cls.validate(cls, new_class._meta, module, name)

        return new_class

    def validate(cls, meta, module, name):
        """
        Validate the settings from meta class
        """
        obj = getattr(meta, 'obj', None)
        if obj is None:
            raise RuntimeError(
                "Test class %s.%s doesn't declare an explicit "
                "object." % (module, name)
            )


