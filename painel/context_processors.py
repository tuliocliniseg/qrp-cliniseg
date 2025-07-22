def empresa_slug(request):
    return {
        'empresa_slug': request.GET.get('empresa_slug', '')
    }