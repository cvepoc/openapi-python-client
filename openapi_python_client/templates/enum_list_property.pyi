        {{ property.name }} = []
        for {{ property.name }}_item in d.get("{{ property.name }}", []):
            {{ property.name }}.append({{ property.reference.class_name }}({{ property.name }}_item))
