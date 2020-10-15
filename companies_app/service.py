
def get_object(self, snippet, pk):

    try:
        return snippet.objects.get(pk=pk)
    except snippet.DoesNotExist:
        raise snippet