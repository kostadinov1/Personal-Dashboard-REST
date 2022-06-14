

def apply_query_filters(self, queryset):
    filter_options = {}
    for filter_name in self.query_fitler_names:
        value = self.request.query_params.get(filter_name, None)
        if value:
            filter_options[f'{filter_name}_id'] = value

    return queryset.filter(**filter_options)