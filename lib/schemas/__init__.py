
import json

class Schema:

    @classmethod
    def _build(cls):
        # Atrributes
        #print(cls)
        attrs = [ attr for attr in dir(cls) if not attr.startswith('_') ]

        # Create instance
        ctx = json.dumps(json.loads(cls._ctx))
        instance = cls()

        # Convert to JSON object
        obj = {}
        for attr in attrs:
            obj[attr] = getattr(cls, attr).lookup(ctx)

        # Print it
        formatter = cls().__str__()
        print(formatter.format(**obj))